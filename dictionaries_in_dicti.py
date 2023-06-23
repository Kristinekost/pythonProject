# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"]
# }

# Nesting dictionary in a list
travel_log = [
    {"country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12
     },
    {"country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 2
     },
]


def add_new_country(country, cities_visited, total_visits):
    new_dictionary = {
        "country": country,
        "cities_visited": cities_visited,
        "total_visits": total_visits
    }
    travel_log.append(new_dictionary)

add_new_country("Russia", ["Moscow", "Saint Petersburg"], 2)

print(travel_log)
