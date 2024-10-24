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