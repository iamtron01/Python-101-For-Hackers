add = lambda x, y: x + y
print(add(5, 3))

blocks = lambda x,y: [x[i:i+y] 
            for i in range(0, len(x), y)]
print(blocks("string",2))

to_ord = lambda x: [ord(c) for c in x]
print(to_ord("abc"))