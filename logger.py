import csv
from datetime import datetime
import os

LOG_FILE = "logs.csv"

def log_transaction(item_name, price, status):
    """Log a vending transaction to logs.csv"""
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)

        #Writer header if file is new
        if not file_exists:
            writer.writerow(["timestamp", "item_name", "price", "status"])

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([timestamp, item_name, price, status])
        print(f"[LOGGED] {timestamp} - {item_name} - {price} IRR - {status}")