from restaurant import Restaurant as res

my_res = res("Lang Nuong Nam Bo", "Grill & Beer")
my_res.describe_restaurant()
my_res.open_restaurant()


my_res.set_number_served(10)
print(f"Number served: {my_res.number_served}")

for i in range(5):
	my_res.increment_number_served(2)
	print(f"Number served: {my_res.number_served}")