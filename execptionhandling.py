# exception handling.py
# This module demonstrates basic exception handling in Python.
try:  # Attempt to divide by zero
    n=0
    result = 10 / n
except ZeroDivisionError:  # Catch the division by zero error
    print("Error: Cannot divide by zero.")
else:  # This block executes if no exception occurs
    print("Result:", result)
finally:  # This block always executes
    print("Execution completed.")