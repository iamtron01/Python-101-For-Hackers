class Infix:
    def __init__(self, function):
        self.function = function

    def __ror__(self, other):
        return Infix(
            lambda x, self=self,
            other=other: self.function(other, x))

    def __or__(self, other):
        return self.function(other)

equals = Infix(lambda x, y: x == y)
not_equal = Infix(lambda x, y: x != y)

valid = True
not_valid = False

print(valid |equals| not_valid)
print(valid |not_equal| not_valid)

print(9 < 10)

print(10 > 9 and 10 < 11)
print(10 > 9 or 10 > 11)

x = 10
print(x)
x = x + 1
print(x)
x += 1
x -= 1
x *= 2
print(x)
x /= 2
print(x)

x = 13
#print(bin(x))
print("----")
print(bin(x)[2:].rjust(4, '0'))
y = 5
#print(bin(y))
print(bin(y)[2:].rjust(4, '0'))
print("----")

print(bin(x & y)[2:].rjust(4, '0'))
print(x & y)

print(bin(x | y)[2:].rjust(4, '0'))
print(x | y)

print(bin(x ^ y)[2:].rjust(4, '0'))

print("----")
print(bin(x >> 1)[2:].rjust(4, '0'))