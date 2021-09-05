# 9-5. Login Attempts: Add an attribute called
# login_attempts to your User class from Exercise 9-3
# (page 162). Write a method called
# increment_login_attempts() that increments the value
# of login_attempts by 1. Write another method called
# reset_login_attempts() that resets the value of
# login_attempts to 0.

# Make an instance of the User class and call
# increment_login_attempts() several times. Print the value
# of login_attempts to make sure it was incremented
# properly, and then call reset_login_attempts(). Print
# login_attempts again to make sure it was reset to 0.

print("\nEx 9.5 Login Attempts\n" + "-"*70)

class User:
    def __init__(self, first_name, last_name, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.gender = gender

        # add an attribute called login_attempt
        self.login_attempts = 0
        
    def describe_user(self):
        print(f"Full name: {self.first_name}, {self.last_name}")
        print(f"Gender   : {self.gender}\n")

    def greet_user(self):
        print(f"Welcome you back, {self.first_name}!")

    # Increments the value of login_attempts by 1
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"login_attempts: {self.login_attempts}")

    # Resets the value of login_attempts to 0
    def reset_login_attempts(self):
        self.login_attempts = 0
        print(f"login_attempts: {self.login_attempts}")

user_1 = User("Trọng", "Phạm", "Nam")

user_1.greet_user()
user_1.describe_user()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()

user_1.increment_login_attempts()
user_1.increment_login_attempts()
user_1.reset_login_attempts()
