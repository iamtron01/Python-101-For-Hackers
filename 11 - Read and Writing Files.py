file = open('00-things.txt')
print(file)

file = open('00-things.txt', 'rt')
print(file)

print(file.read())
file.seek(0)
print(file.readlines())

file.seek(0)
for line in file:
    print(line.strip())
file.close()

print("---")

file = open("test.txt", "w")
file.write("Hello, World!")
file.close()

file = open("test.txt", "a")
file.write("Bonjour, Monde!")
file.close()

with open("00-things.txt") as file:
    print(file.read())
    print("with will close the file automatically")