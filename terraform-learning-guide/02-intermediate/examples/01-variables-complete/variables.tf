# String Variables
variable "aws_region" {
  description = "AWS region where resources will be created"
  type        = string
  default     = "us-east-1"
}

variable "project_name" {
  description = "Name of the project (used for resource naming)"
  type        = string

  validation {
    condition     = length(var.project_name) > 0 && length(var.project_name) <= 20
    error_message = "Project name must be between 1 and 20 characters."
  }
}

variable "environment" {
  description = "Environment name (dev, staging, prod)"
  type        = string

  validation {
    condition     = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

# Network Variables
variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"

  validation {
    condition     = can(cidrhost(var.vpc_cidr, 0))
    error_message = "VPC CIDR must be a valid IPv4 CIDR block."
  }
}

variable "public_subnet_cidrs" {
  description = "CIDR blocks for public subnets"
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24"]

  validation {
    condition     = length(var.public_subnet_cidrs) >= 1
    error_message = "At least one public subnet CIDR must be provided."
  }
}

variable "availability_zones" {
  description = "Availability zones for subnets"
  type        = list(string)
  default     = ["us-east-1a", "us-east-1b"]
}

# Number Variables
variable "instance_count" {
  description = "Number of EC2 instances to create"
  type        = number
  default     = 2

  validation {
    condition     = var.instance_count >= 1 && var.instance_count <= 10
    error_message = "Instance count must be between 1 and 10."
  }
}

# Boolean Variables
variable "create_instances" {
  description = "Whether to create EC2 instances"
  type        = bool
  default     = true
}

variable "create_s3_bucket" {
  description = "Whether to create S3 bucket"
  type        = bool
  default     = true
}

# List Variables
variable "allowed_ports" {
  description = "List of ports to allow in security group"
  type        = list(number)
  default     = [80, 443]
}

# Map Variables
variable "common_tags" {
  description = "Common tags to apply to all resources"
  type        = map(string)
  default = {
    ManagedBy = "Terraform"
    Project   = "Learning"
  }
}

# Object Variable (Complex Type)
variable "instance_config" {
  description = "Configuration for EC2 instances"
  type = object({
    type              = string
    volume_size       = number
    enable_monitoring = bool
  })

  default = {
    type              = "t2.micro"
    volume_size       = 20
    enable_monitoring = false
  }

  validation {
    condition     = contains(["t2.micro", "t2.small", "t2.medium", "t3.micro", "t3.small"], var.instance_config.type)
    error_message = "Instance type must be a valid t2 or t3 type."
  }

  validation {
    condition     = var.instance_config.volume_size >= 8 && var.instance_config.volume_size <= 100
    error_message = "Volume size must be between 8 and 100 GB."
  }
}

# Sensitive Variable (for demonstration)
variable "database_password" {
  description = "Password for database"
  type        = string
  sensitive   = true
  default     = ""

  validation {
    condition     = length(var.database_password) == 0 || length(var.database_password) >= 8
    error_message = "Database password must be at least 8 characters if provided."
  }
}
