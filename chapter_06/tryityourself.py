# 6-1. Person: Use a dictionary to store information about a person you know.
# Store their first name, last name, age, and the city in which they live.
# You should have keys such as first_name, last_name, age, and city.
# Print each piece of information stored in your dictionary.
person_info = {
	'first_name' : 'trong',
	'last_name' : 'pham',
	'age' : 29,
	'city' : 'hcmc',
	}
print(f"{person_info}\n")
keys = ['first_name', 'last_name', 'age', 'city']
for key in keys: print(f"{key}: {person_info[key]}")

# 6-2. Favorite Numbers: Use a dictionary to store people’s favorite numbers.
# Think of five names, and use them as keys in your dictionary.
# Think of a favorite number for each person, and store each as a value in your dictionary.
# Print each person’s name and their favorite number.
# For even more fun, poll a few friends and get some actual data for your program.
favorite_numbers = {}
favorite_numbers['trong'] = 7
favorite_numbers['duyen'] = 3
favorite_numbers['phuc'] = 1
favorite_numbers['thach'] = 4
favorite_numbers['bao'] = 5
print(f"\n{favorite_numbers}")

# 6-3. Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •Think of five programming words you’ve learned about in the previous chapters.
# Use these words as the keys in your glossary, and store their meanings as values.
# •Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line.
# Use the newline character (\n)
glossarys = {
	'del' : 'delete',
	'append' : 'add',
	'==' : 'equal to',
	'!=' : 'not equal to',
	'for' : 'a loop statement',
	}
for word, meaning in glossarys.items():
	print(f"\n{word}\n{meaning}")

# 6-4. Now that you know how to loop through a dictionary,
# clean up the code from Exercise 6-3 (page 99) by replacing your series of
# print() calls with a loop that runs through the dictionary’s keys and values.
# When you’re sure that your loop works, add five more Python terms to your glossary.
# When you run your program again, these new words and meanings should
# automatically be included in the output.
glossarys = {
	'del' : 'delete',
	'append' : 'add',
	'==' : 'equal to',
	'!=' : 'not equal to',
	'for' : 'a loop statement',
	}
for word, meaning in glossarys.items():
	print(f"\n{word}\n{meaning}")

# 6-5. Rivers: Make a dictionary containing three major rivers and the country
# each river runs through. One key-value pair might be 'nile': 'egypt'.
print("\nEx 6.5")
rivers = {
	'nile' : 'egypt',
	'hong' : 'vietnam',
	'dubai creek' : 'uae',
	'seine' : 'france',
	'volga' : 'russia',
	'mississippi' : 'usa',
	'nile' : 'egypt',
	}
# •	 Use a loop to print a sentence about each river, such as The Nile runs
# through Egypt.
print("\nFamous rivers in the world:")
for river, country in sorted(set(rivers.items())):
	if country in ['usa', 'uae']:
		country = country.upper()
	else:
		country = country.title()
	print(f"- The {river.title()} runs through {country}.")
# •	 Use a loop to print the name of each river included in the dictionary.
print("\nFamous rivers:")
for river in sorted(set(rivers.keys())):
	print(f"- {river.title()}")
# •	 Use a loop to print the name of each country included in the dictionary.
print("\nbelong to the following countries:")
for country in sorted(set(rivers.values())):
	if country in ['usa', 'uae']:
		print(f"- {country.upper()}")
	else:
		print(f"- {country.title()}")

# 6-6. Polling: Use the code in favorite_languages.py (page 97).
print("\nEx 6.6")
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
# •	 Make a list of people who should take the favorite languages poll.
# Include some names that are already in the dictionary and some that are not.
peoples = ['sarah', 'phil', 'trong pham', 'ngoc trong', 'andrew', 'edward', 'jen', 'michael']
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take the poll.
for name in peoples:
	if name in favorite_languages.keys():
		print(f"- {name.title()}, thank for your responding.")
	else:
		print(f"- {name.title()}, let's take the poll")


# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 99).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.
print("\nEx 6.7")
person0 = {
	'first_name': 'trong',
	'last_name' : 'pham',
	'age'       : 29,
	'city'      : 'phan rang - thap cham',
	}
person1 = {
	'first_name': 'duyen',
	'last_name' : 'huynh',
	'age'       : 29,
	'city'      : 'nha trang',
	}
person2 = {
	'first_name': 'hoang',
	'last_name' : 'do',
	'age'       : 29,
	'city'      : 'buon ma thuot',
	}
