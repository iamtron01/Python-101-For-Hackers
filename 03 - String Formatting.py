string4 = "I\" a string"
print(string4)

string5 = "I'm a string"
print(string5)

string6 = "\x41"
print(string6)

string7 = "a" * 5
print(string7)

print("string" in string7)
print(string4.startswith("I"))

print(string4.index("string"))

string6 = "I'm a string"
print(string6.rjust(20, "*"))

print("string4 is {} characters long".format(len(string4)))
print("{} {} {}".format(len(string4), 4.0, 0x12))
print("{0} {2} {1}".format(len(string4), 4.0, 0x12))

length = len(string4)
print(f"string4 is {length} characters long")
print(f"string4 is {length:.2f} characters long")
print("string4 is {length:.2f} characters long".format(length=length))

print(f"string4 is {length:x} characters long")
print(f"string4 is {length:b} characters long")
print(f"string4 is {length:o} characters long")

print("string4 is %d characters long" % len(string4))
print("string4 is %f characters long" % len(string4))
print("string4 is %x characters long" % len(string4))