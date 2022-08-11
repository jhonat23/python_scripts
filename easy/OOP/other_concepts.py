"""Aggregation and composition examples"""

# Composition
class Salary():
    def __init__(self, pay):
        self.pay = pay

    def get_total_per_year(self):
        return self.pay * 12

class EmployeeA():
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.obj_salary = Salary(self.pay) #Salary instance that only exist if a Employee instance is created
    
    def annual_salary(self):
        return self.obj_salary.get_total_per_year() + self.bonus #method using a method from salary instance

#Implement
job = EmployeeA(10000, 100)
print(job.annual_salary())

#Aggregation (using the Salary class)----------------------------------------------------------------

class EmployeeB():
    def __init__(self, pay, bonus):
        """Pay must be a Salary instance"""
        self.pay = pay #this attribute can handle with a Salary instance
        self.bonus = bonus

    def annual_salary(self):
        return self.pay.get_total_per_year() + self.bonus #BUT, BE CAREFUL BECAUSE this method calls a Salary method

#Implement
myPay = Salary(10000)
myJob = EmployeeB(myPay, 100)
print(myJob.annual_salary())