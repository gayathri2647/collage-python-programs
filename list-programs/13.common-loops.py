list_1 = [1, 2, 3, 4, 5]
list_2 = [3, 4, 5, 6, 7]

print("List 1 :",list_1)
print("List 2 :",list_2)

common = list(set(list_1) & set(list_2))

print("Common elements:", common)