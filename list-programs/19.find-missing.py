# Continuous list with missing elements
continuous_list = [3, 4, 7, 8, 9, 11]

print("Given list :",continuous_list)
# Determine the start and end of the range
start = continuous_list[0]
end = continuous_list[-1]

full_range = set(range(start, end + 1))

#to find the missing elements
missing_elements = full_range - set(continuous_list)

# Convert to a sorted list and display the result
missing_elements = sorted(missing_elements)
print("The missing elements are:", missing_elements)
