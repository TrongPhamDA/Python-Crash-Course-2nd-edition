# 10-8. Cats and Dogs: Make two files, cats.txt and dogs.txt. Store at
# least three names of cats in the first file and three names of dogs
# in the second file. Write a program that tries to read these files
# and print the contents of the file to the screen. Wrap your code in
# a try-except block to catch the FileNotFound error, and print a
# friendly message if a file is missing. Move one of the files to a
# different location on your system, and make sure the code in the
# except block executes properly.

print("\nEx 10.8 Cats and Dogs\n" + "-"*70)

def read_txt(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            lines = file_object.readlines()
    except FileNotFoundError:
        print(f"\n{filename} does not exist.")
    else:
        print(f"\n{filename}:")
        for line in lines:
            print(f"- {line.title().rstrip()}")

filenames = ['cats.txt', 'dogs.txt', 'cat.txt', 'dog.txt']
for filename in filenames:
    read_txt(filename)