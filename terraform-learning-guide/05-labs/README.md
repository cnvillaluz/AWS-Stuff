# Chapter 5: Hands-On Labs & Exercises

Practice your Terraform skills with these hands-on exercises.

## Lab Structure

Each lab includes:
- **Objective**: What you'll build
- **Prerequisites**: What you need to know
- **Estimated Time**: How long it should take
- **Instructions**: Step-by-step guidance
- **Validation**: How to verify success
- **Cleanup**: How to destroy resources

## Beginner Labs

### Lab 1: Your First Infrastructure
**Objective**: Create basic AWS resources and understand Terraform workflow

**What You'll Build**:
- VPC with public subnet
- S3 bucket with versioning
- EC2 instance

**Estimated Time**: 30 minutes

**Prerequisites**:
- AWS account configured
- Terraform installed
- Basic understanding of AWS services

[Lab 1 Instructions →](./beginner/lab1-first-infrastructure.md)

---

### Lab 2: Working with Variables
**Objective**: Make your configuration flexible with variables

**What You'll Build**:
- VPC with configurable CIDR
- Multiple subnets using variables
- Environment-specific configurations

**Estimated Time**: 45 minutes

[Lab 2 Instructions →](./beginner/lab2-variables.md)

---

### Lab 3: Outputs and Data Sources
**Objective**: Extract information and query existing resources

**What You'll Build**:
- Query existing AWS resources
- Export resource information
- Use outputs in other configurations

**Estimated Time**: 30 minutes

[Lab 3 Instructions →](./beginner/lab3-outputs-data.md)

---

## Intermediate Labs

### Lab 4: Creating and Using Modules
**Objective**: Build reusable infrastructure components

**What You'll Build**:
- Custom VPC module
- Web server module
- Module composition

**Estimated Time**: 1.5 hours

[Lab 4 Instructions →](./intermediate/lab4-modules.md)

---

### Lab 5: Remote State Management
**Objective**: Set up remote state with S3 and DynamoDB

**What You'll Build**:
- S3 bucket for state storage
- DynamoDB table for state locking
- Backend configuration
- State migration

**Estimated Time**: 1 hour

[Lab 5 Instructions →](./intermediate/lab5-remote-state.md)

---

### Lab 6: Multi-Tier Application
**Objective**: Build a complete multi-tier architecture

**What You'll Build**:
- VPC with public and private subnets
- Application Load Balancer
- Auto Scaling Group
- RDS database

**Estimated Time**: 2 hours

[Lab 6 Instructions →](./intermediate/lab6-multi-tier.md)

---

## Advanced Labs

### Lab 7: Dynamic Infrastructure
**Objective**: Master dynamic blocks and for_each

**What You'll Build**:
- Dynamic security group rules
- Multiple environments from configuration
- Complex resource iteration

**Estimated Time**: 1.5 hours

[Lab 7 Instructions →](./advanced/lab7-dynamic.md)

---

### Lab 8: Multi-Region Deployment
**Objective**: Deploy infrastructure across multiple regions

**What You'll Build**:
- VPC in multiple regions
- Cross-region replication
- Route53 failover routing

**Estimated Time**: 2 hours

[Lab 8 Instructions →](./advanced/lab8-multi-region.md)

---

### Lab 9: Serverless Application
**Objective**: Build a serverless API with Terraform

**What You'll Build**:
- Lambda functions
- API Gateway
- DynamoDB tables
- CloudWatch monitoring

**Estimated Time**: 2 hours

[Lab 9 Instructions →](./advanced/lab9-serverless.md)

---

### Lab 10: CI/CD Integration
**Objective**: Automate Terraform with GitHub Actions

**What You'll Build**:
- GitHub Actions workflow
- Automated testing
- Deployment pipeline
- State management in CI/CD

**Estimated Time**: 2 hours

[Lab 10 Instructions →](./advanced/lab10-cicd.md)

---

## Challenge Projects

### Challenge 1: High-Availability Web Application
**Difficulty**: Advanced

**Objective**: Design and implement a production-ready, highly available web application

**Requirements**:
- Multi-AZ deployment
- Auto-scaling
- Monitoring and alerting
- Disaster recovery
- Security best practices

**Estimated Time**: 4-6 hours

[Challenge Details →](./challenges/challenge1-ha-webapp.md)

---

### Challenge 2: Microservices Infrastructure
**Difficulty**: Expert

**Objective**: Build infrastructure for a microservices architecture

