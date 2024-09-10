from functools import reduce

list1 = [1,2,3,4,5]
list2 = [i**2 for i in list1]
list3 = [i**2 for i in[1,2,3,4,5]]
print(list3)

list4 = [x for x in range(10) if x % 2 == 0]
print(list4)

list5 = [hex(x) for x in range(10)]
print(list5)

list6 = [x for x in range(10) if x % 2 == 0 if x % 3 == 0]
print(list6)

list7 = [x if x % 2 == 0 else None for x in range(10)]
print(list7)

list8 = [x for x in range(5) if x == 0 or x == 1]
print(list8)

list9 = [[1,2,3],[4,5,6],[7,8,9]]   
list10 = [y for x in list9 for y in x]
print(list10)

list11 = [[1,2,3],[4,5,6],[7,8,9]]
list12 = reduce(lambda acc, x: acc + x, list11)
print(list12)

list13 = [c for c in "string"]
print(list13)

print("".join(list13))