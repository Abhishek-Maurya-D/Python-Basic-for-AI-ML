from abc import ABC, abstractmethod
class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass;

class Intern(Employee):
    def calculate_salary(self):
        print("My Salary is 50000");

class FullTimeEmployee(Employee):
    def calculate_salary(self):
        print("My Salary is 60000");

class ContractEmployee(Employee):
    def calculate_salary(self):
        print("My Salary is 70000");

inter1 = Intern();
inter1.calculate_salary();