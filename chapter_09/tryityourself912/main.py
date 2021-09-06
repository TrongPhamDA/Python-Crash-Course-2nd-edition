# Using Ex 9.11
# Import Admin class only
from admin import Admin as Ad

# Create an instance of Admin
admin_user = Ad("Trọng", "Phạm", "Nam")
admin_user.greet_user()
admin_user.describe_user()

admin_user.privileges.show_privileges()