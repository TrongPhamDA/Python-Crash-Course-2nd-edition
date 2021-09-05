#A Dictionary of Similar Objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print(f"\n{favorite_languages}")

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.\n")

#Dùng .items() để truy cập toàn bộ cặp giá trị key-value
for name, language in favorite_languages.items():
    print(f"{name.title()}'s favorite language is {language.title()}.")

#Dùng .keys() để truy cập toàn bộ keys
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("\n")
for name in favorite_languages.keys():
    print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())
    if name in friends:
        language = favorite_languages[name]
        print(f"\t{name.title()}, I see you love"
            "{language.title()}!")
if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

#Looping Through a Dictionary’s Keys in a Particular Order
print("\n")
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

#Looping Through All Values in a Dictionary
print("\n")
print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(f"- {language.title()}")

#thêm hàm set() ở trước để lấy danh sách unique:
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("\n")
print("The following languages have been mentioned - "
    "unique with set():")
for language in set(favorite_languages.values()):
    print(f"- {language.title()}    ")

# A List in a Dictionary
print("\n# A List in a Dictionary")
favorite_languages = {
    'jen'   : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward': ['ruby', 'go'],
    'phil'  : ['python', 'haskell'],
    }
for name, languages in favorite_languages.items():
    if len(languages) == 1:
        print(f"\n{name.title()}'s favorite language is {language.title()}.")
    else:
        print(f"\n{name.title()}'s favorite languages are:")
        for language in languages:
            print(f"\t{language.title()}")
