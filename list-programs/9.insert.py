#to insert the element in desired location 

list = [5, 10, 15, 200, 25, 50, 20]

print("The list :",list)

position = int(input("Enter the position: "))

a = int(input("Enter the element: "))

# Insert the element
list.insert(position, a)

print("List:", list)