**Requirements**:
- ECS/EKS cluster
- Service mesh
- API Gateway
- Centralized logging
- Distributed tracing

**Estimated Time**: 6-8 hours

[Challenge Details →](./challenges/challenge2-microservices.md)

---

### Challenge 3: Secure Multi-Environment Setup
**Difficulty**: Expert

**Objective**: Implement a secure, compliant multi-environment infrastructure

**Requirements**:
- Separate AWS accounts
- Transit Gateway
- Central logging
- Compliance controls (AWS Config, GuardDuty)
- Secrets management

**Estimated Time**: 6-8 hours

[Challenge Details →](./challenges/challenge3-secure-multi-env.md)

---

## Lab Tips

### Before Starting Any Lab

1. **Read through completely first**
2. **Check AWS Free Tier limits**
3. **Set up billing alerts**
4. **Have AWS CLI configured**
5. **Create a dedicated directory for each lab**

### During the Lab

1. **Follow along, don't just copy-paste**
2. **Read error messages carefully**
3. **Use `terraform plan` liberally**
4. **Validate at each step**
5. **Take notes on challenges**

### After Completing

1. **Review what you built**
2. **Understand the costs**
3. **Run `terraform destroy` to clean up**
4. **Try modifying the solution**
5. **Document lessons learned**

## Common Issues and Solutions

### Issue: "Resource already exists"
**Solution**: Either import the existing resource or change the name in your configuration.

```bash
terraform import aws_s3_bucket.example my-bucket-name
```

### Issue: "State lock acquisition failed"
**Solution**: Wait for the lock to release or manually release it if it's stuck.

```bash
# Only if you're sure no other process is using it
terraform force-unlock <lock-id>
```

### Issue: "Error launching source instance: Unsupported"
**Solution**: Check that the AMI and instance type are available in your region.

### Issue: Unexpected costs
**Solution**: Always run `terraform destroy` after labs and check AWS Cost Explorer.

```bash
terraform destroy -auto-approve
```

## Additional Resources

### Practice Environments

- **LocalStack**: Test AWS services locally
- **Terraform Cloud Free Tier**: Practice remote state management
- **AWS Free Tier**: 12 months of free resources

### Validation Tools

```bash
# Validate syntax
terraform validate

# Check formatting
terraform fmt -check

# Security scanning
tfsec .

# Cost estimation
terraform plan -out=tfplan
terraform show -json tfplan | infracost breakdown
```

### Useful Commands for Labs

```bash
# Quick destroy without confirmation (use carefully!)
terraform destroy -auto-approve

# Target specific resource
terraform apply -target=aws_instance.web

# Refresh state
terraform refresh

# Show current state
terraform show

# Get specific output
terraform output -raw instance_ip
```

## Lab Completion Checklist

After each lab:

- [ ] All resources created successfully
- [ ] Outputs displaying correct information
- [ ] Configuration follows best practices
- [ ] Code is formatted (`terraform fmt`)
- [ ] Resources are tagged appropriately
- [ ] Destruction completed successfully
- [ ] No unexpected AWS charges
- [ ] Lessons learned documented

## Getting Help

If you get stuck:

1. **Check error messages** - They're usually informative
2. **Review documentation** - [Terraform AWS Provider Docs](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
3. **Search for the error** - Likely someone else has encountered it
4. **Check AWS Console** - See what actually got created
5. **Start fresh** - Sometimes `terraform destroy` and starting over helps

## Progress Tracking

Mark your progress as you complete labs:

**Beginner Labs**
- [ ] Lab 1: Your First Infrastructure
- [ ] Lab 2: Working with Variables
- [ ] Lab 3: Outputs and Data Sources

**Intermediate Labs**
- [ ] Lab 4: Creating and Using Modules
- [ ] Lab 5: Remote State Management
- [ ] Lab 6: Multi-Tier Application

**Advanced Labs**
- [ ] Lab 7: Dynamic Infrastructure
- [ ] Lab 8: Multi-Region Deployment
- [ ] Lab 9: Serverless Application
- [ ] Lab 10: CI/CD Integration

**Challenge Projects**
- [ ] Challenge 1: High-Availability Web Application
- [ ] Challenge 2: Microservices Infrastructure
- [ ] Challenge 3: Secure Multi-Environment Setup

---

**Ready to start?** Begin with [Lab 1: Your First Infrastructure](./beginner/lab1-first-infrastructure.md)

Remember: The goal is learning, not perfection. Experiment, break things, and learn from the experience!
