filename = 'tryityourself101_learning_python.txt'

with open(filename) as learning_python1:
	contents = learning_python1.read()
print(contents.rstrip())

with open(filename) as learning_python2:
	for line in learning_python2:
		print(line.rstrip())

with open(filename) as learning_python3:
	lines = learning_python3.readlines()
for line in lines:
	print(line.rstrip())