# Chapter 3: Advanced Terraform Concepts

Master advanced Terraform techniques for production-grade infrastructure.

## Topics Covered

1. [Dynamic Blocks](#dynamic-blocks)
2. [Count and For Each](#count-and-for-each)
3. [Terraform Functions](#terraform-functions)
4. [Conditional Expressions](#conditional-expressions)
5. [Workspaces](#workspaces)
6. [Provider Configuration](#provider-configuration)
7. [Import Existing Resources](#import-existing-resources)
8. [Security Best Practices](#security-best-practices)

## Dynamic Blocks

Dynamic blocks allow you to dynamically construct repeatable nested blocks.

### Basic Dynamic Block

```hcl
variable "ingress_rules" {
  type = list(object({
    port        = number
    protocol    = string
    cidr_blocks = list(string)
    description = string
  }))

  default = [
    {
      port        = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "HTTP"
    },
    {
      port        = 443
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
      description = "HTTPS"
    }
  ]
}

resource "aws_security_group" "web" {
  name        = "web-sg"
  description = "Security group with dynamic ingress rules"
  vpc_id      = aws_vpc.main.id

  # Dynamic ingress rules
  dynamic "ingress" {
    for_each = var.ingress_rules
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
      description = ingress.value.description
    }
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

### Nested Dynamic Blocks

```hcl
variable "s3_lifecycle_rules" {
  type = list(object({
    id      = string
    enabled = bool
    transitions = list(object({
      days          = number
      storage_class = string
    }))
  }))

  default = [
    {
      id      = "archive-old-objects"
      enabled = true
      transitions = [
        {
          days          = 30
          storage_class = "STANDARD_IA"
        },
        {
          days          = 90
          storage_class = "GLACIER"
        }
      ]
    }
  ]
}

resource "aws_s3_bucket_lifecycle_configuration" "bucket" {
  bucket = aws_s3_bucket.main.id

  dynamic "rule" {
    for_each = var.s3_lifecycle_rules
    content {
      id     = rule.value.id
      status = rule.value.enabled ? "Enabled" : "Disabled"

      dynamic "transition" {
        for_each = rule.value.transitions
        content {
          days          = transition.value.days
          storage_class = transition.value.storage_class
        }
      }
    }
  }
}
```

### Dynamic Blocks with Maps

```hcl
variable "tags_map" {
  type = map(string)
  default = {
    Environment = "prod"
    Team        = "platform"
    CostCenter  = "engineering"
  }
}

# Convert map to list for dynamic blocks
locals {
  tags_list = [for k, v in var.tags_map : {
    key   = k
    value = v
  }]
}

resource "aws_autoscaling_group" "example" {
  # ...

  dynamic "tag" {
    for_each = local.tags_list
    content {
      key                 = tag.value.key
      value               = tag.value.value
      propagate_at_launch = true
    }
  }
}
```

## Count and For Each

### Count vs For Each

**Count** - Use for creating multiple similar resources with numeric indexing:

```hcl
variable "subnet_count" {
  default = 3
}

resource "aws_subnet" "public" {
  count             = var.subnet_count
  vpc_id            = aws_vpc.main.id
  cidr_block        = cidrsubnet(aws_vpc.main.cidr_block, 8, count.index)
  availability_zone = data.aws_availability_zones.available.names[count.index]

  tags = {
    Name = "public-subnet-${count.index + 1}"
  }
}

# Reference: aws_subnet.public[0].id
```

**For Each** - Use for creating resources from a set or map (more flexible):

```hcl
variable "subnet_configs" {
  type = map(object({
    cidr_block = string
    az         = string
    public     = bool
  }))

  default = {
    "public-1" = {
      cidr_block = "10.0.1.0/24"
      az         = "us-east-1a"
      public     = true
    }
    "public-2" = {
      cidr_block = "10.0.2.0/24"
      az         = "us-east-1b"
      public     = true
    }
    "private-1" = {
      cidr_block = "10.0.3.0/24"
      az         = "us-east-1a"
      public     = false
    }
  }
}

resource "aws_subnet" "this" {
  for_each = var.subnet_configs

  vpc_id                  = aws_vpc.main.id
  cidr_block              = each.value.cidr_block
  availability_zone       = each.value.az
  map_public_ip_on_launch = each.value.public

  tags = {
    Name = each.key
    Type = each.value.public ? "Public" : "Private"
  }
}

# Reference: aws_subnet.this["public-1"].id
```

### For Each with Set

```hcl
variable "users" {
  type    = set(string)
  default = ["alice", "bob", "charlie"]
}

resource "aws_iam_user" "users" {
  for_each = var.users

  name = each.value

  tags = {
    Name = each.value
  }
}

# Create access keys for each user
resource "aws_iam_access_key" "keys" {
  for_each = aws_iam_user.users

  user = each.value.name
}
```

### Converting Count to For Each

```hcl
# Old approach with count (less flexible)
resource "aws_instance" "web" {
  count = 3
  # ...
}

# New approach with for_each (more flexible)
locals {
  instances = {
    "web-1" = { type = "t2.micro" }
    "web-2" = { type = "t2.small" }
    "web-3" = { type = "t2.micro" }
  }
}

resource "aws_instance" "web" {
  for_each = local.instances

  instance_type = each.value.type
  # ...

  tags = {
    Name = each.key
  }
}
```

## Terraform Functions

### String Functions

```hcl
locals {
  # String manipulation
  upper_name     = upper("hello")              # "HELLO"
  lower_name     = lower("HELLO")              # "hello"
  title_name     = title("hello world")        # "Hello World"
  trimmed        = trim("  hello  ", " ")      # "hello"
  replaced       = replace("hello", "l", "L")  # "heLLo"

  # String interpolation
  greeting       = format("Hello, %s!", "World")
  padded         = format("%05d", 42)          # "00042"

  # Splitting and joining
  parts          = split(",", "a,b,c")         # ["a", "b", "c"]
  joined         = join("-", ["a", "b", "c"])  # "a-b-c"

  # Regex
  regex_result   = regex("^([a-z]+)-([0-9]+)$", "app-123")  # ["app-123", "app", "123"]

  # Substring
  substring_val  = substr("hello world", 0, 5) # "hello"
}
```

### Collection Functions

```hcl
locals {
  # List operations
  numbers        = [1, 2, 3, 4, 5]
  first_item     = element(local.numbers, 0)   # 1
  contains_3     = contains(local.numbers, 3)  # true
  length_list    = length(local.numbers)       # 5

  # Merging
  map1           = { a = 1, b = 2 }
  map2           = { b = 3, c = 4 }
  merged         = merge(local.map1, local.map2)  # { a = 1, b = 3, c = 4 }

  # List manipulation
  list1          = [1, 2, 3]
  list2          = [4, 5, 6]
  concatenated   = concat(local.list1, local.list2)  # [1, 2, 3, 4, 5, 6]
  flattened      = flatten([[1, 2], [3, 4]])          # [1, 2, 3, 4]
  distinct       = distinct([1, 2, 2, 3, 3])          # [1, 2, 3]

  # Sorting
  sorted         = sort(["c", "a", "b"])       # ["a", "b", "c"]
  reverse        = reverse([1, 2, 3])          # [3, 2, 1]

  # Lookup
  lookup_val     = lookup(local.map1, "a", "default")  # 1
}
```

### For Expressions

```hcl
locals {
  # Transform list
  numbers = [1, 2, 3, 4, 5]
  doubled = [for n in local.numbers : n * 2]   # [2, 4, 6, 8, 10]

  # Filter list
  evens   = [for n in local.numbers : n if n % 2 == 0]  # [2, 4]

  # Transform map to list
  users = {
    alice = { age = 30 }
    bob   = { age = 25 }
  }
  user_ages = [for name, user in local.users : user.age]  # [30, 25]

  # Transform map to map
  upper_users = {
    for name, user in local.users :
    upper(name) => user
  }  # { ALICE = { age = 30 }, BOB = { age = 25 } }

  # Create map from list
  instances = ["web-1", "web-2", "web-3"]
  instance_map = {
    for name in local.instances :
    name => { type = "t2.micro" }
  }

  # Conditional transformation
  instance_configs = {
    for name, config in local.instance_map :
    name => merge(config, {
      monitoring = name == "web-1" ? true : false
    })
  }
}
```

### Network Functions

```hcl
locals {
  vpc_cidr = "10.0.0.0/16"

  # Create subnet CIDRs
  subnet_cidrs = [
    cidrsubnet(local.vpc_cidr, 8, 0),  # 10.0.0.0/24
    cidrsubnet(local.vpc_cidr, 8, 1),  # 10.0.1.0/24
    cidrsubnet(local.vpc_cidr, 8, 2),  # 10.0.2.0/24
  ]

  # Get specific host
  first_host = cidrhost(local.vpc_cidr, 5)  # 10.0.0.5

  # Get netmask
  netmask    = cidrnetmask("10.0.1.0/24")   # "255.255.255.0"
}
```

### Type Conversion Functions

```hcl
locals {
  # Type conversions
  string_num  = tostring(123)           # "123"
  num_string  = tonumber("123")         # 123
  bool_val    = tobool("true")          # true

  # Complex conversions
  list_val    = tolist(["a", "b"])
  set_val     = toset(["a", "b", "b"])  # ["a", "b"]
  map_val     = tomap({ a = 1 })

  # Type checking
  is_string   = can(tostring(var.value))
  is_number   = can(tonumber(var.value))
}
```

### Encoding Functions

```hcl
locals {
  # JSON encoding
  config = {
    name = "app"
    port = 8080
  }
  json_config = jsonencode(local.config)

  # Base64 encoding
  encoded = base64encode("hello world")
  decoded = base64decode(local.encoded)

  # URL encoding
  url_encoded = urlencode("hello world")  # "hello+world"
}
```

### File Functions

```hcl
locals {
  # Read file
  user_data     = file("${path.module}/user-data.sh")

  # Template file
  config_file   = templatefile("${path.module}/config.tpl", {
    port = 8080
    host = "localhost"
  })

  # Base64 encode file
  encoded_file  = filebase64("${path.module}/binary-file")

  # Check file existence
  file_exists   = fileexists("${path.module}/optional-file.txt")

  # File hash
  file_md5      = filemd5("${path.module}/file.txt")
  file_sha256   = filesha256("${path.module}/file.txt")
}
```

### Crypto Functions

```hcl
locals {
  # Generate hashes
  md5_hash    = md5("hello world")
  sha256_hash = sha256("hello world")

  # Generate UUID
  random_uuid = uuid()

  # Generate RSA key pair
  private_key = tls_private_key.example.private_key_pem
}

resource "tls_private_key" "example" {
  algorithm = "RSA"
  rsa_bits  = 4096
}
```

## Conditional Expressions

```hcl
# Ternary operator
variable "environment" {
  default = "dev"
}

locals {
  instance_type = var.environment == "prod" ? "t3.large" : "t2.micro"
  instance_count = var.environment == "prod" ? 5 : 1
  enable_backup = var.environment == "prod" ? true : false
}

# Conditional resource creation
resource "aws_instance" "web" {
  count = var.create_instance ? 1 : 0
  # ...
}

# Complex conditions
locals {
  is_production = var.environment == "prod"
  is_staging    = var.environment == "staging"
  is_high_env   = local.is_production || local.is_staging

  instance_type = (
    local.is_production ? "t3.large" :
    local.is_staging ? "t3.medium" :
    "t2.micro"
  )
}

# Conditional values in resources
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = local.instance_type

  monitoring = local.is_production

  root_block_device {
    volume_size = local.is_production ? 100 : 20
    encrypted   = local.is_production ? true : false
  }

  tags = merge(
    var.common_tags,
    local.is_production ? { Backup = "required" } : {}
  )
}
```

## Workspaces

Workspaces allow you to manage multiple environments with the same configuration.

### Basic Workspace Commands

```bash
# List workspaces
terraform workspace list

# Create new workspace
terraform workspace new dev
terraform workspace new staging
terraform workspace new prod

# Switch workspace
terraform workspace select dev

# Show current workspace
terraform workspace show

# Delete workspace
terraform workspace delete dev
```

### Using Workspaces in Configuration

```hcl
# Workspace-specific configuration
locals {
  environment = terraform.workspace

  # Configuration per workspace
  config = {
    dev = {
      instance_type  = "t2.micro"
      instance_count = 1
      db_instance    = "db.t3.micro"
    }
    staging = {
      instance_type  = "t3.small"
      instance_count = 2
      db_instance    = "db.t3.small"
    }
    prod = {
      instance_type  = "t3.large"
      instance_count = 5
      db_instance    = "db.t3.large"
    }
  }

  current_config = local.config[local.environment]
}

resource "aws_instance" "web" {
  count         = local.current_config.instance_count
  instance_type = local.current_config.instance_type

  tags = {
    Name        = "web-${terraform.workspace}-${count.index + 1}"
    Environment = terraform.workspace
  }
}

# Workspace-specific S3 backend
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "terraform.tfstate"
    region = "us-east-1"

    # Each workspace gets its own state file
    workspace_key_prefix = "workspaces"
  }
}
```

## Provider Configuration

### Multiple Provider Configurations

```hcl
# Default provider
provider "aws" {
  region = "us-east-1"
}

# Additional provider for different region
provider "aws" {
  alias  = "west"
  region = "us-west-2"
}

# Use specific provider
resource "aws_instance" "east" {
  provider = aws  # Default provider
  # ...
}

resource "aws_instance" "west" {
  provider = aws.west  # Aliased provider
  # ...
}

# Module with specific provider
module "vpc_west" {
  source = "./modules/vpc"

  providers = {
    aws = aws.west
  }
}
```

### Multi-Region Setup

```hcl
provider "aws" {
  alias  = "us-east-1"
  region = "us-east-1"
}

provider "aws" {
  alias  = "us-west-2"
  region = "us-west-2"
}

provider "aws" {
  alias  = "eu-west-1"
  region = "eu-west-1"
}

# Deploy VPC in each region
resource "aws_vpc" "east" {
  provider   = aws.us-east-1
  cidr_block = "10.0.0.0/16"

  tags = {
    Name = "vpc-us-east-1"
  }
}

resource "aws_vpc" "west" {
  provider   = aws.us-west-2
  cidr_block = "10.1.0.0/16"

  tags = {
    Name = "vpc-us-west-2"
  }
}

resource "aws_vpc" "eu" {
  provider   = aws.eu-west-1
  cidr_block = "10.2.0.0/16"

  tags = {
    Name = "vpc-eu-west-1"
  }
}
```

### Provider with Assume Role

```hcl
provider "aws" {
  region = "us-east-1"

  assume_role {
    role_arn     = "arn:aws:iam::123456789012:role/TerraformRole"
    session_name = "terraform-session"
  }

  default_tags {
    tags = {
      ManagedBy = "Terraform"
      Project   = "Infrastructure"
    }
  }
}
```

## Import Existing Resources

Import existing AWS resources into Terraform management.

### Import Process

```bash
# 1. Write resource configuration
# main.tf
resource "aws_instance" "imported" {
  # Configuration must match existing resource
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}

# 2. Import the resource
terraform import aws_instance.imported i-1234567890abcdef0

# 3. Run plan to verify
terraform plan

# 4. Update configuration to match actual state
# Make any necessary adjustments based on plan output
```

### Import Examples

```bash
# Import VPC
terraform import aws_vpc.main vpc-0123456789abcdef

# Import Subnet
terraform import aws_subnet.public subnet-0123456789abcdef

# Import Security Group
terraform import aws_security_group.web sg-0123456789abcdef

# Import S3 Bucket
terraform import aws_s3_bucket.data my-bucket-name

# Import RDS Instance
terraform import aws_db_instance.database mydb-instance

# Import IAM Role
terraform import aws_iam_role.role role-name
```

### Import Block (Terraform 1.5+)

```hcl
# New declarative import
import {
  to = aws_instance.example
  id = "i-1234567890abcdef0"
}

resource "aws_instance" "example" {
  # Configuration
}

# Then run:
# terraform plan -generate-config-out=generated.tf
```

## Security Best Practices

### 1. Sensitive Data Management

```hcl
# Mark outputs as sensitive
output "database_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}

# Mark variables as sensitive
variable "db_password" {
  type      = string
  sensitive = true
}

# Use AWS Secrets Manager
data "aws_secretsmanager_secret_version" "db_password" {
  secret_id = "prod/db/password"
}

resource "aws_db_instance" "main" {
  password = jsondecode(data.aws_secretsmanager_secret_version.db_password.secret_string)["password"]
}
```

### 2. State File Security

```hcl
# Encrypt state file
terraform {
  backend "s3" {
    bucket         = "terraform-state-bucket"
    key            = "prod/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    kms_key_id     = "arn:aws:kms:us-east-1:123456789012:key/12345678-1234-1234-1234-123456789012"
    dynamodb_table = "terraform-locks"
  }
}
```

### 3. IAM Least Privilege

```hcl
# Create specific IAM policy for Terraform
resource "aws_iam_policy" "terraform" {
  name        = "TerraformPolicy"
  description = "Policy for Terraform operations"

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect = "Allow"
        Action = [
          "ec2:*",
          "s3:*",
          "rds:*"
        ]
        Resource = "*"
        Condition = {
          StringEquals = {
            "aws:RequestedRegion" = "us-east-1"
          }
        }
      }
    ]
  })
}
```

### 4. Resource Tagging

```hcl
# Required tags
variable "required_tags" {
  type = object({
    Environment = string
    Owner       = string
    CostCenter  = string
    Project     = string
  })
}

# Apply tags consistently
resource "aws_instance" "web" {
  # ...

  tags = merge(
    var.required_tags,
    {
      Name = "web-server"
      Type = "application"
    }
  )
}
```

### 5. Prevent Accidental Deletion

```hcl
resource "aws_db_instance" "production" {
  # ...

  deletion_protection = true

  lifecycle {
    prevent_destroy = true
  }
}

resource "aws_s3_bucket" "critical_data" {
  # ...

  lifecycle {
    prevent_destroy = true
  }
}
```

## Next Steps

- [Chapter 4: Use Cases & Patterns](../04-use-cases/README.md)
- [Advanced Labs](../05-labs/advanced/)
