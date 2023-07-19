import sys

if len(sys.argv) != 2:
    print("Usage: python hello.py <your_name>")
else:
    print("Hello,", sys.argv[1])
