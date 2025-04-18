# read_file.py

f = open("sample.txt", "r")   # Open in read mode
content = f.read()            # Read entire content
print(content)
f.close()                     # Close file