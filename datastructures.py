# List
employees = ["Alice", "Bob", "Charlie", "Diana"]
print(employees)
print (employees[2]) #accessing an element
employees[1] = "Robert" #modifying an element
print(employees)

# Tuple
student= ('Dennis', 'Jose', 'Victor', 'Maria')
print(student)
print(student[2]) #accessing an element
# student[2]= 'Victoria' #tuples are immutable and cannot be modified
# print(student)
# Set
fruits = {'apple', 'banana', 'orange', 'mango'}
print(fruits)
# does not have indexing, so cannot access elements by index
fruits.add('grape') #adding an element
print(fruits)

# Dictionary
person = {
    'name': 'Eve',
    'age': 28,
    'gender': 'Female',
}
print(person)
print(person['name']) #accessing an element

