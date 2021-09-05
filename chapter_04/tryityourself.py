# #Count to 20
# for number in range(1,21): print(number)

# #One million
# numbers = list(range(1,1_000_001))
# for number in numbers: print(number)

# #Summing a [1..1 million]
# numbers = list(range(1,1_000_001))
# min_number = min(numbers)
# max_number = max(numbers)
# sum_numbers = sum(numbers)
# print(f"min: {min_number}\nmax: {max_number}\nsum: {sum_numbers}")

# #Odd Numbers
# odd_numbers = [number for number in range(1,20,2)]
# print(odd_numbers)

# #Three
# numbers= [number for number in range(3,31,3)]
# print(numbers)

# #10 first cubes
# cubes = [number**3 for number in range(1,11)]
# print(cubes)

# #Or
# cubes = []
# for number in range(1,11): cubes.append(number**3)
# print(cubes)

# #Slices
# mon_an = ['com', 'chao long', 'pho', 'bun bo', 'bun dau']
# print("\nThe first 3 mon_an:")
# for mon in mon_an[:3]:
# 	print(f"- {mon.title()}")

# print("\nThe middle 3 mon_an:")
# for mon in mon_an[1:4]:
# 	print(f"- {mon.title()}")

# print("\nThe last 3 mon_an:")
# for mon in mon_an[-3:]:
# 	print(f"- {mon.title()}")

# #My Pizzas, Your Pizzas
# my_pizzas = ['xuc xich', 'thit xong khoi', 'rau cu']
# friend_pizzas = my_pizzas[:]
# my_pizzas.append('dam bong')
# friend_pizzas.append('thanh cua')
# print('\nMy favorite Pizzas are:')
# for pizza in my_pizzas[:]: print(f"- {pizza.title()}")
# print("\nMy friend's favorite Pizzas are:")
# for pizza in friend_pizzas[:]: print(f"- {pizza.title()}")

#Buffet
foods = ["com suon tam", "bun bo", "bun dau", "pho", "bun thit nuong"]
print("\nBuffet Restaurant's menu:")
#sorted() để sắp xếp lại menu theo AZ
for food in sorted(foods): print(f"- {food.lower()}")
#Python rejects this change
#foods[0] = "cơm sườn tấm"
#change 2 items
foods = ("cơm sườn tấm", "bún bò", "bún đậu mắm tôm", "phở bò", "bún thịt nướng")
print("\nNew menu:")
for food in sorted(foods): print(f"- {food.title()}")