peoples = [person0, person1, person2]
print(f"We have {len(peoples)} people:")
for people in peoples:
	full_name = f"\n{people['first_name']}, {people['last_name']}"
	print(full_name.title())
	print(f"\tage  : {people['age']}")
	print(f"\tcity : {people['city'].title()}")

# 6-8. Pets: Make several dictionaries, where each dictionary represents a
# different pet. In each dictionary, include the kind of animal and the
# owner’sname. Store these dictionaries in a list called pets. Next, loop
# through your list and as you do, print everything you know about each pet.
print("\nEx 6.8")
pet0 = {
	'pet_name': 'keno',
	'animal'  : 'pig',
	'owner'   : 'charlie',
	}
pet1 = {
	'pet_name': 'fred',
	'animal'  : 'dog',
	'owner'   : 'jisoo',
	}
pet2 = {
	'pet_name': 'angel',
	'animal'  : 'pig',
	'owner'   : 'jimin',
	}
pet3 = {
	'pet_name': 'murphy',
	'animal'  : 'cat',
	'owner'   : 'billie',
	}
pet4 = {
	'pet_name': 'olivia',
	'animal'  : 'parrot',
	'owner'   : 'rose',
	}
pet5 = {
	'pet_name': 'oreo',
	'animal'  : 'parrot',
	'owner'   : 'gaga',
	}
pet6 = {
	'pet_name': 'kathy',
	'animal'  : 'pig',
	'owner'   : 'shawn',
	}
pet7 = {
	'pet_name': 'bunny',
	'animal'  : 'pig',
	'owner'   : 'suga',
	}
pet8 = {
	'pet_name': 'harley',
	'animal'  : 'dog',
	'owner'   : 'mina',
	}
pet9 = {
	'pet_name': 'falcon',
	'animal'  : 'pig',
	'owner'   : 'taeyang',
	}

pets = [pet0, pet1, pet2, pet3, pet4, pet5, pet6, pet7, pet8, pet9]
print(f"We have {len(pets)} pets:")
for pet in pets:
	print(f"- {pet['pet_name'].title()}")
	print(f"\tanimal : {pet['animal'].lower()}")
	print(f"\towner  : {pet['owner'].title()}")

# 6-9. Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.
print("\nEx 6.9")
favorite_places = {
	'trong' : ['nha trang', 'vung tau', 'da lat'],
	'hoang' : ['da nang', 'da lat', 'nha trang'],
	'duyen' : ['nha trang', 'da nang', 'phu quoc']
	}
for people, places in favorite_places.items():
	print(f"\n{people.title()}'s favorite places:")
	for place in places:
		print(f"\t- {place.title()}")

#6.10
print("\nEx 6.9")
favorite_numbers = {
	'trong': [7,1],
	'duyen': [49,79],
	'phuc' : [1,2,3,4],
	'thach': [1],
	'bao'  : [5,22,30],
	}
for name, numbers in favorite_numbers.items():
	if len(numbers) == 1:
		print(f"{name.title()}'s favorite number is: " + f"{str(numbers)[1:-1]}")
	else:
		print(f"{name.title()}'s favorite number are: " + f"{str(numbers)[1:-1]}")

