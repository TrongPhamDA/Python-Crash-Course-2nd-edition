pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(f"Current pets:\n{pets}")
while 'cat' in pets:
    pets.remove('cat')
print(f"\nAfter removing 'cat':\n{pets}")
