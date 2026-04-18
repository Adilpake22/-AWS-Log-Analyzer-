import json
import re
import boto3
import base64
import gzip
from datetime import datetime

sns = boto3.client('sns')

SNS_TOPIC_ARN = "REPLACE_WITH_YOUR_SNS_TOPIC_ARN"

ERROR_PATTERNS = [
    r'ERROR',
    r'Exception',
    r'FAIL',
    r'CRITICAL',
    r'HTTP 5\d{2}'
]

def lambda_handler(event, context):
    try:
        compressed_payload = base64.b64decode(event['awslogs']['data'])
        uncompressed_payload = gzip.decompress(compressed_payload)
        logs_data = json.loads(uncompressed_payload)

        alerts = []

        for log_event in logs_data['logEvents']:
            message = log_event['message']

            for pattern in ERROR_PATTERNS:
                if re.search(pattern, message, re.IGNORECASE):
                    alerts.append({
                        "timestamp": log_event['timestamp'],
                        "message": message,
                        "pattern": pattern
                    })
                    break

        if alerts:
            formatted_message = format_alert(alerts)
            send_alert(formatted_message)

        return {"status": "processed", "alerts_found": len(alerts)}

    except Exception as e:
        print(f"Error processing logs: {str(e)}")
        raise e


def format_alert(alerts):
    output = "🚨 AWS LOG ALERT 🚨\n\n"
    for alert in alerts:
        time = datetime.fromtimestamp(alert['timestamp']/1000)
        output += f"[{time}] Pattern: {alert['pattern']}\n"
        output += f"Message: {alert['message']}\n\n"
    return output


def send_alert(message):
    response = sns.publish(
        TopicArn=SNS_TOPIC_ARN,
        Subject="AWS Log Analyzer Alert",
        Message=message
    )
    print("Alert sent:", response)