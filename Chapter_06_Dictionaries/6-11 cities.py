cities ={'caracas': {'country':'venezuela', 'population':'5k',
        'fact': 'is the capital of the country'},
        'valencia': {'country': 'spain', 'population': '3k',
        'fact': ' is the 3rd major city of the country'},
        'barcelona': {'country': 'spain', 'population': '4k',
        'fact': 'oficial language is catalan'}}

for city, city_info in cities.items():
    print(f"City name: {city.title()}")
    print(f"\tIs locate in: {city_info['country'].title()}")
    print(f"\tPopulation around: {city_info['population'].title()}")
    print(f"\tA interest facy is: {city_info['fact']}")
