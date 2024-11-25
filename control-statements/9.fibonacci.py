# Input: Number of terms in the Fibonacci series
n = int(input("Enter the number of terms: "))

#initialize the first two terms
a, b = 0, 1

print("Fibonacci Series:")

for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
