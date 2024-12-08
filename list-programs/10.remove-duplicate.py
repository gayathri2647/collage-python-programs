list = [6, 3, 98, 24, 3, 5, 74, 1, 5, 6, 3]
#remove duplicates

print("Given list :",list)
list1 = []
for item in list:
    if item not in list1:
        list1.append(item)

print("Duplicates removed List:",list1)