list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]
# Finding common elements

print("List 1 :",list_1)
print("List 2 :",list_2)
common= []

for item in list_1:
    if item in list_2:
        common.append(item)


print("Common elements:", common)