import logging
import time
import random

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

messages = [
    "User login successful",
    "Database connected",
    "ERROR: Database connection failed",
    "WARNING: Disk usage high",
    "Exception: Null pointer error",
    "HTTP 500 Internal Server Error",
    "Request processed successfully"
]

while True:
    msg = random.choice(messages)
    if "ERROR" in msg or "Exception" in msg:
        logging.error(msg)
    elif "WARNING" in msg:
        logging.warning(msg)
    else:
        logging.info(msg)

    time.sleep(2)