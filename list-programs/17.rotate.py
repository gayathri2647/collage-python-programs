# Input list and rotation value

list = [1, 2, 3, 4, 5]
print("Original list:", list)

n = int(input("Enter no. of places to be rotated :"))
# Rotate the list
for _ in range(n):
    list.insert(0, list.pop())

print("Rotated list:", list)