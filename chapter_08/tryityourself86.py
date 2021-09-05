# 8-6. City Names: Write a function called city_country()
# that takes in the name of a city and its country. The
# function should return a string formatted like this:
# "Santiago, Chile" Call your function with at least
# three city-country pairs, and print the values that
# are returned.

print("\nEx 8.6 City Names\n" + "-"*70)
def city_country(city, country='vietnam'):
	value_return = f"{city.title()}, {country.title()}"
	return value_return

city = city_country('ha noi', 'vietnam')
print(city)

city = city_country(city='da nang')
print(city)

city = city_country('da lat')
print(city)