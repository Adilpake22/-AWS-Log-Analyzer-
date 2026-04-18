import json
import re
import boto3
import base64
import gzip
from datetime import datetime

# AWS clients
sns = boto3.client('sns', region_name='ap-south-1')
cw = boto3.client('cloudwatch', region_name='ap-south-1')

SNS_TOPIC_ARN = "arn:aws:sns:ap-south-1:943339979116:log-analyzer-topic"

ERROR_PATTERNS = [
    r'ERROR',
    r'Exception',
    r'FAIL',
    r'CRITICAL',
    r'HTTP 5\d{2}'
]

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event))

        alerts = []

        # ✅ Case 1: Direct test event
        if isinstance(event, dict) and "message" in event:
            message = event["message"]

            for pattern in ERROR_PATTERNS:
                if re.search(pattern, message, re.IGNORECASE):
                    alerts.append({
                        "timestamp": int(datetime.now().timestamp() * 1000),
                        "message": message,
                        "pattern": pattern
                    })
                    break

        # ✅ Case 2: CloudWatch Logs
        elif isinstance(event, dict) and "awslogs" in event:
            compressed_payload = base64.b64decode(event['awslogs']['data'])
            uncompressed_payload = gzip.decompress(compressed_payload)
            logs_data = json.loads(uncompressed_payload)

            for log_event in logs_data.get('logEvents', []):
                message = log_event.get('message', '')

                for pattern in ERROR_PATTERNS:
                    if re.search(pattern, message, re.IGNORECASE):
                        alerts.append({
                            "timestamp": log_event.get('timestamp', int(datetime.now().timestamp() * 1000)),
                            "message": message,
                            "pattern": pattern
                        })
                        break

        # ✅ If alerts found → send SNS + push metric
        if alerts:
            formatted_message = format_alert(alerts)
            send_alert(formatted_message)
            push_metric(len(alerts))

        return {
            "status": "processed",
            "alerts_found": len(alerts)
        }

    except Exception as e:
        print("Error:", str(e))
        raise e


# 🔔 Format message
def format_alert(alerts):
    output = "🚨 AWS LOG ALERT 🚨\n\n"
    for alert in alerts:
        time = datetime.fromtimestamp(alert['timestamp'] / 1000)
        output += f"[{time}] Pattern: {alert['pattern']}\n"
        output += f"Message: {alert['message']}\n\n"
    return output


# 📩 Send SNS alert
def send_alert(message):
    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="AWS Log Analyzer Alert",
        Message=message
    )
    print("Alert sent:", response)


# 📊 Push metric to CloudWatch
def push_metric(count):
    response = cw.put_metric_data(
        Namespace='LogAnalyzer',
        MetricData=[
            {
                'MetricName': 'ErrorCount',
                'Value': count,
                'Unit': 'Count'
            }
        ]
    )
    print("Metric sent:", response)