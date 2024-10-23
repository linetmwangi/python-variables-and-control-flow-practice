#2.Odd or Even Checker
# Ask the user for a number
number = int(input("Enter a number: "))

# Check if the number is even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

#3.Grade Categorizer
# Ask the user for a score
score = int(input("Enter your score (0-100): "))

# Determine the grade based on the score
if 90 <= score <= 100:
    grade = 'A'
elif 80 <= score < 90:
    grade = 'B'
elif 70 <= score < 80:
    grade = 'C'
elif 60 <= score < 70:
    grade = 'D'
elif 0 <= score < 60:
    grade = 'F'
else:
    grade = 'Invalid score'

# Output the result
if grade == 'Invalid score':
    print("Please enter a valid score between 0 and 100.")
else:
    print(f"Your grade is: {grade}")

#4.Simple Calculator with Conditionals
# Ask for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Ask for an operation
operation = input("Enter an operation (+, -, *, /): ")

# Perform the operation and display the result
if operation == '+':
    result = num1 + num2
    print(f"The result of {num1} + {num2} is {result}")
elif operation == '-':
    result = num1 - num2
    print(f"The result of {num1} - {num2} is {result}")
elif operation == '*':
    result = num1 * num2
    print(f"The result of {num1} * {num2} is {result}")
elif operation == '/':
    if num2 != 0:  # Avoid division by zero
        result = num1 / num2
        print(f"The result of {num1} / {num2} is {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")

#5.Simple Age Checker
# Ask the user for their age
age = int(input("Enter your age: "))

# Determine the category based on the age
if age < 18:
    print("You are a minor.")
elif 18 <= age <= 65:
    print("You are an adult.")
elif age > 65:
    print("You are a senior.")
else:
    print("Invalid age.")


#6. Password Validator
# Ask the user to enter a password
password = input("Enter the password: ")

# Check if the password is correct
if password == "emobilis123":
    print("Access granted.")
else:
    print("Access denied.")

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

#8.Determine and print the corresponding day of the week
if day_number == 1:
    print("Monday")
elif day_number == 2:
    print("Tuesday")
elif day_number == 3:
    print("Wednesday")
elif day_number == 4:
    print("Thursday")
elif day_number == 5:
    print("Friday")
elif day_number == 6:
    print("Saturday")
elif day_number == 7:
    print("Sunday")
else:
    print("Invalid input. Please enter a number between 1 and 7.")
