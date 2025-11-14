print("Hello World!")

#variables
age =23
name = "Alice"

print(age)
print(name)

#Data Types
# 1. Integer
weight = 29
# 2. String
my_name = "Bob"
# 3. Float
height = 5.9
# 4. Boolean
is_student = True
is_graduated = False

# user input
last_name = input("Enter your last name: ")
print("Your last name is " + last_name)
weight1 = input("Please key in here your weight in kgs: ")
print("Your weight is " + weight1 + " kgs")

#concatenation
full_name = name + " " + last_name
print("Your full name is " + full_name)

#  type conversion
num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

sum = int(num1) + int(num2)
print(sum)
print("The sum is: " + str(sum))

marks1 = input("Enter marks for subject 1: ")
marks2 = input("Enter marks for subject 2: ")

total= int(marks1)+int(marks2)
print(total)


#calculate area of a circle
# radius is an input from user

import math
radius = float(input("Enter the radius of the circle: "))
area = math.pi * radius ** 2
print("The area of the circle is: " + str(area))