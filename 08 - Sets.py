letters = {'a', 'b', 'c', 'd'}
print(letters)
print('a' in letters)

numbers = {1, 2, 3, 4}
print(numbers)
print(len(numbers))

print(letters.union(numbers))
print(letters.intersection(numbers))

numbers.remove(1)
print(numbers)