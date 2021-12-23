def describe_city(city='reykjavik', country='iceland'):
    """Display information for a city."""
    print(f"\n{city.title()} is in {country.title()}.")

describe_city()
describe_city('qaqortoq', 'greenland')
describe_city(country='norway', city='fredrikstad')