# 6-11. Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the
# information you have stored about it.
print("\nEx 6.11")
largest_cities = {
	'tokyo'            : {'country' : 'japan',          'population' : 39105000, 'area' :  8231, 'density' : 4751 },
	'delhi'            : {'country' : 'india',          'population' : 31870000, 'area' :  2233, 'density' : 14272},
	'seoul'            : {'country' : 'south korea',    'population' : 22394000, 'area' :  2769, 'density' : 8087 },
	'shanghai'         : {'country' : 'china',          'population' : 22118000, 'area' :  4069, 'density' : 5436 },
	'sao paulo'        : {'country' : 'brazil',         'population' : 22495000, 'area' :  3237, 'density' : 6949 },
	'mexico city'      : {'country' : 'mexico',         'population' : 21505000, 'area' :  2385, 'density' : 9017 },
	'cairo'            : {'country' : 'egypt',          'population' : 19787000, 'area' :  2010, 'density' : 9844 },
	'mumbai'           : {'country' : 'india',          'population' : 22186000, 'area' :  1008, 'density' : 22010},
	'beijing'          : {'country' : 'china',          'population' : 19437000, 'area' :  4172, 'density' : 4659 },
	'dhaka'            : {'country' : 'bangladesh',     'population' : 16839000, 'area' :   456, 'density' : 36928},
	'osaka'            : {'country' : 'japan',          'population' : 15490000, 'area' :  3020, 'density' : 5129 },
	'new york'         : {'country' : 'united states',  'population' : 20902000, 'area' : 12093, 'density' : 1728 },
	'karachi'          : {'country' : 'pakistan',       'population' : 15292000, 'area' :  1044, 'density' : 14648},
	'buenos aires'     : {'country' : 'argentina',      'population' : 16216000, 'area' :  3222, 'density' : 5033 },
	'chongqing'        : {'country' : 'china',          'population' :  8261000, 'area' :  1536, 'density' : 5378 },
	'istanbul'         : {'country' : 'turkey',         'population' : 15311000, 'area' :  1375, 'density' : 11135},
	'kolkata'          : {'country' : 'india',          'population' : 18698000, 'area' :  1352, 'density' : 13830},
	'manila'           : {'country' : 'philippines',    'population' : 23971000, 'area' :  1873, 'density' : 12798},
	'lagos'            : {'country' : 'nigeria',        'population' : 15487000, 'area' :  1966, 'density' : 7877 },
	'rio de janeiro'   : {'country' : 'brazil',         'population' : 12486000, 'area' :  2020, 'density' : 6181 },
	'tianjin'          : {'country' : 'china',          'population' : 10932000, 'area' :  2813, 'density' : 3886 },
	'kinshasa'         : {'country' : 'dr congo',       'population' : 15056000, 'area' :   466, 'density' : 32309},
	'guangzhou'        : {'country' : 'china',          'population' : 21489000, 'area' :  4341, 'density' : 4950 },
	'los angeles'      : {'country' : 'united states',  'population' : 15477000, 'area' :  6351, 'density' : 2437 },
	'moscow'           : {'country' : 'russia',         'population' : 17693000, 'area' :  5879, 'density' : 3010 },
	'shenzhen'         : {'country' : 'china',          'population' : 14678000, 'area' :  1803, 'density' : 8141 },
	'lahore'           : {'country' : 'pakistan',       'population' : 11148000, 'area' :   852, 'density' : 13085},
	'bangalore'        : {'country' : 'india',          'population' : 13999000, 'area' :  1204, 'density' : 11627},
	'paris'            : {'country' : 'france',         'population' : 11027000, 'area' :  2844, 'density' : 3877 },
	'bogota'           : {'country' : 'colombia',       'population' :  9274000, 'area' :   562, 'density' : 16502},
	'jakarta'          : {'country' : 'indonesia',      'population' : 35362000, 'area' :  3541, 'density' : 9986 },
	'chennai'          : {'country' : 'india',          'population' : 11564000, 'area' :  1085, 'density' : 10658},
	'lima'             : {'country' : 'peru',           'population' :  8992000, 'area' :   891, 'density' : 10092},
	'bangkok'          : {'country' : 'thailand',       'population' : 17573000, 'area' :  3199, 'density' : 5493 },
	'nagoya'           : {'country' : 'japan',          'population' :  9522000, 'area' :  3704, 'density' : 2571 },
	'hyderabad'        : {'country' : 'india',          'population' :  9840000, 'area' :  1274, 'density' : 7724 },
	'london'           : {'country' : 'united kingdom', 'population' : 11120000, 'area' :  1738, 'density' : 6398 },
	'tehran'           : {'country' : 'iran',           'population' : 13819000, 'area' :  1704, 'density' : 8110 },
	'chicago'          : {'country' : 'united states',  'population' :  9013000, 'area' :  7006, 'density' : 1286 },
	'chengdu'          : {'country' : 'china',          'population' : 11920000, 'area' :  1829, 'density' : 6517 },
	'nanjing'          : {'country' : 'china',          'population' :  7729000, 'area' :  1614, 'density' : 4789 },
	'wuhan'            : {'country' : 'china',          'population' :  9729000, 'area' :  1722, 'density' : 5650 },
	'ho chi minh city' : {'country' : 'vietnam',        'population' : 13954000, 'area' :  1637, 'density' : 8524 },
	'luanda'           : {'country' : 'angola',         'population' :  8883000, 'area' :  1005, 'density' : 8839 },
	'ahmedabad'        : {'country' : 'india',          'population' :  7717000, 'area' :   360, 'density' : 21436},
	'kuala lumpur'     : {'country' : 'malaysia',       'population' :  8639000, 'area' :  2163, 'density' : 3994 },
	'xian'             : {'country' : 'china',          'population' :  7090000, 'area' :  1093, 'density' : 6487 },
	'hong kong'        : {'country' : 'china',          'population' :  7398000, 'area' :   290, 'density' : 25510},
	'dongguan'         : {'country' : 'china',          'population' :  8142000, 'area' :  1759, 'density' : 4629 },
	'hangzhou'         : {'country' : 'china',          'population' :  6713000, 'area' :  1445, 'density' : 4646 },
	'shenyang'         : {'country' : 'china',          'population' :  7208000, 'area' :  1515, 'density' : 4758 },
	'riyadh'           : {'country' : 'saudi arabia',   'population' :  6889000, 'area' :  1673, 'density' : 4118 },
	'baghdad'          : {'country' : 'iraq',           'population' :  6107000, 'area' :   694, 'density' : 8800 },
	'santiago'         : {'country' : 'chile',          'population' :  7026000, 'area' :  1147, 'density' : 6126 },
	'surat'            : {'country' : 'india',          'population' :  4875000, 'area' :   238, 'density' : 20483},
	'madrid'           : {'country' : 'spain',          'population' :  6006000, 'area' :  1365, 'density' : 4400 },
	'suzhou'           : {'country' : 'china',          'population' :  5103000, 'area' :  1386, 'density' : 3682 },
	'pune'             : {'country' : 'india',          'population' :  7948000, 'area' :   650, 'density' : 12228},
	'harbin'           : {'country' : 'china',          'population' :  4583000, 'area' :   671, 'density' : 6830 },
	'houston'          : {'country' : 'united states',  'population' :  6529000, 'area' :  4931, 'density' : 1324 },
	'dallas'           : {'country' : 'united states',  'population' :  6960000, 'area' :  5278, 'density' : 1319 },
	'toronto'          : {'country' : 'canada',         'population' :  6985000, 'area' :  2300, 'density' : 3037 },
	'dar es salaam'    : {'country' : 'tanzania',       'population' :  7461000, 'area' :   961, 'density' : 7764 },
	'miami'            : {'country' : 'united states',  'population' :  6212000, 'area' :  3313, 'density' : 1875 },
	'belo horizonte'   : {'country' : 'brazil',         'population' :  5159000, 'area' :  1288, 'density' : 4005 },
	'singapore'        : {'country' : 'singapore',      'population' :  5271000, 'area' :  1287, 'density' : 4096 },
	'philadelphia'     : {'country' : 'united states',  'population' :  5697000, 'area' :  5429, 'density' : 1049 },
	'atlanta'          : {'country' : 'united states',  'population' :  5434000, 'area' :  7400, 'density' : 734  },
	'fukuoka'          : {'country' : 'japan',          'population' :  2280000, 'area' :   505, 'density' : 4515 },
	'khartoum'         : {'country' : 'sudan',          'population' :  6017000, 'area' :  1031, 'density' : 5836 },
	'barcelona'        : {'country' : 'spain',          'population' :  4735000, 'area' :  1072, 'density' : 4417 },
	'johannesburg'     : {'country' : 'south africa',   'population' : 14167000, 'area' :  4040, 'density' : 3507 },
	'saint petersburg' : {'country' : 'russia',         'population' :  5207000, 'area' :  1373, 'density' : 3792 },
	'qingdao'          : {'country' : 'china',          'population' :  6232000, 'area' :  1655, 'density' : 3766 },
	'dalian'           : {'country' : 'china',          'population' :  3994000, 'area' :   987, 'density' : 4047 },
	'washington, d.c.' : {'country' : 'united states',  'population' :  7583000, 'area' :  5501, 'density' : 1378 },
	'yangon'           : {'country' : 'myanmar',        'population' :  6497000, 'area' :   603, 'density' : 10774},
	'alexandria'       : {'country' : 'egypt',          'population' :  4857000, 'area' :   293, 'density' : 16577},
	'jinan'            : {'country' : 'china',          'population' :  4381000, 'area' :   798, 'density' : 5490 },
	'guadalajara'      : {'country' : 'mexico',         'population' :  5437000, 'area' :   313, 'density' : 17371}
	}
for city, informations in largest_cities.items():
	print(f"\n{city.title()}")
	for info, values in informations.items():
		print(f"\t- {info} : " + f"{str(values).title()}")