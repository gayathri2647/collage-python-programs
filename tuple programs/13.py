tup1 = (1, 2, 3, 4)
tup2 = (3, 4, 5, 6)

print("Tuple 1 : ",tup1)
print("Tuple 2 : ",tup2)

common = tuple(set(tup1) & set(tup2))

print("Common elements:", common)