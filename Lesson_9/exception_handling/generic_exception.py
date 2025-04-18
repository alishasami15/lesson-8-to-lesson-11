# generic_exception.py

try:
    x = int("abc")
except Exception as e:
    print("❌ Error occurred:", e)