# 9-8. Privileges: Write a separate Privileges class.
# The class should have one attribute, privileges, that
# stores a list of strings as described in Exercise 9-7.
# Move the show_privileges() method to this class. Make
# a Privileges instance as an attribute in the Admin
# class. Create a new instance of Admin and use your
# method to show its privileges.

print("\nEx 9.8 Privileges\n" + "-"*70)

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

# Write a separate Privileges() class
class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    # lists privileges
    def show_privileges(self):
        print(f"\nPrivileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

# Child class of User() class
class Admin(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        
        # call Privileges() class, assign to privileges attribute
        self.privileges = Privileges()

# Create an instance of Admin
admin_1 = Admin("Trọng", "Phạm", "Nam")
admin_1.greet_user()

# Call show_privileges() method
admin_1.privileges.show_privileges()
