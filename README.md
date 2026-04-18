# 🚀 AWS Log Analyzer & Alerting System

A serverless log monitoring system built using AWS that detects error patterns in logs, triggers alerts, and visualizes metrics in real time.

---

## 📌 Project Overview

This project automatically analyzes application logs, identifies critical issues such as errors or exceptions, and sends real-time alerts via email. It also tracks error trends using CloudWatch dashboards for better monitoring and observability.

---

## 🏗️ Architecture

```
CloudWatch Logs → Lambda → SNS → Email Alerts
                      ↓
              CloudWatch Metrics → Dashboard → Alarm
```

---

## ⚙️ Tech Stack

* AWS Lambda (Python)
* Amazon CloudWatch (Logs, Metrics, Dashboard)
* Amazon SNS (Email notifications)
* Boto3 (AWS SDK for Python)

---

## 🔥 Features

* Real-time log monitoring
* Pattern-based error detection (ERROR, Exception, FAIL, CRITICAL)
* Automatic email alerts using SNS
* Custom CloudWatch metrics (ErrorCount)
* Interactive dashboard with graphs
* Alarm triggering on threshold breach

---

## 🧠 How It Works

1. Logs are generated and stored in CloudWatch
2. Lambda function processes logs or test events
3. Error patterns are detected using regular expressions
4. If errors are found:

   * SNS sends an email alert
   * CloudWatch metric (ErrorCount) is updated
5. Dashboard visualizes error trends and triggers alarms

---

## 📊 Dashboard Insights

* Line graph showing error trends over time
* Bar and number widgets for quick analysis
* Alarm triggers when error count exceeds threshold

---

## 🛠️ Setup Instructions

### 1. Clone Repository

```bash
git clone https://github.com/your-username/aws-log-analyzer.git
cd aws-log-analyzer
```

---

### 2. Deploy Lambda Function

* Create a Lambda function (Python 3.11)
* Copy and paste the code from `lambda_function.py`
* Attach required IAM policies:

  * AWSLambdaBasicExecutionRole
  * AmazonSNSFullAccess
  * CloudWatchFullAccess

---

### 3. Create SNS Topic

* Create a topic: `log-analyzer-topic`
* Add an email subscription
* Confirm the subscription from your email

---

### 4. Configure CloudWatch Logs

* Create a log group (example: `test-log-group`)
* Create a log stream
* Add a subscription filter connecting the log group to Lambda

---

### 5. Create Dashboard

* Go to CloudWatch → Dashboards
* Create dashboard: `LogAnalyzerDashboard`
* Add a line graph widget
* Select:

  * Namespace: `LogAnalyzer`
  * Metric: `ErrorCount`

---

### 6. Create Alarm

* Go to CloudWatch → Alarms
* Create alarm on `ErrorCount`
* Set threshold:

  * Greater than or equal to 1
* Attach SNS topic for notifications

---

## 🧪 Test Event

Use this test payload in Lambda:

```json
{
  "message": "ERROR: Database connection failed"
}
```

---

## 📈 Expected Output

* Email alert received 📩
* Dashboard graph updated 📊
* Alarm triggered 🚨

---

## 📌 Future Enhancements

* Add support for multiple log levels (INFO, WARNING)
* Store logs in S3 for historical analysis
* Integrate Kinesis for real-time streaming
* Build a frontend dashboard using React

---

## 🏆 Resume Description

Built a serverless AWS log monitoring system using Lambda, CloudWatch, and SNS to detect errors, trigger alerts, and visualize metrics in real time.

---

## 👨‍💻 Author

Your Name
GitHub: https://github.com/your-username

---

## ⭐ If you found this project useful, consider giving it a star!
