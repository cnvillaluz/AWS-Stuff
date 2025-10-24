# Example 2: Your First EC2 Instance
# This example shows how to create an EC2 instance with data sources

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

# Data source to get the latest Amazon Linux 2 AMI
data "aws_ami" "amazon_linux_2" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
}

# Get the default VPC (every AWS account has one)
data "aws_vpc" "default" {
  default = true
}

# Create a security group allowing SSH access
resource "aws_security_group" "allow_ssh" {
  name        = "allow_ssh_terraform_learning"
  description = "Allow SSH inbound traffic for learning purposes"
  vpc_id      = data.aws_vpc.default.id

  ingress {
    description = "SSH from anywhere (not recommended for production)"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound traffic"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "allow_ssh"
  }
}

# Create an EC2 instance
resource "aws_instance" "web_server" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"  # Free tier eligible

  vpc_security_group_ids = [aws_security_group.allow_ssh.id]

  tags = {
    Name        = "MyFirstEC2Instance"
    Environment = "Learning"
    ManagedBy   = "Terraform"
  }

  # User data script to install and start a simple web server
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<h1>Hello from Terraform!</h1>" > /var/www/html/index.html
              EOF
}

# Outputs
output "instance_id" {
  value       = aws_instance.web_server.id
  description = "The ID of the EC2 instance"
}

output "instance_public_ip" {
  value       = aws_instance.web_server.public_ip
  description = "The public IP address of the instance"
}

output "instance_public_dns" {
  value       = aws_instance.web_server.public_dns
  description = "The public DNS name of the instance"
}

output "ami_id" {
  value       = data.aws_ami.amazon_linux_2.id
  description = "The AMI ID used for the instance"
}

output "security_group_id" {
  value       = aws_security_group.allow_ssh.id
  description = "The ID of the security group"
}
