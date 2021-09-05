# 9-3. Users: Make a class called User. Create two
# attributes called first_name and last_name, and
# then create several other attributes that are typically
# stored in a user profile. Make a method called
# describe_user() that prints a summary of the user’s
# information. Make another method called greet_user()
# that prints a personalized greeting to the user.
# Create several instances representing different users,
# and call both methods for each user.

print("\nEx 9.3 Users\n" + "-"*70)

class User:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender
        
    def describe_user(self):
        print(f"Full name: {self.first_name}, {self.last_name}")
        print(f"Gender   : {self.gender}\n")

    def greet_user(self):
        print(f"Welcome you back, {self.first_name}!")

user_1 = User("Trọng", "Phạm", "Nam")
user_2 = User("Phúc", "Phạm", "Nam")
user_3 = User("Duyên", "Huỳnh", "Nữ")

user_1.greet_user()
user_1.describe_user()

user_2.greet_user()
user_2.describe_user()

user_3.greet_user()
user_3.describe_user()