#A Simple Dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

#Accessing Values in a Dictionary
new_points = alien_0['points']
print(f"\nYou just earned {new_points} points!")

#Adding New Key-Value Pairs
print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(f'\n{alien_0}')

#Starting with an Empty Dictionary
alien_0 = {}
alien_0['color'] = 'green'
alien_0['points'] = 5
print(f'\n{alien_0}')

#Modifying Values in a Dictionary
alien_0 = {'color': 'green'}
print(f"\nThe alien is {alien_0['color']}.")
alien_0['color'] = 'yellow'
print(f"\nThe alien is now {alien_0['color']}.")

#Alien speed
alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
alien_0['speed'] = 'fast'
print(f"\nOriginal position: {alien_0['x_position']}")
#Move the alien to the right.
#Determine how far to move the alien based on its current speed.
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment
print(f"New position: {alien_0['x_position']}")

#Removing Key-Value Pairs
print(f"\nBefore: {alien_0}")
del alien_0['x_position']
del alien_0['y_position']
print(f"After : {alien_0}")