# 9-2. Three Restaurants: Start with your class from
# Exercise 9-1. Create three different instances from
# the class, and call describe_restaurant() for each
# instance.

print("\nEx 9.2 Three restaurant\n" + "-"*70)

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Cuisine: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

res_1 = Restaurant("Làng Nướng Nam Bộ", "Grill & Beer")
res_2 = Restaurant("Sushi Nhí", "Sushi")
res_3 = Restaurant("Lẩu Tươi MK", "Hot Pot")

res_1.describe_restaurant()
res_2.describe_restaurant()
res_3.describe_restaurant()