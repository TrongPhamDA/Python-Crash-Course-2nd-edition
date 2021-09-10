# try it yourself 11.3

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name    = first_name
        self.last_name     = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_amount=None):
        if raise_amount:
            self.annual_salary += raise_amount
        else:
            self.annual_salary += 5000