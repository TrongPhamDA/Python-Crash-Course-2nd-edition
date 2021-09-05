players = ['charles', 'martina', 'michael', 'florence', 'eli'] 
print(players)

#print 3 first items
print(players[0:3])

#print 2nd-3rd-4th items
print(players[1:4])

#print out 4 first item
print(players[:4])

#print out from 3rd to the last item
print(players[2:])

print("\n")
print("Here are the first three players on my team:")
for player in players[:3]: print(player.title())
