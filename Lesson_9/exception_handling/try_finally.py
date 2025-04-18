# try_finally.py

try:
    print("Opening file...")
    f = open("sample.txt", "r")
    print(f.read())
except FileNotFoundError:
    print("❌ File not found!")
finally:
    print("✅ File access attempt finished")