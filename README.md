# progen-erp-service
This stack holds the functionality of ProGen ERP flows
 
## EC2 retirement notes
1. Remove terraform/ec2.tf - EC2 instance will be terminated.
2. Remove terraform/role.tf - IAM role used by EC2 instance will be removed.
3. Remove terraform/load_balancer/ec2.tf - ALB target group used by EC2 instance will be removed.
4. In terraform/secrets.tf update role_arn in postgresql_credentials (line 38) - replace `aws_iam_role.instance_iam_role.arn` with `module.container_platform.service_role_arn` - this secret will be accessible by ECS role.