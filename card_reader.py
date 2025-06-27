import time
import random

def send_payment_request(amount):
    print(f"[CARD READER] Showing payment on card reader -> {amount} IRR ")
    time.sleep(1)
    success = random.choice([True, True, False])
    if success:
        print("[CARD READER] Payment successful!")
        return True
    else:
        print("[CARD READER] Payment failed.")
        return False