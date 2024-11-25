#Input
year = int(input("Enter a year: "))

#check if the year is a leap year
'''
A year is a leap year if:
    It is divisible by 4, and
    It is not divisible by 100, unless it is also divisible by 400
'''
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
