# 9-4. Number Served: Start with your program from
# Exercise 9-1 (page 162). Add an attribute called
# number_served with a default value of 0. Create
# an instance called restaurant from this class.
# Print the number of customers the restaurant has
# served, and then change this value and print it again.
# Add a method called set_number_served() that lets you
# set the number of customers that have been served.
# Call this method with a new number and print the
# value again.
# Add a method called increment_number_served() that
# lets you increment the number of customers who’ve
# been served. Call this method with any number you like
# that could represent how many customers were served in,
# say, a day of business.

print("\nEx 9.4 Number Served\n" + "-"*70)

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        
        # Add an attribute called number_served
        self.number_served = 0
        
    def describe_restaurant(self):
        print(f"Welcome to {self.restaurant_name}!")
        print(f"Cuisine: {self.cuisine_type}\n")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is open.\n")

    # Set the number of customer that have been served
    def set_number_served(self, served):
        self.number_served = served
    
    # Increment the number of customers who’ve been served
    def increment_number_served(self, served):
        self.number_served += served

res_1 = Restaurant("Lang Nuong Nam Bo", "Grill & Beer")
res_1.describe_restaurant()
res_1.open_restaurant()


# Call set_number_served method
res_1.set_number_served(5)


# Call increment_number_served method
res_1.increment_number_served(10)

# Print the number of customers the restaurant has served
print(f"Number served: {res_1.number_served}")