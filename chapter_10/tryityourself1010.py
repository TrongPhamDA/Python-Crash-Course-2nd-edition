print("\nEx 10.11. Common Words:\n" + "-"*70)

def read_txt(filename):
    try:
        with open(filename, encoding='utf-8') as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        contents = ''
        print(f"\n'{filename}'' dose not exist!")
    else:
        print(f"\n'{filename}' has about:")
    return contents

filenames = ['gone with the wind.txt',
            'alice1.txt',
            'alice.txt',
            'siddhartha.txt',
            'moby_dick.txt',
            'little_women.txt',
            'dogs.txt', 
            'cats.txt']
words_list = ['the', 'the ', 'there', 'then']

for filename in filenames:
    contents = read_txt(filename)
    if contents:
        for word in words_list:
            print(f"- {contents.lower().count(word):6d} : '{word}'")