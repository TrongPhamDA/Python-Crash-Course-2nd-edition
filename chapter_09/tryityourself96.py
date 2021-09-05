# 9-6. Ice Cream Stand: An ice cream stand is a specific
# kind of restaurant. Write a class called IceCreamStand
# that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 167).
# Either version of the class will work; just pick the
# one you like better. Add an attribute called flavors
# that stores a list of ice cream flavors. Write a
# method that displays these flavors. Create an instance
# of IceCreamStand, and call this method.

print("\nEx 9.6 Ice Cream Stand\n" + "-"*70)

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Cuisine: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"\n{self.restaurant_name} is open.")

# Child Class "IceCreamStand"
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)

        # Add an attribute called flavors that stores a list of ice cream flavors
        self.flavors = ["Vanilla",
                        "Chocolate",
                        "Cookies N' Cream",
                        "Mint Chocolate Chip",
                        "Chocolate Chip Cookie Dough",
                        "Buttered Pecan",
                        "Cookie Dough",
                        "Strawberry",
                        "Moose Tracks", 
                        "Neapolitan"]
    # Write a method that displays these flavors
    def displays_flavors(self):
        print(f"\n{self.restaurant_name} have the following ice cream flavors:")
        for flavor in sorted(self.flavors):
            print(f"\t- {flavor}")

# Instance of IceCreamStand() class
my_BR = IceCreamStand("Baskin Robbins", "Ice Cream")
my_BR.describe_restaurant()

# Call display_flavors() method
my_BR.displays_flavors()