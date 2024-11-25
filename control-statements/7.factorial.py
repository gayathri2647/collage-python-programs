#input
num = int(input("Enter a number : "))
#inizilation
fact = 1
#looping
for i in range(1,num + 1):
    fact = i * fact
#output
print("The factorial of",num,"is",fact)