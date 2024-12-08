list = [5, 10, 15, 20, 25, 50, 20]

print("Actual list : ",list)

# Check if 20 is in the list
if 20 in list:
    index = list.index(20)
    list[index] = 200

print("Updated list:", list)