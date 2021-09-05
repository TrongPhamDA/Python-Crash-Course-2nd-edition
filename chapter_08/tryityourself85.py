# 8-5. Cities: Write a function called describe_city()
# that accepts the name of a city and its country.
# The function should print a simple sentence, such
# as Reykjavik is in Iceland. Give the parameter
# for the country a default value. Call your function
# for three different cities, at least one of which
# is not in the default country.

print("\nEx 8.5 Cities\n" + "-"*70)
def describe_city(city, country = 'Vietnam'):
	print(f"{city.title()} is in {country.title()}.")

describe_city(country='vietnam', city='ho chi minh')
describe_city('da nang')
describe_city(city='can tho')