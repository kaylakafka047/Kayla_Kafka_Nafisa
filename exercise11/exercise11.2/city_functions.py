def city_country(city, country, population=None):
    """Return a city, country, and optionally population."""

    if population:
        formatted_name = (
            f"{city}, {country} - population {population}"
        )
    else:
        formatted_name = f"{city}, {country}"

    return formatted_name.title() if not population else (
        f"{city.title()}, {country.title()} - population {population}"
    )