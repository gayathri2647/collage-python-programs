#input
num = int(input("Enter a number: "))
# Range for the multiplication table
start = int(input("Enter the starting range: "))
end = int(input("Enter the ending range: "))

# Loop to print the multiplication table within the range
print(f"Multiplication Table for {num} from {start} to {end}:")
for i in range(start, end + 1):
    print(num,"x",i,"=",num * i)
