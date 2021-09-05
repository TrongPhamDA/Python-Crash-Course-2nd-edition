# 8-13. User Profile: Start with a copy of
# user_profile.py from page 149. Build a profile of
# yourself by calling build_profile(), using your firs
# and last names and three other key-value pairs
# that describe you
print("\nEx 8.13 User Profile\n" + "-"*70)
def build_profile(first_name, last_name, **user_info):
    user_info['first_name'] = first_name.title()
    user_info['last_name'] = last_name.title()
    return user_info

my_profile = build_profile(last_name = 'pham', first_name = 'trong', location = 'Ninh Thuan', age = 29)
print(my_profile)
