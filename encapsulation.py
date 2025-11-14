# what is encapsulation? 
# It refers to the bundling of data (attributes) and methods (functions) that operate on that
# data within a single unit or class. It restricts direct access to some of an object's components,

class Student:
    def __init__(self, name, grade):  # constructor with parameters
        self.__name = name   # private instance variable
        self.__grade = grade     # private instance variable
        

    # Getter method for name
    def get_name(self):
        return self.__name
    
    def get_grade(self):
        return self.__grade

    # Setter method for name
    def set_grade(self , grade):
        if grade >= 0 and grade <= 100:
            self.__grade = grade
        else:
            print("Invalid grade. Please enter a grade between 0 and 100.")
# which is a means of preventing unintended interference and misuse of the methods and data.

student1= Student("Alice", 85)  # creating an object of Student class
print(student1.get_name())  # accessing private variable using getter method
print(student1.get_grade())  # accessing private variable using getter method
student1.set_grade(95)  # modifying private variable using setter method
print(student1.get_grade())  # accessing modified private variable using getter method
# which is a means of preventing unintended interference and misuse of the methods and data.self.__name = name


    