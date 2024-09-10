def f(x):
    return x + 1

def g(x):
    return x + 2

x = f(g(1))
print(x)

def compose(f, g):
    return lambda x: f(g(x))

h = compose(f, g)
x = h(1)
print(x)

def o(*functions):
    def composed_function(x):
        result = x
        for f in functions:
            result = f(result)
        return result
    return composed_function

g = o(
    lambda x: x * 3,
    lambda x: x * 2)
print(g(2))

def f(x, *xs):
    print("{} {}".format(
        x, " ".join([x for x in xs ])))
f("hi", "bye", "cya")

def map(func, iterable):
    return [func(item) for item in iterable]

from itertools import chain

def bind(func, iterable):
    return list(chain.from_iterable(map(func, iterable)))
print(bind(lambda x: x, [[1,2,3],[4,5,6]]))

def dictionary(**kvargs):
    for key, value in kvargs.items():
        print("{}: {}".format(key, value))
dictionary(a=1, b=2, c=3)