# Using Ex 9.8
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


class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(f"\nPrivileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")


class Admin(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.privileges = Privileges()