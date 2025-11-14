def my_function():   # defining a function
    print("This is a function in functions.py")   # function body

my_function()    # calling the function
# you must call a function after defining it

def salutation():
    hello= "Good afternoon Vinnn"
    print(hello)

salutation()    # calling the function

def salute(name):   # defining a function with parameter
    print(f'Good afternoon {name}')   # using f-string for formatting

salute("Vinnn")   # passing argument to the function
salute("Alice")   # passing another argument to the function
salute("Bob")     # passing another argument to the function

def student(name,age,gender):   # defining a function with multiple parameters
    print(f'My name is: {name}, I am {gender} of {age} years old ')  # using f-string for formatting

student("Vinnn", 24, 'Male')  # passing arguments to the function

def multi(a,b,c):
    result = a*b*c
    return result  # returning the result
print(multi(2,3,4) ) # calling the function and printing the returned value


def age_calculator(current_age):
    new_age = current_age +9
    return new_age

print(age_calculator(24))  # calling the function and printing the returned value

# write a funtion that calculates a persons BMI and gives back
# the response to the person whether they are obese or underweight
# basing on the BMI

def bmi_calculator(weight, height):
    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"
    
print(bmi_calculator(74, 1.72))  # calling the function and printing the returned value