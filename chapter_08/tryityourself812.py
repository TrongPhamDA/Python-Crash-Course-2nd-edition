# 8-12. Sandwiches: Write a function that accepts a list
# of items a person wants on a sandwich. The function
# should have one parameter that collects as many items
# as the function call provides, and it should print
# a summary of the sandwich that’s being ordered. Call
# the function three times, using a different number of
# arguments each time

print("\nEx 8.12 Sandwiches\n" + "-"*70)
def make_sandwich(*items):
    print(f"\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

make_sandwich('cheese', 'ham', 'cucumber', 'bacon', 'onion')
make_sandwich('chesse', 'bacon', 'salad', 'mushrooms', 'sauce', 'tomato')