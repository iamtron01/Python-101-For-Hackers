import re

test = input()
print(test)

test = input("Enter a number: ")
print(test)

while True:
    ip = input("Enter an IP address: ")
    if re.match(r'^(\d{1,3}\.){3}\d{1,3}$', ip):
        print(">>> {}".format(ip))
    else:
        print("Invalid IPv4 address")
        break
    