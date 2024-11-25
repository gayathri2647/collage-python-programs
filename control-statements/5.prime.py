# Input: Number to check
num = int(input("Enter a number: "))

# A prime number is greater than 1 and divisible only by 1 and itself
if num > 1:
    for i in range(2, int(num/2)):
        if num % i == 0:
            print(num,"is not a prime number.")
            break
    else:
        print(num,"is a prime number.")
else:
    print(num,"is not a prime number.")
