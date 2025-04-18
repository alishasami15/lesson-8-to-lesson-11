# try_else.py

try:
    value = int(input("Enter a number: "))
except ValueError:
    print("❌ Invalid number!")
else:
    print("You entered:", value)