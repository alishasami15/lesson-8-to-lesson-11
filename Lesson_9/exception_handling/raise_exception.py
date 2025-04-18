# raise_exception.py

age = int(input("Enter your age: "))
if age < 18:
    raise ValueError("❌ You must be at least 18 years old.")
else:
    print("✅ Access granted")