# break.py
# This module demonstrates the use of the 'break' statement in Python.
# It iterates through a list of numbers and stops when it finds a specific value.
numbers = [1, 3, 5, 7, 9, 11, 13, 15]
target = 9
for number in numbers:
    if number == target:
        print(f"Found the target number: {number}")
        break