# # #IF statement
# # requested_topping = "mushrooms"
# # if requested_topping != "anchovies":
# #     print("Hold the anchovies!")

# # #IF with a List
# # requested_toppings = ['mushrooms', 'onions', 'pineapple']
# # #Sử dụng từ khóa IN để kiểm tra (so sánh) có thuộc List không
# # check = 'mushrooms' in requested_toppings
# # print(check)
# # check = 'pepperoni' in requested_toppings
# # print(check)

# #IF with a List
# #Sử dụng từ khóa NOT IN để kiểm tra không thuộc List
# banned_users = ['andrew', 'carolina', 'david']
# user = 'marie'
# if user not in banned_users: print(f"{user.title()}, you can post a respone if you wish.")

# #Testing multiple conditions
# requested_toppings = ['mushrooms', 'extra cheese']
# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# if 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# if 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")
# print("\nFinished making your pizza!")


# #Checking for Special Items
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# #Checking for Special Items
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == 'green peppers':
#         print("Sorry, we are out of green peppers right now.")
#     else:
#         print(f"Adding {requested_topping}.")
# print("\nFinished making your pizza!")

# #Checking That a List Is Not Empty
# requested_toppings = []
# #Nếu List không bị rỗng
# if requested_toppings:
#     for requested_topping in requested_toppings:
#         print(f"Adding {requested_topping}.")
#         print("\nFinished making your pizza!")
# #Nếu List rỗng thiệt
# else:
#     print("Are you sure you want a plain pizza?")

#Using Multiple Lists
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:   
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping}.")
    else:
        print(f"Sorry, we don't have {requested_topping}.")
print("\nFinished making your pizza!")