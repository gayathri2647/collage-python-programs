import math

# Input coefficients
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Ensure it is a quadratic equation
if a == 0:
    print("The coefficient 'a' cannot be zero for a quadratic equation.")
else:
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check discriminant and find roots
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print("Two distinct real roots: %.2f and %.2f" % (root1, root2))
    elif discriminant == 0:
        root = -b / (2 * a)
        print("One real root: %.2f" % root)
    else:
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        print("Two complex roots: %.2f + %.2fi and %.2f - %.2fi" % (real_part, imaginary_part, real_part, imaginary_part))