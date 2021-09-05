#5.1 Conditional Tests
car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

#5.3 Alien Color #1
color = ('green', 'yellow', 'red')
#if true
alien_color = color[0]
if alien_color == 'green':
	print('+5 points')
#if false
alien_color=color[1]
if alien_color == 'green':
	print('+5 points')

#5.4 Alien Color #2
color = ('green', 'yellow', 'red')
#Do if block
alien_color = color[0]
if alien_color == 'green':
	print('+5 points')
else:
	print('+10 points')
#Do else block
alien_color2 = color[1]
if alien_color2 == 'green':
	print('+5 points')
else:
	print('+10 points')

#5.5 Alien Color #3
color = ('green', 'yellow', 'red')
for alien_color in color:
	if alien_color == 'green':
		score = 5
	elif alien_color == 'yellow':
		score = 10
	else:
		score = 15
	print(f'{alien_color} : +{score} points')

#5.6 Stages of Life
person = range(0,71,1)
for person_yo in person:
	if person_yo < 2: print(f'{person_yo} : a baby')
	elif person_yo < 4: print(f'{person_yo} : a toddler')
	elif person_yo < 13: print(f'{person_yo} : a kid')
	elif person_yo < 20: print(f'{person_yo} : a teenager')
	elif person_yo < 65: print(f'{person_yo} : an adult')
	else: print(f'{person_yo} : an elder')

#5.7 Favorite Fruit
your_fruits = ['banana', 'apple', 'orange', 'watermelon', 'grape']
favorite_fruits = ['apple','grape','banana']
for fruit in sorted(your_fruits):
	if fruit in favorite_fruits:
		print(f'You really like {fruit}!')

#5.8 Hello Admin
usernames = ['admin','trongpham','ngoctrong','trongda','phamtrong']
username = 'admin'
if username == 'admin':
	print('Hello admin, would you like to see a status report?')
else:
	print(f'Hello {username}, thank you for logging in again.')

#5.9 No Users
usernames = []
username = 'trongpham'
if usernames:
	if username == 'admin':
		print('Hello admin, would you like to see a status report?')
	else:
		print(f'Hello {username}, thank you for logging in again.')
else:
	print('We need to find some users!')

#5.10 Checking Usernames
current_users = ['admin','trongpham','NGOCTRONG','trongda','phamtrong']
new_users = ['NgocTrong','tronghocpython','trongquan2','TRONGda']
#convert to lowercase
current_users = [user.lower() for user in current_users]
new_users = [user.lower() for user in new_users]
#Checking
for user in new_users:
	if user in current_users:
		print(f'Username {user} already exists, enter a new username.')
	else:
		print(f'Username {user} is available')

#5.11 Ordinal Numbers
number_list = list(range(1,10,1))
ordinal_number = []
for number in number_list:
	if number == 1: ordinal = '1st'
	elif number == 2: ordinal = '2nd'
	elif number == 3: ordinal = '3rd'
	else: ordinal = f'{number}th'
	ordinal_number.append(ordinal)
print(number_list)
print(ordinal_number)