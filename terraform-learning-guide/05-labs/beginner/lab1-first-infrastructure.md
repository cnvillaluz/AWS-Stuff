# Lab 1: Your First Infrastructure

## Objective
Create your first AWS infrastructure using Terraform, understanding the complete workflow from initialization to destruction.

## What You'll Build
- A VPC with a public subnet
- An S3 bucket with versioning enabled
- An EC2 instance in the public subnet
- Security group allowing SSH access
- All resources properly tagged

## Prerequisites
- AWS account configured with AWS CLI (`aws configure`)
- Terraform installed (version >= 1.0)
- Basic understanding of AWS services (VPC, EC2, S3)
- SSH key pair in your AWS account (or you'll create one)

## Estimated Time
30-45 minutes

## Learning Outcomes
By completing this lab, you will:
- Understand the Terraform workflow (init, plan, apply, destroy)
- Create basic AWS resources
- Use data sources to query AWS
- Work with resource dependencies
- Use outputs to display information

## Step-by-Step Instructions

### Step 1: Set Up Your Project Directory

Create a new directory for this lab:

```bash
mkdir -p ~/terraform-labs/lab1-first-infrastructure
cd ~/terraform-labs/lab1-first-infrastructure
```

### Step 2: Create the Main Configuration

Create a file named `main.tf`:

```hcl
# main.tf

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

# Data source for latest Amazon Linux 2 AMI
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

# Create VPC
resource "aws_vpc" "lab_vpc" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name      = "lab1-vpc"
    Lab       = "lab1"
    ManagedBy = "Terraform"
  }
}

# Create Internet Gateway
resource "aws_internet_gateway" "lab_igw" {
  vpc_id = aws_vpc.lab_vpc.id

  tags = {
    Name      = "lab1-igw"
    Lab       = "lab1"
    ManagedBy = "Terraform"
  }
}

# Create Public Subnet
resource "aws_subnet" "public_subnet" {
  vpc_id                  = aws_vpc.lab_vpc.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name      = "lab1-public-subnet"
    Lab       = "lab1"
    Type      = "Public"
    ManagedBy = "Terraform"
  }
}

# Create Route Table
resource "aws_route_table" "public_rt" {
  vpc_id = aws_vpc.lab_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.lab_igw.id
  }

  tags = {
    Name      = "lab1-public-rt"
    Lab       = "lab1"
    ManagedBy = "Terraform"
  }
}

# Associate Route Table with Subnet
resource "aws_route_table_association" "public_association" {
  subnet_id      = aws_subnet.public_subnet.id
  route_table_id = aws_route_table.public_rt.id
}

# Create Security Group
resource "aws_security_group" "web_sg" {
  name        = "lab1-web-sg"
  description = "Security group for web server - allows SSH and HTTP"
  vpc_id      = aws_vpc.lab_vpc.id

  ingress {
    description = "SSH from anywhere"
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    description = "HTTP from anywhere"
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    description = "Allow all outbound"
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name      = "lab1-web-sg"
    Lab       = "lab1"
    ManagedBy = "Terraform"
  }
}

# Create S3 Bucket
resource "aws_s3_bucket" "lab_bucket" {
  bucket = "lab1-terraform-bucket-${data.aws_caller_identity.current.account_id}"

  tags = {
    Name      = "lab1-bucket"
    Lab       = "lab1"
    ManagedBy = "Terraform"
  }
}

# Enable versioning on S3 bucket
resource "aws_s3_bucket_versioning" "lab_bucket_versioning" {
  bucket = aws_s3_bucket.lab_bucket.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Block public access to S3 bucket
resource "aws_s3_bucket_public_access_block" "lab_bucket_pab" {
  bucket = aws_s3_bucket.lab_bucket.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Create EC2 Instance
resource "aws_instance" "web_server" {
  ami           = data.aws_ami.amazon_linux_2.id
  instance_type = "t2.micro"
  subnet_id     = aws_subnet.public_subnet.id

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<h1>Hello from Terraform Lab 1!</h1>" > /var/www/html/index.html
              echo "<p>Instance ID: $(ec2-metadata --instance-id | cut -d ' ' -f 2)</p>" >> /var/www/html/index.html
              EOF

  tags = {
    Name      = "lab1-web-server"
    Lab       = "lab1"
    ManagedBy = "Terraform"
  }
}

# Data source for current AWS account ID
data "aws_caller_identity" "current" {}
```

### Step 3: Create Outputs File

Create `outputs.tf`:

```hcl
# outputs.tf

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.lab_vpc.id
}

output "vpc_cidr" {
  description = "CIDR block of the VPC"
  value       = aws_vpc.lab_vpc.cidr_block
}

output "subnet_id" {
  description = "ID of the public subnet"
  value       = aws_subnet.public_subnet.id
}

output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web_server.id
}

output "instance_public_ip" {
  description = "Public IP address of the EC2 instance"
  value       = aws_instance.web_server.public_ip
}

output "instance_public_dns" {
  description = "Public DNS name of the EC2 instance"
  value       = aws_instance.web_server.public_dns
}

output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = aws_s3_bucket.lab_bucket.id
}

output "s3_bucket_arn" {
  description = "ARN of the S3 bucket"
  value       = aws_s3_bucket.lab_bucket.arn
}

output "web_url" {
  description = "URL to access the web server"
  value       = "http://${aws_instance.web_server.public_ip}"
}

output "ssh_command" {
  description = "SSH command to connect to the instance"
  value       = "ssh -i /path/to/your/key.pem ec2-user@${aws_instance.web_server.public_ip}"
}
```

### Step 4: Initialize Terraform

Initialize your Terraform working directory:

```bash
terraform init
```

**Expected Output:**
```
Initializing the backend...
Initializing provider plugins...
- Finding hashicorp/aws versions matching "~> 5.0"...
- Installing hashicorp/aws v5.x.x...
- Installed hashicorp/aws v5.x.x

Terraform has been successfully initialized!
```

**What happened?**
- Terraform downloaded the AWS provider plugin
- Created a `.terraform` directory to store provider plugins
- Created a `.terraform.lock.hcl` file to lock provider versions

### Step 5: Validate Configuration

Validate your Terraform configuration:

```bash
terraform validate
```

**Expected Output:**
```
Success! The configuration is valid.
```

### Step 6: Format Your Code

Format your Terraform files:

```bash
terraform fmt
```

This ensures consistent formatting across your configuration files.

### Step 7: Preview Changes

Generate and review an execution plan:

```bash
terraform plan
```

**What to look for:**
- **Green `+`**: Resources to be created
- **Red `-`**: Resources to be destroyed (none in this lab)
- **Yellow `~`**: Resources to be modified (none in this lab)

You should see approximately **11 resources** to be created:
1. VPC
2. Internet Gateway
3. Subnet
4. Route Table
5. Route Table Association
6. Security Group
7. S3 Bucket
8. S3 Bucket Versioning
9. S3 Bucket Public Access Block
10. EC2 Instance
11. Various data sources

### Step 8: Apply Configuration

Create the infrastructure:

```bash
terraform apply
```

Review the plan again, then type `yes` when prompted.

**This will take 2-3 minutes.** Terraform will create resources in the correct order based on dependencies.

**Expected Output:**
```
Apply complete! Resources: 11 added, 0 changed, 0 destroyed.

Outputs:

instance_id = "i-0123456789abcdef"
instance_public_ip = "3.45.67.89"
...
```

### Step 9: Verify Your Infrastructure

#### Check Terraform State

```bash
# List all resources in state
terraform state list

# Show details of a specific resource
terraform state show aws_instance.web_server
```

#### View Outputs

```bash
# View all outputs
terraform output

# View specific output
terraform output instance_public_ip

# Use -raw for script-friendly output
terraform output -raw instance_public_ip
```

#### Verify in AWS Console

1. Go to AWS Console → EC2 → Instances
2. Find your instance named "lab1-web-server"
3. Check S3 → Buckets for your bucket
4. Check VPC → Your VPCs for "lab1-vpc"

#### Test the Web Server

Get the public IP from outputs and test:

```bash
# Get the instance IP
INSTANCE_IP=$(terraform output -raw instance_public_ip)

# Wait a minute for the instance to fully boot, then test
curl http://$INSTANCE_IP

# Or open in browser
echo "http://$INSTANCE_IP"
```

You should see: "Hello from Terraform Lab 1!"

### Step 10: Make a Change

Let's modify the configuration to see how Terraform handles updates.

Edit `main.tf` and change the EC2 instance tags:

```hcl
resource "aws_instance" "web_server" {
  # ... existing configuration ...

  tags = {
    Name        = "lab1-web-server-updated"  # Changed
    Lab         = "lab1"
    ManagedBy   = "Terraform"
    Environment = "learning"  # Added
  }
}
```

Run plan to see the changes:

```bash
terraform plan
```

You should see:
```
~ update in-place

  ~ tags = {
      ~ "Name" = "lab1-web-server" -> "lab1-web-server-updated"
      + "Environment" = "learning"
    }
```

Apply the change:

```bash
terraform apply
```

Type `yes` to confirm.

### Step 11: Explore State File

**⚠️ Warning**: Never edit the state file manually!

View the state:

```bash
# Show current state
terraform show

# Show state in JSON format
terraform show -json | jq '.'
```

The state file contains:
- Current state of all resources
- Resource dependencies
- Provider configuration
- Output values

### Step 12: Clean Up

Destroy all resources:

```bash
terraform destroy
```

Review the plan showing what will be destroyed, then type `yes`.

**This is critical!** Always destroy lab resources to avoid unnecessary charges.

Verify destruction:

```bash
# Should show empty state
terraform state list

# Should show 0 resources
terraform show
```

## Validation Checklist

Before destroying, verify:

- [ ] VPC created with correct CIDR (10.0.0.0/16)
- [ ] Public subnet created with correct CIDR (10.0.1.0/24)
- [ ] Internet Gateway attached to VPC
- [ ] Route table has route to Internet Gateway
- [ ] Security group allows SSH (port 22) and HTTP (port 80)
- [ ] S3 bucket created with versioning enabled
- [ ] EC2 instance running and accessible
- [ ] Web server responding on HTTP
- [ ] All resources properly tagged
- [ ] Outputs display correct information
- [ ] `terraform plan` shows no changes after apply

## Troubleshooting

### Issue: "Error: creating EC2 Instance: InvalidKeyPair.NotFound"

**Problem**: No SSH key pair in your AWS account

**Solution**: Either:
1. Remove key_name from aws_instance (you won't be able to SSH)
2. Create a key pair in AWS Console and add to configuration:

```hcl
resource "aws_instance" "web_server" {
  key_name = "your-key-name"  # Add this line
  # ... rest of config
}
```

### Issue: "Error: creating S3 Bucket: BucketAlreadyExists"

**Problem**: S3 bucket names must be globally unique

**Solution**: The configuration uses your account ID to ensure uniqueness. If it still fails, add a random suffix:

```hcl
resource "random_id" "bucket_suffix" {
  byte_length = 4
}

resource "aws_s3_bucket" "lab_bucket" {
  bucket = "lab1-terraform-bucket-${data.aws_caller_identity.current.account_id}-${random_id.bucket_suffix.hex}"
}
```

### Issue: Web server not responding

**Problem**: Instance still booting or security group misconfigured

**Solution**:
1. Wait 2-3 minutes for user data script to complete
2. Check security group in AWS Console
3. Verify instance is running: `aws ec2 describe-instances --instance-ids $(terraform output -raw instance_id)`

### Issue: "Error acquiring the state lock"

**Problem**: Another Terraform process is running or was interrupted

**Solution**: Wait for the process to complete or force unlock (use carefully):

```bash
terraform force-unlock <LOCK_ID>
```

## Cost Estimate

Resources in this lab (as of 2024):
- **VPC**: Free
- **S3 Bucket**: Free (empty bucket)
- **EC2 t2.micro**: $0.0116/hour (~$0.28/day)
- **Data transfer**: Minimal

**Estimated cost if left running**: ~$8.40/month

**This is why you should always run `terraform destroy`!**

## Next Steps

Now that you've completed Lab 1:

1. **Review**: Look at each resource in the AWS Console
2. **Experiment**: Try adding more resources or changing configurations
3. **Understand Dependencies**: Notice the order Terraform created resources
4. **Read the Docs**: Look up each resource type in the Terraform AWS provider docs

**Next Lab**: [Lab 2: Working with Variables](./lab2-variables.md)

## Key Takeaways

You learned:
- ✅ The complete Terraform workflow (init, plan, apply, destroy)
- ✅ How to create basic AWS resources
- ✅ Resource dependencies and references
- ✅ Using data sources to query AWS
- ✅ Outputs to expose information
- ✅ The importance of proper resource tagging
- ✅ Always destroy resources after practice!

## Additional Challenges

If you want more practice:

1. **Add a second subnet** in a different availability zone
2. **Create an Elastic IP** and associate it with the instance
3. **Add more security group rules** (e.g., HTTPS on port 443)
4. **Upload a file to the S3 bucket** using Terraform
5. **Create an IAM role** for the EC2 instance

## References

- [Terraform AWS Provider - VPC](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/vpc)
- [Terraform AWS Provider - EC2](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/instance)
- [Terraform AWS Provider - S3](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/s3_bucket)

---

**Congratulations!** You've completed your first Terraform lab. You now understand the fundamental Terraform workflow and can create basic AWS infrastructure as code.
