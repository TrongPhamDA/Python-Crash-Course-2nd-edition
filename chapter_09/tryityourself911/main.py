from user import User, Admin, Privileges

# Create an instance of Admin
admin_user = Admin("Trọng", "Phạm", "Nam")
admin_user.greet_user()
admin_user.describe_user()

admin_user.privileges.show_privileges()
