#input
start = int(input("Enter the start of the interval: "))
end = int(input("Enter the end of the interval: "))

print("Prime numbers between",start,"and", end,"are:")

#loop through each number in the interval
for num in range(start, end + 1):
    if num > 1:  #prime numbers are greater than 1
        for i in range(2, int(num/2)):
            if num % i == 0:
                break
        else:
            print(num, end=" ")
