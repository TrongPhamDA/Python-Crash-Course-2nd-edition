#What is a List?
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print("a List:")
print(bicycles)

#Accessing Elements in a List
print("\nAccessing Elements in a List")
print(bicycles[0])
print(bicycles[0].title())

#Index position, start from 0, not 1
print("\nIndex position, start from 0 to 3, not from 1 to 4")
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

#Using
message = f"\nMy first bicycle was a {bicycles[0].title()}."
print(message)