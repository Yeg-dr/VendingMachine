import RPi.GPIO as GPIO
import time

# پین‌هایی که رله‌ها به اون‌ها وصل شدن
ROW_PIN = 17 # پین کنترل ردیف (مثلاً رله مربوط به ردیف‌ها)
COL_PIN = 27 # پین کنترل ستون (مثلاً رله مربوط به ستون‌ها)

#  تنظیم اولیه GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(ROW_PIN, GPIO.OUT)
GPIO.setup(COL_PIN, GPIO.OUT)

# اطمینان از خاموش بودن رله‌ها در شروع
GPIO.output(ROW_PIN, GPIO.LOW)
GPIO.output(COL_PIN, GPIO.LOW)

def activate_item(row=ROW_PIN, col=COL_PIN, duration=1.5):
    """
    فعال‌سازی آیتم با روشن کردن دو رله به مدت مشخص
    :param row: پین GPIO برای ردیف
    :param col: پین GPIO برای ستون
    :param duration: مدت زمان فعال بودن رله‌ها (به ثانیه)
    """
    print("[RELAY] Activating item...")
    GPIO.output(row, GPIO.HIGH)
    GPIO.output(col, GPIO.HIGH)
    time.sleep(duration)
    GPIO.output(row, GPIO.LOW)
    GPIO.output(col, GPIO.LOW)
    print("[RELAY] Done.")

def cleanup():
    """خاموش‌سازی GPIO بعد از اتمام کار"""
    GPIO.cleanup()

if __name__ == "__main__":
    try:
        activate_item()
    finally:
        cleanup()