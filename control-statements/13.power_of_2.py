# Display the powers of 2 using anonymous function

#terms = 10

# Uncomment code below to take input from the user
terms = int(input("Enter the power : "))

# use anonymous function

result = list(map(lambda x: 2 ** x, range(terms + 1)))

print(f"2 raised to power of {terms} is {result[-1]}")
