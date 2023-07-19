import sys

user_name = "Luis"

if len(sys.argv) == 2:
    user_name = sys.argv[1]

print("Hello,", user_name)
