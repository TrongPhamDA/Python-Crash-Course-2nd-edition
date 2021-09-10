# 11-1. City, Country: Write a function that accepts two
# parameters: a city name and a country name. The function should
# return a single string of the form City, Country, such as
# Santiago, Chile. Store the function in a module
# called city_functions.py

def format_city_country(city_name, country_name):
    format_name = f"{city_name.title()}, {country_name.title()}"
    return format_name