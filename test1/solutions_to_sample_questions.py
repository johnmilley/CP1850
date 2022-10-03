# 1. false, true, false

# 2

grade_int = int(input("Enter grade: "))

if not (grade_int < 1 or grade_int > 100):
    print(grade_int)
else:
    print("Please enter a valid integers between 1–100")


# 3

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


# 4

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


# 5

import time

for i in range(10, 0, -1):
    print(f"{i}")
    time.sleep(1)

print("🚀 BLASTOFF!")


# 6

name = input("Enter your first name: ")
print('* ', end="")
for letter in name:
    print(f'{letter} * ', end="")

# 7

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