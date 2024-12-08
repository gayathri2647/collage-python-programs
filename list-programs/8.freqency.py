#to find the frequency of elements in given list
list = [6, 3, 98, 24, 3, 5, 74, 1, 5, 6, 3]

print("Given list :",list)

# Calculate the frequency of each element
freq_dict = {}
for element in list:
    if element in freq_dict:
        freq_dict[element] += 1
    else:
        freq_dict[element] = 1

print("Frequency of each element:", freq_dict)