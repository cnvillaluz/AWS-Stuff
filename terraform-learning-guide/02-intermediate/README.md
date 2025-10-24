# Chapter 2: Intermediate Terraform Concepts

Build on your foundational knowledge with variables, modules, and state management.

## Topics Covered

1. [Input Variables](#input-variables)
2. [Output Values](#output-values)
3. [Data Sources](#data-sources)
4. [Modules](#modules)
5. [State Management](#state-management)
6. [Resource Dependencies](#resource-dependencies)
7. [Lifecycle Rules](#lifecycle-rules)

## Input Variables

Variables make your Terraform configurations flexible and reusable.

### Defining Variables

```hcl
# variables.tf
variable "region" {
  description = "AWS region for resources"
  type        = string
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}

variable "environment" {
  description = "Environment name"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "instance_count" {
  description = "Number of instances to create"
  type        = number
  default     = 1

  validation {
    condition     = var.instance_count > 0 && var.instance_count <= 10
    error_message = "Instance count must be between 1 and 10."
  }
}

variable "enable_monitoring" {
  description = "Enable detailed monitoring"
  type        = bool
  default     = false
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

variable "tags" {
  description = "Common tags for all resources"
  type        = map(string)
  default = {
    ManagedBy = "Terraform"
    Project   = "Learning"
  }
}
```

### Using Variables

```hcl
# main.tf
provider "aws" {
  region = var.region
}

resource "aws_instance" "app" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type
  count         = var.instance_count

  monitoring = var.enable_monitoring

  tags = merge(
    var.tags,
    {
      Name        = "app-server-${count.index + 1}"
      Environment = var.environment
    }
  )
}
```

### Providing Variable Values

**1. Command Line:**
```bash
terraform apply -var="environment=prod" -var="instance_count=3"
```

**2. Variable Files (terraform.tfvars):**
```hcl
# terraform.tfvars
region         = "us-west-2"
environment    = "prod"
instance_count = 3
instance_type  = "t2.small"
enable_monitoring = true

tags = {
  ManagedBy = "Terraform"
  Project   = "MyApp"
  Team      = "DevOps"
}
```

**3. Environment-Specific Files:**
```hcl
# dev.tfvars
environment    = "dev"
instance_count = 1
instance_type  = "t2.micro"

# prod.tfvars
environment    = "prod"
instance_count = 5
instance_type  = "t2.large"
```

Apply with:
```bash
terraform apply -var-file="prod.tfvars"
```

**4. Environment Variables:**
```bash
export TF_VAR_region="us-west-2"
export TF_VAR_environment="prod"
terraform apply
```

### Variable Types

```hcl
# String
variable "name" {
  type = string
}

# Number
variable "count" {
  type = number
}

# Boolean
variable "enabled" {
  type = bool
}

# List
variable "subnets" {
  type = list(string)
}

# Map
variable "tags" {
  type = map(string)
}

# Object
variable "instance_config" {
  type = object({
    instance_type = string
    volume_size   = number
    monitoring    = bool
  })

  default = {
    instance_type = "t2.micro"
    volume_size   = 20
    monitoring    = false
  }
}

# Tuple
variable "ports" {
  type = tuple([number, string, bool])
}

# Set
variable "unique_values" {
  type = set(string)
}
```

## Output Values

Outputs expose information about your infrastructure.

```hcl
# outputs.tf
output "instance_ids" {
  description = "IDs of EC2 instances"
  value       = aws_instance.app[*].id
}

output "instance_public_ips" {
  description = "Public IP addresses"
  value       = aws_instance.app[*].public_ip
}

output "vpc_id" {
  description = "VPC ID"
  value       = aws_vpc.main.id
}

output "database_connection_string" {
  description = "Database connection string"
  value       = "postgres://${aws_db_instance.main.endpoint}"
  sensitive   = true  # Won't be displayed in console
}

output "complete_instance_info" {
  description = "Complete instance information"
  value = {
    for instance in aws_instance.app :
    instance.id => {
      public_ip  = instance.public_ip
      private_ip = instance.private_ip
      az         = instance.availability_zone
    }
  }
}
```

### Using Outputs

```bash
# View all outputs
terraform output

# View specific output
terraform output instance_ids

# Output as JSON
terraform output -json

# Use in shell scripts
INSTANCE_ID=$(terraform output -raw instance_ids)
```

## Data Sources

Data sources fetch information from existing resources.

### Common AWS Data Sources

```hcl
# Get latest AMI
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Get availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

# Get existing VPC
data "aws_vpc" "selected" {
  filter {
    name   = "tag:Name"
    values = ["production-vpc"]
  }
}

# Get existing subnet
data "aws_subnet" "selected" {
  vpc_id = data.aws_vpc.selected.id

  filter {
    name   = "tag:Type"
    values = ["public"]
  }
}

# Get current AWS account ID
data "aws_caller_identity" "current" {}

# Get current region
data "aws_region" "current" {}

# Get existing security group
data "aws_security_group" "web" {
  name = "web-sg"
}

# Use in resources
resource "aws_instance" "app" {
  ami               = data.aws_ami.amazon_linux_2.id
  availability_zone = data.aws_availability_zones.available.names[0]
  subnet_id         = data.aws_subnet.selected.id
}

output "account_id" {
  value = data.aws_caller_identity.current.account_id
}
```

## Modules

Modules are containers for multiple resources used together.

### Creating a Module

**Directory Structure:**
```
modules/
└── web-server/
    ├── main.tf
    ├── variables.tf
    ├── outputs.tf
    └── README.md
```

**modules/web-server/variables.tf:**
```hcl
variable "name" {
  description = "Name of the web server"
  type        = string
}

variable "instance_type" {
  description = "Instance type"
  type        = string
  default     = "t2.micro"
}

variable "subnet_id" {
  description = "Subnet ID for the instance"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "tags" {
  description = "Tags to apply"
  type        = map(string)
  default     = {}
}
```

**modules/web-server/main.tf:**
```hcl
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_security_group" "web" {
  name        = "${var.name}-sg"
  description = "Security group for ${var.name}"
  vpc_id      = var.vpc_id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = merge(
    var.tags,
    {
      Name = "${var.name}-sg"
    }
  )
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = var.instance_type
  subnet_id     = var.subnet_id

  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<h1>Hello from ${var.name}</h1>" > /var/www/html/index.html
              EOF

  tags = merge(
    var.tags,
    {
      Name = var.name
    }
  )
}
```

**modules/web-server/outputs.tf:**
```hcl
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web.id
}

output "public_ip" {
  description = "Public IP address"
  value       = aws_instance.web.public_ip
}

output "security_group_id" {
  description = "Security group ID"
  value       = aws_security_group.web.id
}
```

### Using a Module

**main.tf:**
```hcl
module "web_server_1" {
  source = "./modules/web-server"

  name          = "web-server-1"
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public.id
  vpc_id        = aws_vpc.main.id

  tags = {
    Environment = "dev"
    Team        = "platform"
  }
}

module "web_server_2" {
  source = "./modules/web-server"

  name          = "web-server-2"
  instance_type = "t2.small"
  subnet_id     = aws_subnet.public.id
  vpc_id        = aws_vpc.main.id

  tags = {
    Environment = "prod"
    Team        = "platform"
  }
}

output "web_server_1_ip" {
  value = module.web_server_1.public_ip
}

output "web_server_2_ip" {
  value = module.web_server_2.public_ip
}
```

### Remote Modules

```hcl
# From Terraform Registry
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "5.0.0"

  name = "my-vpc"
  cidr = "10.0.0.0/16"

  azs             = ["us-east-1a", "us-east-1b", "us-east-1c"]
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]

  enable_nat_gateway = true
  enable_vpn_gateway = false

  tags = {
    Environment = "dev"
  }
}

# From Git repository
module "custom" {
  source = "git::https://github.com/user/terraform-modules.git//web-server?ref=v1.0.0"
}
```

## State Management

Terraform state tracks resources and their relationships.

### Local State (Default)

```
project/
├── main.tf
├── terraform.tfstate       # Current state
└── terraform.tfstate.backup # Previous state
```

**⚠️ Local State Issues:**
- Not suitable for teams
- No locking mechanism
- Risk of losing state file
- Contains sensitive data

### Remote State with S3

**backend.tf:**
```hcl
terraform {
  backend "s3" {
    bucket         = "my-terraform-state-bucket"
    key            = "project/terraform.tfstate"
    region         = "us-east-1"
    encrypt        = true
    dynamodb_table = "terraform-state-lock"
  }
}
```

**Creating the Backend Infrastructure:**

```hcl
# backend-setup.tf (run this first, then migrate to remote backend)
resource "aws_s3_bucket" "terraform_state" {
  bucket = "my-terraform-state-bucket-${data.aws_caller_identity.current.account_id}"

  lifecycle {
    prevent_destroy = true
  }

  tags = {
    Name = "Terraform State Bucket"
  }
}

resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_dynamodb_table" "terraform_lock" {
  name         = "terraform-state-lock"
  billing_mode = "PAY_PER_REQUEST"
  hash_key     = "LockID"

  attribute {
    name = "LockID"
    type = "S"
  }

  tags = {
    Name = "Terraform State Lock Table"
  }
}

data "aws_caller_identity" "current" {}
```

**Migrating to Remote State:**

```bash
# 1. Create S3 bucket and DynamoDB table
terraform apply

# 2. Add backend configuration to main configuration

# 3. Initialize with backend
terraform init -migrate-state

# 4. Verify state is in S3
aws s3 ls s3://my-terraform-state-bucket/
```

### State Commands

```bash
# List resources in state
terraform state list

# Show resource details
terraform state show aws_instance.web

# Move resource in state
terraform state mv aws_instance.old aws_instance.new

# Remove resource from state (doesn't destroy resource)
terraform state rm aws_instance.web

# Pull remote state
terraform state pull

# Push local state to remote
terraform state push

# Replace provider in state
terraform state replace-provider hashicorp/aws registry.terraform.io/hashicorp/aws
```

## Resource Dependencies

### Implicit Dependencies

Terraform automatically creates dependencies from resource references:

```hcl
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_subnet" "public" {
  vpc_id = aws_vpc.main.id  # Implicit dependency on VPC
  cidr_block = "10.0.1.0/24"
}

resource "aws_instance" "web" {
  subnet_id = aws_subnet.public.id  # Implicit dependency on subnet
  # ...
}
```

### Explicit Dependencies

Use `depends_on` when Terraform can't detect the dependency:

```hcl
resource "aws_iam_role_policy" "example" {
  name = "example"
  role = aws_iam_role.example.id
  policy = jsonencode({
    # ...
  })
}

resource "aws_instance" "example" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  iam_instance_profile = aws_iam_instance_profile.example.name

  # Ensure policy is attached before launching instance
  depends_on = [aws_iam_role_policy.example]
}
```

## Lifecycle Rules

Control resource behavior with lifecycle meta-arguments:

```hcl
resource "aws_instance" "example" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"

  lifecycle {
    # Prevent destruction of this resource
    prevent_destroy = true
  }
}

resource "aws_db_instance" "example" {
  # ...

  lifecycle {
    # Create new resource before destroying old one
    create_before_destroy = true
  }
}

resource "aws_instance" "app" {
  ami           = var.ami_id
  instance_type = var.instance_type

  user_data = file("user_data.sh")

  lifecycle {
    # Ignore changes to specific attributes
    ignore_changes = [
      user_data,
      tags["LastUpdated"]
    ]
  }
}

resource "aws_autoscaling_group" "example" {
  # ...

  lifecycle {
    # Replace resource if this field changes
    replace_triggered_by = [
      aws_launch_template.example.id
    ]
  }
}
```

## Best Practices

1. **Organize Your Code:**
```
project/
├── main.tf           # Primary resources
├── variables.tf      # Input variables
├── outputs.tf        # Outputs
├── backend.tf        # Backend configuration
├── providers.tf      # Provider configuration
├── terraform.tfvars  # Variable values (don't commit if sensitive)
└── modules/          # Custom modules
```

2. **Use Remote State:**
- Always use remote state for team projects
- Enable versioning on state bucket
- Use state locking with DynamoDB

3. **Variable Best Practices:**
- Use validation rules
- Provide meaningful descriptions
- Set sensible defaults
- Use .tfvars files for environment-specific values

4. **Module Best Practices:**
- Keep modules focused and reusable
- Document inputs and outputs
- Version your modules
- Use semantic versioning

5. **Security:**
- Mark sensitive outputs
- Never commit state files
- Use AWS IAM roles when possible
- Encrypt remote state

## Next Steps

- [Chapter 3: Advanced Concepts](../03-advanced/README.md)
- [Lab 2: Building a Multi-Tier Application](../05-labs/intermediate/lab2-multi-tier.md)
