# multiple_except.py

try:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    print(a / b)
except ZeroDivisionError:
    print("❌ Division by zero")
except ValueError:
    print("❌ Please enter valid numbers only")