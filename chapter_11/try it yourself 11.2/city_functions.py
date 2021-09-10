# 11-2. Population: Modify your function so it requires a third
# parameter, population. It should now return a single string of the
# form City, Country – population xxx, such as
# Santiago, Chile – population 5000000

def format_city_country(city_name, country_name, population=''):
    # format_name = f"{city_name.title()}, {country_name.title() - {population}}"
    if population:
        format_name = f"{city_name.title()}, {country_name.title()} - {str(population)}"
    else:
        format_name = f"{city_name.title()}, {country_name.title()}"
    return format_name