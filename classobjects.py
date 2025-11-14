#  classobjects.py
class Employee:
    def __init__(self, name, gender, marital_status, residence):  # constructor with parameters
        self.name = name   # instance variable
        self.gender = gender   # instance variable
        self.marital_status = marital_status   # instance variable
        self.residence = residence   # instance variable

employee1 = Employee("Alice", "Female", "Single", "Nairobi")  # creating an object of Employee class
employee2 = Employee("Joseph", "Male", "Married", "Mombasa")  # creating another object of Employee class
employee3 = Employee("Esther","Female", "Divorced","Nakuru")  # creating another object of Employee class
print(employee1.marital_status)  
print(employee2.gender)  
print(employee3.name)

class Developer(Employee):  # child class inheriting from Employee class
    def __init__(self,name,gender,marital_status,residence,proc_lang):  # constructor with parameters
        super().__init__(name,gender,marital_status,residence)  # calling parent class constructor
        self.proc_lang = proc_lang  # instance variable

class CommissionedEmployees(Employee):  # child class inheriting from Employee class
    def __init__(self, name, gender, marital_status, residence, amount_sold):   # constructor with parameters
        super().__init__(name, gender, marital_status, residence)   # calling parent class constructor
        self.amount_sold = amount_sold  # instance variable
    def total_salary(self):     # method to calculate total salary
        total = (self.amount_sold*0.3) + 10000  # calculating total salary
        return total  # returning total salary
CommissionedEmployee1 = CommissionedEmployees("Mark","Male","Married","Kisumu",20000)  # creating an object of CommissionedEmployees classCommissionedEmployee1.total_salary()  # calling total_salary method
print(CommissionedEmployee1.total_salary())
