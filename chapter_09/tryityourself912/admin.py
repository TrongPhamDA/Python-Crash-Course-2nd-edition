# Using Ex 9.11
# Import parent class User()
from user import User

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