# 1. false, true, false

# 2: Write a program that gets a user to enter a grade from 1-100. The program should display an error message to the user if the number is not in that range.

grade_int = int(input("Enter grade: "))

if not (grade_int < 1 or grade_int > 100):
    print(grade_int)
else:
    print("Please enter a valid integers between 1–100")


# 3: Modify the program in question 2 to convert an integer grade to a letter (see question document)

grade = int(input("Enter grade: "))

if grade >= 1 and grade <= 100:
    if grade > 80:
        print("A")
    elif grade > 70:
        print("B")
    elif grade > 60:
        print("C")
    elif grade > 50:
        print("D")
    else:
        print("F")
else:
    print("Please enter a valid integers between 1-100")


# 4: An hourly employee works for $14.75 per hour. The employee gets time and a half (1.5x the base rate of pay) for hours worked over 40.
# 	Write a program that accepts the number of hours worked as input and calculates the employee’s gross pay (before deductions).


HOURLY_RATE = 14.75 # constant
OVERTIME_RATE = HOURLY_RATE * 1.5

overtime_hours = 0
gross_pay = 0

hours_worked = int(input("Enter hours worked: "))

if hours_worked > 40:
    overtime = hours_worked - 40
    gross_pay = ((hours_worked - overtime) * HOURLY_RATE) + (overtime * OVERTIME_RATE)
else:
    gross_pay = hours_worked * HOURLY_RATE

print(f"Gross pay: ${round(gross_pay, 2)}")


# 5: Print the numbers 10 - 1, descending by 1 each time. Print BLASTOFF! after 1.

import time

for i in range(10, 0, -1):
    print(f"{i}")
    time.sleep(1)

print("🚀 BLASTOFF!")


# 6: Enter your name as input and print with asterisks on either end and between each letter as in the sample below.
# * S * n * u * f * f * l * e * u * p * a * g * u * s *

name = input("Enter your first name: ")
print('* ', end="")
for letter in name:
    print(f'{letter} * ', end="")

# 7: Write program that asks a user to guess a number from 1 - 10. Keep the user guessing until your secret number is guessed correctly.

secret_number = 7
guessed = False

while not guessed:
    guess = int(input("\nGuess a number from 1 - 10: "))
    
    if guess < 1 or guess > 10:
        print("\n👎 Please enter a valid number.\n")
    else:
        if guess == secret_number:
            guessed = True
            print(f"\n👍 You did it!")
        else:
            print("\nTry again.")

print("\nThanks for playing! 👋")