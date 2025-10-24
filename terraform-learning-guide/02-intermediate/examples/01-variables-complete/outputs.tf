# VPC Outputs
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "vpc_cidr" {
  description = "CIDR block of the VPC"
  value       = aws_vpc.main.cidr_block
}

# Subnet Outputs
output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}

output "public_subnet_cidrs" {
  description = "CIDR blocks of public subnets"
  value       = aws_subnet.public[*].cidr_block
}

# Security Group Outputs
output "web_security_group_id" {
  description = "ID of the web security group"
  value       = aws_security_group.web.id
}

# Instance Outputs (conditional - only if instances created)
output "instance_ids" {
  description = "IDs of EC2 instances"
  value       = var.create_instances ? aws_instance.web[*].id : []
}

output "instance_public_ips" {
  description = "Public IP addresses of instances"
  value       = var.create_instances ? aws_instance.web[*].public_ip : []
}

output "instance_private_ips" {
  description = "Private IP addresses of instances"
  value       = var.create_instances ? aws_instance.web[*].private_ip : []
}

# Complex output with map
output "instance_details" {
  description = "Detailed information about instances"
  value = var.create_instances ? {
    for idx, instance in aws_instance.web :
    instance.id => {
      public_ip  = instance.public_ip
      private_ip = instance.private_ip
      az         = instance.availability_zone
      subnet_id  = instance.subnet_id
    }
  } : {}
}

# S3 Bucket Output (conditional)
output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = var.create_s3_bucket ? aws_s3_bucket.app_bucket[0].id : null
}

output "s3_bucket_arn" {
  description = "ARN of the S3 bucket"
  value       = var.create_s3_bucket ? aws_s3_bucket.app_bucket[0].arn : null
}

# Environment Information
output "deployment_info" {
  description = "Information about the deployment"
  value = {
    project_name = var.project_name
    environment  = var.environment
    region       = var.aws_region
    instance_count = var.create_instances ? var.instance_count : 0
    created_at   = timestamp()
  }
}
