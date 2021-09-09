# 10-9. Silent Cats and Dogs: Modify your except block in
# Exercise 10-8 to fail silently if either file is missing.

print("\nEx 10.9 Silent Cats and Dogs\n" + "-"*70)

def read_txt(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        # change print() to 'pass'
        pass
    else:
        print(f"\n{filename}:")
        for line in lines:
            print(f"- {line.title().rstrip()}")

filenames = ['cats.txt', 'dogs.txt', 'cat.txt', 'dog.txt']
for filename in filenames:
    read_txt(filename)