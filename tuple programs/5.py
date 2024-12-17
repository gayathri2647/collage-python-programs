tup = (10, 20, 30, 40, 50)

print("Given tuple :",tup)

num = int(input("Enter a element to check : "))

if num in tup:
    print(f"{num} present in tuple.")
else:
    print(f"{num} is not in the tuple.")