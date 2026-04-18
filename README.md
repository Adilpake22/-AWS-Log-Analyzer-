# AWS Log Analyzer 🚀

## Overview
Serverless log monitoring system using AWS Lambda, CloudWatch, and SNS.

## Features
- Real-time log monitoring
- Error detection (ERROR, Exception, HTTP 500)
- Email/SMS alerts via SNS
- Event-driven architecture

## Tech Stack
- AWS Lambda (Python)
- CloudWatch Logs
- Amazon SNS
- IAM

## Architecture
CloudWatch Logs → Lambda → SNS → Email Alert

## Setup Steps

1. Create SNS Topic and subscribe email
2. Deploy Lambda function
3. Attach IAM role (CloudWatch + SNS permissions)
4. Add CloudWatch subscription filter
5. Test using log generator script

## Future Enhancements
- Slack integration
- Dashboard with CloudWatch metrics
- Kinesis streaming support

## Resume Impact
Built a serverless AWS log monitoring system that detects errors in real-time and sends alerts, demonstrating cloud automation and DevOps skills.