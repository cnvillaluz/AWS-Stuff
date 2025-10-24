# Example 1: Your First S3 Bucket

## Overview
This example demonstrates the simplest possible Terraform configuration - creating an S3 bucket in AWS.

## What You'll Learn
- How to configure the AWS provider
- How to create an S3 bucket resource
- How to use outputs to display resource information
- How to use the random provider for unique naming

## Prerequisites
- AWS account configured with AWS CLI
- Terraform installed (version >= 1.0)

## Files
- `main.tf` - The main configuration file

## Steps to Run

1. Initialize Terraform:
```bash
terraform init
```

2. Review the plan:
```bash
terraform plan
```

3. Apply the configuration:
```bash
terraform apply
```

4. View the outputs:
```bash
terraform output
```

5. Verify in AWS Console:
- Go to S3 console
- Find your bucket with the generated name

6. Clean up:
```bash
terraform destroy
```

## What's Happening?

1. **Provider Configuration**: Sets up AWS provider with region
2. **Random ID**: Generates a unique suffix for the bucket name
3. **S3 Bucket**: Creates a bucket with a globally unique name
4. **Tags**: Adds metadata to the bucket for organization
5. **Outputs**: Displays bucket name, ARN, and region

## Expected Cost
S3 buckets are free; you only pay for storage and requests. An empty bucket costs nothing.

## Common Issues

**Issue**: Bucket name already exists
**Solution**: The random_id resource ensures uniqueness, but if it fails, just run `terraform destroy` and `terraform apply` again.

**Issue**: AccessDenied error
**Solution**: Ensure your AWS credentials are configured correctly with `aws configure`.

## Next Steps
Try modifying the example:
- Change the region in the provider block
- Add more tags
- Create multiple buckets
