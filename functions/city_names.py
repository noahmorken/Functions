def city_country(city, country):
    """Return a fomatted city and country."""
    location = f"{city}, {country}"
    return location.title()

place = city_country('santiago', 'chile')
print(place)
place = city_country('san salvador', 'el salvador')
print(place)
place = city_country('managua', 'nicaragua')
print(place)