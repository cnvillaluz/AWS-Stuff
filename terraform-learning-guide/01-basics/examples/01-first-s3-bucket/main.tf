# Example 1: Your First S3 Bucket
# This is the simplest possible Terraform configuration for AWS

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
# IMPORTANT: Change the bucket name to something unique (S3 buckets are globally unique)
resource "aws_s3_bucket" "my_first_bucket" {
  bucket = "terraform-learning-bucket-${random_id.bucket_suffix.hex}"

  tags = {
    Name        = "My First Terraform Bucket"
    Environment = "Learning"
    ManagedBy   = "Terraform"
    Purpose     = "Learning Terraform Basics"
  }
}

# Generate a random suffix for unique bucket name
resource "random_id" "bucket_suffix" {
  byte_length = 4
}

# Output the bucket information
output "bucket_name" {
  value       = aws_s3_bucket.my_first_bucket.id
  description = "The name of the S3 bucket"
}

output "bucket_arn" {
  value       = aws_s3_bucket.my_first_bucket.arn
  description = "The ARN of the S3 bucket"
}

output "bucket_region" {
  value       = aws_s3_bucket.my_first_bucket.region
  description = "The region where the bucket is created"
}
