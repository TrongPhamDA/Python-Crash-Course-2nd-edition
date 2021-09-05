# 9-7. Admin: An administrator is a special kind of user.
# Write a class called Admin that inherits from the User
# class you wrote in Exercise 9-3 (page 162) or Exercise
# 9-5 (page 167). Add an attribute, privileges, that
# stores a list of strings like "can add post", "can
# delete post", "can ban user", and so on. Write a
# method called show_privileges() that lists the
# administrator’s set of privileges. Create an instance
# of Admin, and call your method.

print("\nEx 9.7 Admin\n" + "-"*70)

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

# Child class of User() class
class Admin(User):
    def __init__(self, first_name, last_name, gender):
        super().__init__(first_name, last_name, gender)
        self.privileges = ["can add post", "can delete post", "can ban user"]

    # lists the admin privileges
    def show_privileges(self):
        print(f"\nAdministrator's privileges:")
        for privilege in self.privileges:
            print(f"\t- {privilege}")

# Create an instance of Admin
admin_1 = Admin("Trọng", "Phạm", "Nam")
admin_1.greet_user()

# Call show_privileges() method
admin_1.show_privileges()
