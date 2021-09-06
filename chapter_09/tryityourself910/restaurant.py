# Using tryityourself94.py
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Cuisine: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.\n")

    def set_number_served(self, served):
        self.number_served = served
    
    def increment_number_served(self, served):
        self.number_served += served