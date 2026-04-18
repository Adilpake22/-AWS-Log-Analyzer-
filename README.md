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

### 🏆 Screenshots:
## CloudWatch Dashboard
<img width="1919" height="911" alt="Screenshot 2026-04-19 010812" src="https://github.com/user-attachments/assets/b0756070-50cc-426c-a5d0-cdf562245a2d" />
<img width="1916" height="845" alt="Screenshot 2026-04-19 010634" src="https://github.com/user-attachments/assets/6b91220b-4b34-48e6-8542-66049e57cc80" />
<img width="1913" height="838" alt="Screenshot 2026-04-19 011000" src="https://github.com/user-attachments/assets/40e576c5-576b-40e8-8b41-be1737b6ecaa" />

## Lambda
<img width="1914" height="854" alt="Screenshot 2026-04-19 011205" src="https://github.com/user-attachments/assets/1621fa54-fd03-4b19-8c5c-89d92eb7252e" />
<img width="1919" height="845" alt="Screenshot 2026-04-19 011312" src="https://github.com/user-attachments/assets/f0350742-52bf-4557-a39f-53b6c684011f" />
<img width="1917" height="848" alt="Screenshot 2026-04-19 011413" src="https://github.com/user-attachments/assets/c1235381-3b30-440e-ab6c-47b08b9db102" />

## SNS-Email
<img width="1919" height="901" alt="Screenshot 2026-04-19 011642" src="https://github.com/user-attachments/assets/7c421e57-0a6b-4753-8c45-82605f6e646c" />








## 👨‍💻 Author

Aditya Dilpake
GitHub: https://github.com/Adilpake22/

---

## ⭐ If you found this project useful, consider giving it a star!
