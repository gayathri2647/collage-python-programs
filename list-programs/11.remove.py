#to remove empty strings from the givn list 

list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

print("Given string :",list1)

list2 = list(filter(None,list1))
print(list2)