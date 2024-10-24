#7.Triangle Type Checker
# Ask the user for the lengths of the three sides of the triangle
side1 = float(input("Enter the length of the first side: "))
side2 = float(input("Enter the length of the second side: "))
side3 = float(input("Enter the length of the third side: "))

# Determine the type of triangle based on the sides
if side1 == side2 == side3:
    print("The triangle is Equilateral (all sides are equal).")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("The triangle is Isosceles (two sides are equal).")
else:
    print("The triangle is Scalene (all sides are different).")

## Ask the user to enter a number between 1 and 7
day_number = int(input("Enter a number (1 to 7): "))
