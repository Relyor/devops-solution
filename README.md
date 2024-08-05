# Script Usage Guide

## Prerequisites

1. **Install Python 3**
   - The script has been tested with Python 3.8.10.

2. **Install Python Dependencies**
   - Use the following command to install the required dependencies:

     ```bash
     pip3 install -r requirements.txt
     ```

3. **Configure AWS Environment Variables**
   - Before running the script, export your AWS credentials and region:

     ```bash
     export AWS_ACCESS_KEY_ID='your_access_key_id'
     export AWS_SECRET_ACCESS_KEY='your_secret_access_key'
     export AWS_DEFAULT_REGION='your_region'
     ```

## Running the Script

To execute the script, use the following command:

```bash
python3 file_search.py <bucket_name> <substring>
```

## Answers

### Infrastructure as Code (IaC)

Infrastructure as Code, abbreviated as **IaC**, is a concept that allows programmers (typically DevOps, DevSecOps, Cloud Engineers, or Infrastructure Engineers) to create, provision, manage, and maintain cloud infrastructure using code. A few popular tools developed to support IaC include Terraform, OpenTofu, Pulumi, Ansible, and others. Utilizing IaC is paramount for enhancing automation, maintainability, and reusability of infrastructure within a company.

### Observability

**Observability** is the ability to monitor the behavior of microservices and the platform they run on. Microservices architecture involves many small, decoupled services that interact with each other. Using tools for logging, dashboards, alerts, traces, metrics, and events helps gain insights into how these services perform, how they interact, and where issues might arise. Observability is crucial for troubleshooting, performance monitoring, dependency tracking, error tracing, and managing the complexity of microservices architecture.

### Security

When assessing security in an AWS environment, here are the first things to check:

1. **Security Groups and NACLs**: Ensure that rules are restrictive and only allow necessary traffic.
2. **IAM (Policies and Roles)**: Ensure that only necessary users and roles exist and that they adhere to the principle of least privilege. Check attached policies to ensure they grant the minimum necessary permissions.
3. **S3 Bucket Policies**: Ensure they are not exposed publicly unless necessary.
4. **WAF (Web Application Firewall) Rules**: Review whitelisted/blacklisted IPs and rules to ensure appropriate access control.
