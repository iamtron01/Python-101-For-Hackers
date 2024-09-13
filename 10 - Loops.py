a = 1
while a < 5:
    a += 1
    print(a)

print('---')

for number in [0, 1, 2, 3, 4]:
    print(number+1)

print('---')

for number in range(5):
    print(number)

print('---')

for number in range(3):
    for y in range(3):
        print(number, y)

print('---')

for number in range(5):
    if number == 2:
        break
    print(number)

print('---')

for number in range(5):
    if number == 2:
        continue
    print(number)

print('---')

for number in range(5):
    if number == 2:
        pass
    print(number)

print('---')

for c in "string":
    print(c)

for key, value in {'a': 1, 'b': 2}.items():
    print(key, value)