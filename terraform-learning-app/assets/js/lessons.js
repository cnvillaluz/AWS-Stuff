// Lessons Content and Loading

// All lessons data
const lessonsData = {
    beginner: [
        {
            id: 'beginner-what-is-terraform',
            title: 'What is Terraform?',
            duration: '15 min',
            description: 'Learn what Terraform is and why it\'s used for Infrastructure as Code.',
            topics: ['IaC', 'Terraform Basics', 'Benefits'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Understand what Terraform is and why it's essential for modern infrastructure management.</p>

                <h3>📖 Simple Explanation</h3>
                <p><strong>Terraform</strong> is like a blueprint builder for your cloud infrastructure. Instead of manually clicking through AWS console to create servers, databases, and networks, you write code that describes what you want, and Terraform builds it for you.</p>

                <div class="alert alert-info">
                    <strong>Think of it like this:</strong> If AWS is a LEGO set, Terraform is the instruction manual that tells you exactly how to build your creation, and it can rebuild it the same way every time!
                </div>

                <h3>💡 Key Concepts</h3>
                <ul>
                    <li><strong>Infrastructure as Code (IaC):</strong> Writing code to manage infrastructure instead of manual configuration</li>
                    <li><strong>Declarative:</strong> You describe what you want, not how to create it</li>
                    <li><strong>Version Control:</strong> Track changes to your infrastructure like you do with code</li>
                    <li><strong>Reproducible:</strong> Create identical environments every time</li>
                </ul>

                <h3>🎨 Real-World Example</h3>
                <p><strong>Without Terraform:</strong></p>
                <ol>
                    <li>Log into AWS Console</li>
                    <li>Click to create VPC</li>
                    <li>Click to create subnet</li>
                    <li>Click to create security group</li>
                    <li>Click to create EC2 instance</li>
                    <li>Configure each manually</li>
                    <li>Hope you remember all settings for next time!</li>
                </ol>

                <p><strong>With Terraform:</strong></p>
                <pre><code>resource "aws_instance" "web" {
  ami           = "ami-12345"
  instance_type = "t2.micro"
  # All configuration in one file!
}</code></pre>
                <p>Run <code>terraform apply</code> and it's done! Need another one? Run the same code again.</p>

                <h3>✅ Benefits</h3>
                <ul>
                    <li>✅ <strong>Consistency:</strong> Same configuration every time</li>
                    <li>✅ <strong>Speed:</strong> Create complex infrastructure in minutes</li>
                    <li>✅ <strong>Documentation:</strong> Your code IS your documentation</li>
                    <li>✅ <strong>Collaboration:</strong> Team can work together using Git</li>
                    <li>✅ <strong>Safety:</strong> Preview changes before applying</li>
                </ul>

                <h3>🚀 Try It Yourself</h3>
                <p>In the next lesson, you'll create your first AWS resource using Terraform!</p>
            `
        },
        {
            id: 'beginner-installing-terraform',
            title: 'Installing Terraform',
            duration: '10 min',
            description: 'Set up Terraform and AWS CLI on your machine.',
            topics: ['Installation', 'Setup', 'AWS CLI'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Install Terraform and configure AWS credentials to start building infrastructure.</p>

                <h3>📥 Step 1: Install Terraform</h3>

                <p><strong>On Mac (using Homebrew):</strong></p>
                <pre><code>brew tap hashicorp/tap
brew install hashicorp/tap/terraform</code></pre>

                <p><strong>On Windows (using Chocolatey):</strong></p>
                <pre><code>choco install terraform</code></pre>

                <p><strong>On Linux:</strong></p>
                <pre><code>wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform</code></pre>

                <p><strong>Verify Installation:</strong></p>
                <pre><code>terraform version</code></pre>

                <h3>☁️ Step 2: Install AWS CLI</h3>
                <p>Download from: <a href="https://aws.amazon.com/cli/" target="_blank">https://aws.amazon.com/cli/</a></p>

                <p><strong>Verify Installation:</strong></p>
                <pre><code>aws --version</code></pre>

                <h3>🔑 Step 3: Configure AWS Credentials</h3>
                <ol>
                    <li>Log into AWS Console</li>
                    <li>Go to IAM → Users → Your User → Security Credentials</li>
                    <li>Create Access Key</li>
                    <li>Save the Access Key ID and Secret Access Key</li>
                </ol>

                <p><strong>Configure AWS CLI:</strong></p>
                <pre><code>aws configure

AWS Access Key ID: [paste your key]
AWS Secret Access Key: [paste your secret]
Default region: us-east-1
Default output format: json</code></pre>

                <div class="alert alert-warning">
                    <strong>⚠️ Security Note:</strong> Never commit AWS credentials to Git! Keep them secure.
                </div>

                <h3>✅ Verify Setup</h3>
                <pre><code># Test AWS connection
aws sts get-caller-identity

# Test Terraform
terraform -help</code></pre>

                <p>If both commands work, you're ready to go! 🎉</p>
            `
        },
        {
            id: 'beginner-first-resource',
            title: 'Your First AWS Resource',
            duration: '20 min',
            description: 'Create your first S3 bucket using Terraform.',
            topics: ['S3', 'Resources', 'terraform apply'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Create your first AWS resource (an S3 bucket) using Terraform and understand the basic workflow.</p>

                <h3>📝 Step 1: Create Your First Terraform File</h3>
                <p>Create a new directory and a file called <code>main.tf</code>:</p>

                <pre><code>mkdir my-first-terraform
cd my-first-terraform
touch main.tf</code></pre>

                <h3>✍️ Step 2: Write Your Configuration</h3>
                <p>Open <code>main.tf</code> and add this code:</p>

                <pre><code>terraform {
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

resource "aws_s3_bucket" "my_first_bucket" {
  bucket = "my-terraform-bucket-12345"  # Change this to be unique!

  tags = {
    Name        = "My First Bucket"
    Environment = "Learning"
    ManagedBy   = "Terraform"
  }
}</code></pre>

                <div class="alert alert-info">
                    <strong>💡 Explanation:</strong><br>
                    - <strong>terraform</strong> block: Specifies which providers we need<br>
                    - <strong>provider "aws"</strong>: Configures AWS as our cloud provider<br>
                    - <strong>resource</strong>: Defines what we want to create (an S3 bucket)
                </div>

                <h3>🚀 Step 3: Initialize Terraform</h3>
                <pre><code>terraform init</code></pre>
                <p>This downloads the AWS provider plugin. You'll see a success message!</p>

                <h3>👀 Step 4: Preview Changes</h3>
                <pre><code>terraform plan</code></pre>
                <p>This shows what Terraform will create. Look for the <strong>+</strong> symbol indicating new resources.</p>

                <h3>✨ Step 5: Create the Resource</h3>
                <pre><code>terraform apply</code></pre>
                <p>Type <code>yes</code> when prompted. Terraform will create your S3 bucket!</p>

                <h3>🎉 Step 6: Verify</h3>
                <p>Check your AWS Console → S3. You should see your new bucket!</p>

                <p>Or use AWS CLI:</p>
                <pre><code>aws s3 ls</code></pre>

                <h3>🧹 Step 7: Clean Up</h3>
                <div class="alert alert-warning">
                    <strong>⚠️ Always clean up to avoid charges!</strong>
                </div>
                <pre><code>terraform destroy</code></pre>
                <p>Type <code>yes</code> to delete the bucket.</p>

                <h3>🎓 What You Learned</h3>
                <ul>
                    <li>✅ The basic Terraform workflow: init → plan → apply → destroy</li>
                    <li>✅ How to define a resource</li>
                    <li>✅ How to use providers</li>
                    <li>✅ How to tag resources</li>
                </ul>
            `
        },
        {
            id: 'beginner-terraform-workflow',
            title: 'The Terraform Workflow',
            duration: '15 min',
            description: 'Master the core Terraform commands and workflow.',
            topics: ['init', 'plan', 'apply', 'destroy'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Understand the four essential Terraform commands and when to use them.</p>

                <h3>🔄 The Terraform Lifecycle</h3>
                <p>Working with Terraform follows a simple pattern:</p>

                <div style="background: #f5f5f5; padding: 20px; border-radius: 10px; margin: 20px 0;">
                    <p style="text-align: center; font-size: 1.2rem;">
                        <strong>Write Code</strong> → <strong>Init</strong> → <strong>Plan</strong> → <strong>Apply</strong> → <strong>Destroy</strong>
                    </p>
                </div>

                <h3>1️⃣ terraform init</h3>
                <p><strong>What it does:</strong> Prepares your directory for Terraform</p>
                <ul>
                    <li>Downloads provider plugins (like AWS)</li>
                    <li>Sets up the backend (where state is stored)</li>
                    <li>Initializes modules</li>
                </ul>
                <p><strong>When to use:</strong> First time in a directory, or when you add new providers</p>
                <pre><code>terraform init</code></pre>

                <h3>2️⃣ terraform plan</h3>
                <p><strong>What it does:</strong> Shows what will change WITHOUT making changes</p>
                <ul>
                    <li><strong>+ green</strong> = will be created</li>
                    <li><strong>~ yellow</strong> = will be modified</li>
                    <li><strong>- red</strong> = will be destroyed</li>
                </ul>
                <p><strong>When to use:</strong> ALWAYS before apply! It's your safety check.</p>
                <pre><code>terraform plan</code></pre>

                <div class="alert alert-info">
                    <strong>💡 Pro Tip:</strong> Think of <code>terraform plan</code> like a GPS route preview before you start driving!
                </div>

                <h3>3️⃣ terraform apply</h3>
                <p><strong>What it does:</strong> Makes the changes happen</p>
                <ul>
                    <li>Creates/updates/deletes resources</li>
                    <li>Updates the state file</li>
                    <li>Shows you what was changed</li>
                </ul>
                <p><strong>When to use:</strong> After reviewing the plan and you're ready to proceed</p>
                <pre><code>terraform apply

# Skip the confirmation prompt (use carefully!)
terraform apply -auto-approve</code></pre>

                <h3>4️⃣ terraform destroy</h3>
                <p><strong>What it does:</strong> Deletes ALL resources managed by Terraform</p>
                <p><strong>When to use:</strong> When you're done with your infrastructure (especially important for learning to avoid costs!)</p>
                <pre><code>terraform destroy</code></pre>

                <div class="alert alert-warning">
                    <strong>⚠️ Warning:</strong> <code>terraform destroy</code> will DELETE everything. Use with caution in production!
                </div>

                <h3>📊 Bonus Commands</h3>
                <pre><code># Format your code nicely
terraform fmt

# Check syntax without accessing providers
terraform validate

# Show current state
terraform show

# List resources in state
terraform state list</code></pre>

                <h3>🎮 Practice Workflow</h3>
                <p>Try this flow with your S3 bucket:</p>
                <ol>
                    <li>Write code in main.tf</li>
                    <li>Run <code>terraform init</code></li>
                    <li>Run <code>terraform plan</code> - Review output</li>
                    <li>Run <code>terraform apply</code> - Type yes</li>
                    <li>Check AWS Console</li>
                    <li>Make a change to your code (add a tag)</li>
                    <li>Run <code>terraform plan</code> - See the diff</li>
                    <li>Run <code>terraform apply</code></li>
                    <li>Run <code>terraform destroy</code> when done</li>
                </ol>
            `
        },
        {
            id: 'beginner-understanding-hcl',
            title: 'Understanding HCL Syntax',
            duration: '20 min',
            description: 'Learn HashiCorp Configuration Language basics.',
            topics: ['HCL', 'Syntax', 'Blocks'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Understand the basic syntax of HCL (HashiCorp Configuration Language) - the language Terraform uses.</p>

                <h3>📖 HCL is Simple!</h3>
                <p>HCL is designed to be easy to read and write. It looks similar to JSON but is more human-friendly.</p>

                <h3>🏗️ Building Blocks</h3>
                <p>Everything in Terraform is made of <strong>blocks</strong>:</p>

                <pre><code>block_type "label" "name" {
  argument1 = value1
  argument2 = value2

  nested_block {
    argument3 = value3
  }
}</code></pre>

                <h3>1️⃣ Resource Block</h3>
                <p>The most common block - defines infrastructure:</p>
                <pre><code>resource "aws_instance" "my_server" {
  ami           = "ami-12345"
  instance_type = "t2.micro"

  tags = {
    Name = "My Server"
  }
}</code></pre>

                <p><strong>Breaking it down:</strong></p>
                <ul>
                    <li><code>resource</code> = block type</li>
                    <li><code>"aws_instance"</code> = resource type</li>
                    <li><code>"my_server"</code> = resource name (your choice)</li>
                    <li><code>ami</code>, <code>instance_type</code> = arguments</li>
                    <li><code>tags</code> = nested block</li>
                </ul>

                <h3>2️⃣ Variables</h3>
                <p>Make your code reusable:</p>
                <pre><code>variable "instance_type" {
  description = "Type of EC2 instance"
  type        = string
  default     = "t2.micro"
}</code></pre>

                <p><strong>Use the variable:</strong></p>
                <pre><code>resource "aws_instance" "my_server" {
  instance_type = var.instance_type
}</code></pre>

                <h3>3️⃣ Outputs</h3>
                <p>Display information after creation:</p>
                <pre><code>output "server_ip" {
  description = "The public IP"
  value       = aws_instance.my_server.public_ip
}</code></pre>

                <h3>4️⃣ Data Types</h3>
                <pre><code># String
name = "hello"

# Number
count = 5

# Boolean
enabled = true

# List
zones = ["us-east-1a", "us-east-1b"]

# Map
tags = {
  Name = "Server"
  Env  = "Dev"
}</code></pre>

                <h3>5️⃣ Comments</h3>
                <pre><code># Single line comment

// Also single line

/*
  Multi-line
  comment
*/</code></pre>

                <h3>6️⃣ String Interpolation</h3>
                <pre><code>name = "server-1"
full_name = "production-\${var.name}"  # Result: "production-server-1"</code></pre>

                <h3>🎨 Example: Complete Configuration</h3>
                <pre><code>variable "environment" {
  default = "dev"
}

resource "aws_s3_bucket" "data" {
  bucket = "my-\${var.environment}-bucket"

  tags = {
    Environment = var.environment
    ManagedBy   = "Terraform"
  }
}

output "bucket_name" {
  value = aws_s3_bucket.data.bucket
}</code></pre>

                <h3>✨ Pro Tips</h3>
                <ul>
                    <li>Use <code>terraform fmt</code> to auto-format your code</li>
                    <li>Indent with 2 spaces</li>
                    <li>Always use meaningful names</li>
                    <li>Add comments to explain complex logic</li>
                </ul>
            `
        },
        {
            id: 'beginner-creating-ec2',
            title: 'Creating Your First EC2 Instance',
            duration: '25 min',
            description: 'Launch an EC2 instance with security groups.',
            topics: ['EC2', 'Security Groups', 'User Data'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Create a web server on AWS using EC2 with proper security configuration.</p>

                <h3>🖥️ What is EC2?</h3>
                <p><strong>EC2 (Elastic Compute Cloud)</strong> = Virtual servers in the cloud</p>
                <p>Think of it as renting a computer in AWS that you can access remotely.</p>

                <h3>📝 Step 1: Complete Configuration</h3>
                <p>Create <code>main.tf</code>:</p>

                <pre><code>terraform {
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

# Get latest Amazon Linux 2 AMI
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]

  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Security Group (firewall rules)
resource "aws_security_group" "web_sg" {
  name        = "web-server-sg"
  description = "Allow HTTP and SSH"

  # Allow HTTP from anywhere
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow SSH from anywhere (restrict this in production!)
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Allow all outbound traffic
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "web-server-sg"
  }
}

# EC2 Instance
resource "aws_instance" "web_server" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t2.micro"  # Free tier eligible!

  vpc_security_group_ids = [aws_security_group.web_sg.id]

  # Install and start web server
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<h1>Hello from Terraform! 🚀</h1>" > /var/www/html/index.html
              EOF

  tags = {
    Name = "my-web-server"
  }
}

# Output the public IP
output "web_server_ip" {
  description = "Public IP of web server"
  value       = aws_instance.web_server.public_ip
}

output "web_server_url" {
  description = "URL to access web server"
  value       = "http://\${aws_instance.web_server.public_ip}"
}</code></pre>

                <h3>🚀 Step 2: Deploy</h3>
                <pre><code>terraform init
terraform plan
terraform apply</code></pre>

                <h3>🌐 Step 3: Test Your Web Server</h3>
                <p>After apply completes, you'll see the IP address. Copy it and paste in your browser:</p>
                <pre><code>http://YOUR_IP_ADDRESS</code></pre>

                <p>You should see "Hello from Terraform! 🚀"</p>

                <h3>📊 Understanding the Parts</h3>

                <p><strong>1. Data Source (aws_ami):</strong></p>
                <p>Finds the latest Amazon Linux image automatically - no need to hardcode AMI IDs!</p>

                <p><strong>2. Security Group:</strong></p>
                <ul>
                    <li><strong>Ingress</strong> = incoming traffic rules</li>
                    <li><strong>Egress</strong> = outgoing traffic rules</li>
                    <li>Port 80 = HTTP (web traffic)</li>
                    <li>Port 22 = SSH (remote access)</li>
                </ul>

                <p><strong>3. User Data:</strong></p>
                <p>Script that runs when the instance first starts. We use it to install Apache web server.</p>

                <p><strong>4. Dependencies:</strong></p>
                <p>Terraform automatically knows to create the security group BEFORE the instance because the instance references it!</p>

                <h3>🧹 Step 4: Clean Up</h3>
                <pre><code>terraform destroy</code></pre>

                <div class="alert alert-warning">
                    <strong>💰 Cost Note:</strong> t2.micro is free tier eligible, but always destroy when done practicing!
                </div>

                <h3>🎓 What You Learned</h3>
                <ul>
                    <li>✅ How to create EC2 instances</li>
                    <li>✅ How to configure security groups (firewall rules)</li>
                    <li>✅ How to use data sources to find AMIs</li>
                    <li>✅ How to use user data to bootstrap instances</li>
                    <li>✅ How Terraform handles dependencies</li>
                </ul>

                <h3>🚀 Challenge</h3>
                <p>Try modifying the user data to display your name instead of "Terraform"!</p>
            `
        },
        {
            id: 'beginner-vpc-basics',
            title: 'VPC Networking Basics',
            duration: '30 min',
            description: 'Create a VPC with public and private subnets.',
            topics: ['VPC', 'Subnets', 'Internet Gateway'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Understand AWS networking basics and create a VPC from scratch.</p>

                <h3>🌐 What is a VPC?</h3>
                <p><strong>VPC (Virtual Private Cloud)</strong> = Your own private network in AWS</p>

                <div class="alert alert-info">
                    <strong>Real-world analogy:</strong><br>
                    VPC = Your office building<br>
                    Subnets = Floors in the building<br>
                    Security Groups = Key card access<br>
                    Internet Gateway = Front door to the outside world
                </div>

                <h3>🏗️ Basic VPC Architecture</h3>
                <pre><code>Internet
    ↓
Internet Gateway
    ↓
Public Subnet (10.0.1.0/24)
    ↓
Private Subnet (10.0.2.0/24)</code></pre>

                <h3>📝 Create Your VPC</h3>
                <pre><code>terraform {
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

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "my-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "my-igw"
  }
}

# Public Subnet
resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.1.0/24"
  availability_zone       = "us-east-1a"
  map_public_ip_on_launch = true

  tags = {
    Name = "public-subnet"
    Type = "Public"
  }
}

# Private Subnet
resource "aws_subnet" "private" {
  vpc_id            = aws_vpc.main.id
  cidr_block        = "10.0.2.0/24"
  availability_zone = "us-east-1a"

  tags = {
    Name = "private-subnet"
    Type = "Private"
  }
}

# Route Table for Public Subnet
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  # Route to Internet Gateway
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "public-rt"
  }
}

# Associate Route Table with Public Subnet
resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

# Outputs
output "vpc_id" {
  value = aws_vpc.main.id
}

output "public_subnet_id" {
  value = aws_subnet.public.id
}

output "private_subnet_id" {
  value = aws_subnet.private.id
}</code></pre>

                <h3>📊 Understanding CIDR Blocks</h3>
                <ul>
                    <li><strong>10.0.0.0/16</strong> = VPC range (65,536 IP addresses)</li>
                    <li><strong>10.0.1.0/24</strong> = Public subnet (256 IP addresses)</li>
                    <li><strong>10.0.2.0/24</strong> = Private subnet (256 IP addresses)</li>
                </ul>

                <div class="alert alert-info">
                    <strong>💡 Simple rule:</strong> Smaller number after / = more IP addresses<br>
                    /16 = 65,536 IPs | /24 = 256 IPs | /32 = 1 IP
                </div>

                <h3>🔍 What Each Resource Does</h3>

                <p><strong>VPC:</strong> Creates your isolated network</p>
                <p><strong>Internet Gateway:</strong> Allows internet access (like a door to the outside)</p>
                <p><strong>Public Subnet:</strong> Resources here can access the internet</p>
                <p><strong>Private Subnet:</strong> Resources here are isolated from the internet</p>
                <p><strong>Route Table:</strong> Tells traffic where to go (like GPS directions)</p>

                <h3>🚀 Deploy Your VPC</h3>
                <pre><code>terraform init
terraform plan
terraform apply</code></pre>

                <h3>✅ Verify in AWS Console</h3>
                <ol>
                    <li>Go to AWS Console → VPC</li>
                    <li>See your VPC, subnets, and internet gateway</li>
                    <li>Check the route table associations</li>
                </ol>

                <h3>🧹 Clean Up</h3>
                <pre><code>terraform destroy</code></pre>

                <h3>🎓 What You Learned</h3>
                <ul>
                    <li>✅ VPC basics and components</li>
                    <li>✅ Public vs Private subnets</li>
                    <li>✅ Internet Gateways</li>
                    <li>✅ Route tables and associations</li>
                    <li>✅ CIDR notation basics</li>
                </ul>

                <h3>📚 Next Steps</h3>
                <p>In the next lesson, you'll launch EC2 instances in this VPC!</p>
            `
        },
        {
            id: 'beginner-state-intro',
            title: 'Understanding Terraform State',
            duration: '20 min',
            description: 'Learn what state files are and why they matter.',
            topics: ['State', 'terraform.tfstate', 'State Management'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Understand what Terraform state is and why it's crucial for managing infrastructure.</p>

                <h3>📋 What is State?</h3>
                <p><strong>State</strong> = Terraform's memory of what it created</p>

                <div class="alert alert-info">
                    <strong>Think of it like this:</strong><br>
                    Your Terraform code = Recipe<br>
                    AWS Resources = The cooked meal<br>
                    State file = Photos of the meal to remember what you made
                </div>

                <h3>📄 The State File</h3>
                <p>After running <code>terraform apply</code>, Terraform creates a file called <code>terraform.tfstate</code></p>

                <p><strong>What's in the state file?</strong></p>
                <ul>
                    <li>IDs of all created resources</li>
                    <li>Current configuration</li>
                    <li>Resource dependencies</li>
                    <li>Metadata about resources</li>
                </ul>

                <h3>🔍 View Your State</h3>
                <pre><code># Show all resources in state
terraform state list

# Show details of a specific resource
terraform state show aws_instance.web_server

# View entire state
terraform show</code></pre>

                <h3>🎮 Try It Yourself</h3>
                <ol>
                    <li>Create a simple S3 bucket with Terraform</li>
                    <li>Run <code>terraform apply</code></li>
                    <li>Look at <code>terraform.tfstate</code> file (but don't edit it!)</li>
                    <li>Run <code>terraform state list</code></li>
                    <li>Run <code>terraform state show aws_s3_bucket.my_bucket</code></li>
                </ol>

                <h3>⚠️ Important Rules</h3>
                <div class="alert alert-warning">
                    <strong>Never:</strong><br>
                    ❌ Manually edit the state file<br>
                    ❌ Commit sensitive state files to Git<br>
                    ❌ Delete the state file (you'll lose track of resources)<br>
                    ❌ Share state files between team members directly
                </div>

                <h3>✅ Do This Instead</h3>
                <div class="alert alert-success">
                    <strong>Always:</strong><br>
                    ✅ Let Terraform manage the state<br>
                    ✅ Use remote state storage (S3) for teams<br>
                    ✅ Back up your state file<br>
                    ✅ Use state locking to prevent conflicts
                </div>

                <h3>🔄 How State Works</h3>
                <pre><code>1. You write code: "I want an S3 bucket"
2. Terraform plan: Compares code to state
3. State says: "No bucket exists yet"
4. Terraform apply: Creates bucket, saves to state
5. You change code: "I want tags on the bucket"
6. Terraform plan: Compares code to state
7. State says: "Bucket exists, but tags are different"
8. Terraform apply: Updates bucket, updates state</code></pre>

                <h3>🎨 Example: State in Action</h3>
                <p><strong>First apply:</strong></p>
                <pre><code>resource "aws_s3_bucket" "data" {
  bucket = "my-bucket"
}

# terraform apply
# State: Bucket "my-bucket" created with ID "my-bucket"</code></pre>

                <p><strong>Add tags:</strong></p>
                <pre><code>resource "aws_s3_bucket" "data" {
  bucket = "my-bucket"

  tags = {
    Environment = "dev"
  }
}

# terraform plan
# Terraform says: "I'll UPDATE the bucket (not recreate it)"
# How does it know? The STATE file!</code></pre>

                <h3>📁 Local vs Remote State</h3>
                <p><strong>Local State:</strong></p>
                <ul>
                    <li>Stored on your computer</li>
                    <li>Fine for learning</li>
                    <li>Not good for teams</li>
                </ul>

                <p><strong>Remote State:</strong></p>
                <ul>
                    <li>Stored in S3 or Terraform Cloud</li>
                    <li>Shared with team</li>
                    <li>Has locking (prevents conflicts)</li>
                    <li>Encrypted and backed up</li>
                </ul>

                <h3>🎓 What You Learned</h3>
                <ul>
                    <li>✅ What state is and why it's important</li>
                    <li>✅ How to view state information</li>
                    <li>✅ State file best practices</li>
                    <li>✅ The difference between local and remote state</li>
                </ul>

                <h3>📚 Coming Next</h3>
                <p>In intermediate lessons, you'll learn how to set up remote state with S3 and DynamoDB!</p>
            `
        }
    ],
    intermediate: [
        {
            id: 'intermediate-variables-deep-dive',
            title: 'Variables Deep Dive',
            duration: '30 min',
            description: 'Master input variables and validation.',
            topics: ['Variables', 'Validation', 'Types'],
            content: `
                <h3>🎯 What You'll Learn</h3>
                <p>Make your Terraform code flexible and reusable with variables.</p>

                <h3>🎨 Why Variables?</h3>
                <p>Instead of hardcoding values, use variables to make your code work in different environments!</p>

                <p><strong>Without variables (bad):</strong></p>
                <pre><code>resource "aws_instance" "web" {
  instance_type = "t2.micro"  # Hardcoded
  ami           = "ami-12345"  # Hardcoded
}</code></pre>

                <p><strong>With variables (good):</strong></p>
                <pre><code>resource "aws_instance" "web" {
  instance_type = var.instance_type
  ami           = var.ami_id
}</code></pre>

                <h3>📝 Defining Variables</h3>
                <p>Create <code>variables.tf</code>:</p>

                <pre><code>variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t2.micro"
}</code></pre>

                <p>More examples with validation coming...</p>
            `
        }
    ],
    advanced: [],
    expert: []
};

// Load lessons into the UI
function loadLessons() {
    const container = document.getElementById('lessonsContainer');
    if (!container) return;

    let html = '';

    for (const [level, lessons] of Object.entries(lessonsData)) {
        if (lessons.length === 0) continue;

        html += `
            <div class="lesson-section" data-level="${level}">
                <h3 class="lesson-badge ${level}">${level.charAt(0).toUpperCase() + level.slice(1)} Level</h3>
                ${lessons.map(lesson => createLessonCard(lesson, level)).join('')}
            </div>
        `;
    }

    container.innerHTML = html;
}

// Create individual lesson card
function createLessonCard(lesson, level) {
    const isComplete = isLessonComplete(lesson.id);

    return `
        <div class="lesson-card">
            <input
                type="checkbox"
                class="completion-checkbox"
                data-lesson="${lesson.id}"
                ${isComplete ? 'checked' : ''}
                onchange="toggleLessonComplete('${lesson.id}')"
            />
            <div class="lesson-header">
                <h4 class="lesson-title">${lesson.title}</h4>
            </div>
            <div class="lesson-meta">
                <span class="lesson-badge ${level}">⏱️ ${lesson.duration}</span>
            </div>
            <p class="lesson-description">${lesson.description}</p>
            <div class="lesson-topics">
                ${lesson.topics.map(topic => `<span class="topic-tag">${topic}</span>`).join('')}
            </div>
            <div class="lesson-actions">
                <button class="btn btn-primary" onclick="startLesson('${lesson.id}', 'lesson')">
                    ${isComplete ? '📖 Review' : '🚀 Start Lesson'}
                </button>
            </div>
        </div>
    `;
}

// Get lesson content
function getLessonContent(lessonId) {
    for (const [level, lessons] of Object.entries(lessonsData)) {
        const lesson = lessons.find(l => l.id === lessonId);
        if (lesson) return lesson;
    }
    return null;
}

// Practice exercises will be loaded here
function loadPracticeExercises() {
    const container = document.getElementById('practiceContainer');
    if (!container) return;

    container.innerHTML = `
        <div class="practice-card">
            <h3>🎯 Coming Soon: Interactive Practice Exercises</h3>
            <p>Practice exercises will be added to reinforce your learning!</p>
        </div>
    `;
}

// Labs will be loaded here
function loadLabs() {
    const container = document.getElementById('labsContainer');
    if (!container) return;

    container.innerHTML = `
        <div class="lab-card">
            <h3>🧪 Coming Soon: Hands-On Labs</h3>
            <p>Guided labs with AWS will be added for practical experience!</p>
        </div>
    `;
}
