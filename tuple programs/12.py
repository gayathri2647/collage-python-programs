tup = (0, 1, 2, 3, 4, 3, 5)

print("Tuple before removing : ",tup)

tup = list(tup)

num = int(input("Enter an index number to remove :"))

tup.remove(num)

tup = tuple(tup)

print("Tuple after removing an element:", tup)