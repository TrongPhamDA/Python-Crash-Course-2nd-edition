# 9-1. Restaurant: Make a class called Restaurant.
# The __init__() method for Restaurant should store
# two attributes: a restaurant_name and a cuisine_type.
# Make a method called describe_restaurant() that prints
# these two pieces of information, and a method called
# open_restaurant() that prints a message indicating
# that the restaurant is open. Make an instance called
# restaurant from your class. Print the two attributes
# individually, and then call both methods.

print("\nEx 9.1 Restaurant\n" + "-"*70)

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Cuisine: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.")

res_1 = Restaurant("Lang Nuong Nam Bo", "Grill & Beer")
res_1.describe_restaurant()
res_1.open_restaurant()