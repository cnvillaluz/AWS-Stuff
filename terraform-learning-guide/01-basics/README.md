# Chapter 1: Terraform Basics

Learn the fundamentals of Terraform and create your first AWS resources.

## Topics Covered

1. [What is Terraform?](#what-is-terraform)
2. [Core Concepts](#core-concepts)
3. [HCL Syntax Basics](#hcl-syntax-basics)
4. [Terraform Workflow](#terraform-workflow)
5. [Your First AWS Resource](#your-first-aws-resource)

## What is Terraform?

Terraform is an **Infrastructure as Code (IaC)** tool that lets you define and provision infrastructure using a declarative configuration language.

### Why Terraform?

- **Declarative**: Describe what you want, not how to create it
- **Cloud Agnostic**: Works with AWS, Azure, GCP, and 1000+ providers
- **Version Control**: Track infrastructure changes like application code
- **Reproducible**: Create identical environments every time
- **Plan Before Apply**: Preview changes before making them

### Infrastructure as Code Benefits

- **Automation**: Eliminate manual processes
- **Consistency**: No configuration drift
- **Collaboration**: Team-based infrastructure management
- **Documentation**: Code serves as living documentation
- **Disaster Recovery**: Rebuild infrastructure quickly

## Core Concepts

### Providers

Providers are plugins that interact with APIs of cloud platforms and services.

```hcl
# AWS Provider
provider "aws" {
  region = "us-east-1"
}
```

### Resources

Resources are the most important element - they represent infrastructure objects.

```hcl
# An AWS EC2 instance
resource "aws_instance" "web" {
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"
}
```

### State

Terraform tracks your infrastructure in a **state file** (`terraform.tfstate`). This maps your configuration to real-world resources.

### Execution Plan

Before making changes, Terraform generates a plan showing what will be created, modified, or destroyed.

## HCL Syntax Basics

HashiCorp Configuration Language (HCL) is designed to be human-readable and writable.

### Basic Structure

```hcl
# Block type, block label, block label
resource "aws_instance" "example" {
  # Argument = value
  ami           = "ami-0c55b159cbfafe1f0"
  instance_type = "t2.micro"

  # Nested block
  tags = {
    Name = "example-instance"
  }
}
```

### Key Elements

1. **Blocks**: Containers for configuration
2. **Arguments**: Assign values to names
3. **Expressions**: Represent values
4. **Comments**: `#` or `//` for single line, `/* */` for multi-line

### Data Types

```hcl
# String
variable "instance_name" {
  type    = string
  default = "my-instance"
}

# Number
variable "instance_count" {
  type    = number
  default = 2
}

# Boolean
variable "enable_monitoring" {
  type    = bool
  default = true
}

# List
variable "availability_zones" {
  type    = list(string)
  default = ["us-east-1a", "us-east-1b"]
}

# Map
variable "instance_tags" {
  type = map(string)
  default = {
    Environment = "dev"
    Project     = "learning"
  }
}
```

## Terraform Workflow

The basic Terraform workflow consists of four main commands:

### 1. terraform init

Initializes a working directory and downloads providers.

```bash
terraform init
```

This command:
- Downloads provider plugins
- Initializes backend for state storage
- Sets up the working directory

### 2. terraform plan

Creates an execution plan showing what Terraform will do.

```bash
terraform plan
```

Output indicators:
- `+` Resource will be created
- `-` Resource will be destroyed
- `~` Resource will be modified in-place
- `-/+` Resource will be destroyed and recreated

### 3. terraform apply

Applies the changes to reach the desired state.

```bash
terraform apply
```

Terraform will:
- Show the plan
- Ask for confirmation
- Execute the changes
- Update the state file

Use `-auto-approve` to skip confirmation (not recommended for production).

### 4. terraform destroy

Destroys all resources managed by the configuration.

```bash
terraform destroy
```

**Important**: Always destroy resources after practice to avoid charges!

### Additional Useful Commands

```bash
# Format your code to canonical style
terraform fmt

# Validate configuration syntax
terraform validate

# Show current state
terraform show

# List resources in state
terraform state list

# Display outputs
terraform output
```

## Your First AWS Resource

Let's create an S3 bucket - one of the simplest AWS resources.

### Example 1: Simple S3 Bucket

Create a file named `main.tf`:

```hcl
# Configure the AWS Provider
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  required_version = ">= 1.0"
}

provider "aws" {
  region = "us-east-1"
}

# Create an S3 bucket
resource "aws_s3_bucket" "my_first_bucket" {
  bucket = "my-terraform-learning-bucket-12345"  # Must be globally unique

  tags = {
    Name        = "My First Bucket"
    Environment = "Learning"
    ManagedBy   = "Terraform"
  }
}

# Output the bucket name
output "bucket_name" {
  value       = aws_s3_bucket.my_first_bucket.id
  description = "The name of the S3 bucket"
}

output "bucket_arn" {
  value       = aws_s3_bucket.my_first_bucket.arn
  description = "The ARN of the S3 bucket"
}
```

### Running Your First Configuration

```bash
# Navigate to your directory
cd 01-basics/examples/first-resource

# Initialize Terraform
terraform init

# Validate the configuration
terraform validate

# Format the code
terraform fmt

# Preview the changes
terraform plan

# Apply the configuration
terraform apply

# View the outputs
terraform output

# Destroy the resources when done
terraform destroy
```

### Example 2: EC2 Instance

Create a simple EC2 instance:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Get the latest Amazon Linux 2 AMI
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Create an EC2 instance
resource "aws_instance" "web_server" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"

  tags = {
    Name = "MyFirstEC2Instance"
  }
}

output "instance_id" {
  value = aws_instance.web_server.id
}

output "instance_public_ip" {
  value = aws_instance.web_server.public_ip
}
```

### Example 3: Multiple Resources with Dependencies

Create an S3 bucket with versioning and encryption:

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "us-east-1"
}

# Create S3 bucket
resource "aws_s3_bucket" "data_bucket" {
  bucket = "my-data-bucket-with-versioning-12345"

  tags = {
    Name        = "Data Bucket"
    Environment = "Learning"
  }
}

# Enable versioning
resource "aws_s3_bucket_versioning" "data_bucket_versioning" {
  bucket = aws_s3_bucket.data_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Enable server-side encryption
resource "aws_s3_bucket_server_side_encryption_configuration" "data_bucket_encryption" {
  bucket = aws_s3_bucket.data_bucket.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

# Block public access
resource "aws_s3_bucket_public_access_block" "data_bucket_pab" {
  bucket = aws_s3_bucket.data_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

output "bucket_id" {
  value = aws_s3_bucket.data_bucket.id
}

output "bucket_versioning_status" {
  value = aws_s3_bucket_versioning.data_bucket_versioning.versioning_configuration[0].status
}
```

## Understanding Resource Addressing

Resources are addressed using the format: `resource_type.resource_name`

```hcl
# Reference format
aws_s3_bucket.my_bucket.id
aws_instance.web_server.public_ip

# In this example:
resource "aws_instance" "web" {
  ami = data.aws_ami.latest.id  # Reference a data source
}

resource "aws_eip" "web_ip" {
  instance = aws_instance.web.id  # Reference another resource
}
```

## Best Practices for Beginners

1. **Use Version Control**: Always commit your `.tf` files to Git
2. **Never Commit State Files**: Add `*.tfstate*` to `.gitignore`
3. **Use Meaningful Names**: Make resource names descriptive
4. **Add Tags**: Always tag AWS resources for organization
5. **Test with Plan**: Always run `plan` before `apply`
6. **Destroy After Learning**: Clean up resources to avoid charges
7. **Keep It Simple**: Start with simple configurations
8. **Read Error Messages**: Terraform errors are usually informative

## Common Beginner Mistakes

1. **Forgetting to Run Init**: Always run `terraform init` first
2. **Not Using Unique Names**: S3 buckets need globally unique names
3. **Hardcoding Regions**: Use variables for flexibility
4. **Ignoring State Files**: State files contain sensitive information
5. **Not Destroying Resources**: Forgetting cleanup leads to unexpected charges

## Quick Reference

### Essential Commands
```bash
terraform init      # Initialize directory
terraform plan      # Preview changes
terraform apply     # Apply changes
terraform destroy   # Destroy resources
terraform fmt       # Format code
terraform validate  # Validate syntax
terraform show      # Show current state
```

### File Structure
```
project/
├── main.tf           # Primary configuration
├── variables.tf      # Input variables
├── outputs.tf        # Output values
├── terraform.tfstate # State file (don't commit!)
└── .terraform/       # Provider plugins (don't commit!)
```

## Next Steps

Now that you understand the basics, proceed to:

- [Chapter 2: Intermediate Concepts](../02-intermediate/README.md) - Variables, modules, and state management
- [Hands-on Lab 1](../05-labs/beginner/lab1-first-resource.md) - Practice creating your first resources

## Additional Resources

- [Terraform AWS Provider Documentation](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [HCL Syntax Reference](https://www.terraform.io/docs/language/syntax/configuration.html)
- [AWS Free Tier](https://aws.amazon.com/free/)

---

**Practice Time!** Try creating different AWS resources like VPCs, Security Groups, or IAM roles to reinforce your learning.
