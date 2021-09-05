motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

#Change motocycles[0]
print("\nChange")
motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles[0] = "ducati"
print(motorcycles)

#Appending (thêm)
print("\nAppending")
motorcycles = ['honda', 'yamaha', 'suzuki'] 
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)

#Dynamic list
print("\nDymamic list")
motorcycles=[]
print(motorcycles)
motorcycles.append("honda")
print(motorcycles)
motorcycles.append("yamaha")
print(motorcycles)
motorcycles.append("suzuki")
print(motorcycles)
motorcycles.append("ducati")
print(motorcycles)

#Delete Element
print("\nDelete")
print(motorcycles)
del motorcycles[3]
print(motorcycles)
del motorcycles[2]
print(motorcycles)
del motorcycles[1]
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#Delete the last element - pop()
print("\npop() - delet the last element")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
pop_motocycles = motorcycles.pop()
print(motorcycles)
print(pop_motocycles)

#Delete any element - pop(1)
print("\npop(1) - delete any element")
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
pop_motocycles = motorcycles.pop(1)
print(motorcycles)
print(pop_motocycles)

#Delete by value - remove(value) - just for the 1st value finded
print("\nDelete by value - remove(value)")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles)
motorcycles.remove('suzuki')
print(motorcycles)


print("\n")
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#Error
print("\nError - get the lastest value [-1]")
print(motorcycles)
#print(motorcycles[3]) #Out of range
print(motorcycles[-1])
