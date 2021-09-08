filename = 'tryityourself101_learning_python.txt'

with open(filename) as learning_c:
	contents = learning_c.read()
contents = contents.rstrip()
contents = contents.replace("Python", "C")

print(contents)