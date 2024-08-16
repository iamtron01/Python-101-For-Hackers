x = 3
if x == 3:
    print('x is 3')
else:
    print('x is ¬3')

y = 5
if y != 6:
    print('y is ¬6')

def f(x):
    return x > 5
if not f(3):
    print('3 is <= 5')

if 1 < 1:
    print('1 < 1')
elif 1 <= 1:
    print('1 is <= 1')

if 0 < 1: print("0 < 1")
print("1 >= 1" if 1 >= 1 else "1 < 1")

