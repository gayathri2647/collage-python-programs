# Aim : to find the given number is divisible by another number.

no = int(input("Enter a number : "))

ans = []

for i in range(2, no):
    if no % i == 0:
        ans.append(i)

if ans:  #if there is a no. that can divide the given number then print the divisors
    print(ans)
else:    #if there is no. number that can divide the given no. then its a prime no.
    print("Given is a prime number.")