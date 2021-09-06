# Using Ex 9.11
# Child class is Admin class

class User:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        
    def describe_user(self):
        print(f"Full name: {self.first_name}, {self.last_name}")
        print(f"Gender   : {self.gender}")

    def greet_user(self):
        print(f"\nWelcome you back, {self.first_name}!")