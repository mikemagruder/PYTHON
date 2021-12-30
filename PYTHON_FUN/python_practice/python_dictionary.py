favorite_cities = {}
favorite_places = {}

favorite_cities["id_1"] = "San Francisco"
favorite_cities["id_2"] = "Florence"
favorite_cities["id_3"] = "Venice"
favorite_cities["id_4"] = "Rome"

favorite_places["id_1"] = "Italy"
favorite_places["id_2"] = "Virgin Islands"
favorite_places["id_3"] = "Costa Rica"
favorite_places["id_4"] = "Hawaii"

print(favorite_cities)
print(favorite_places)

########
print(len(favorite_cities))
print(str(favorite_places))
print(type(favorite_places))

#########

copied_favorite_places = favorite_places.copy
print(copied_favorite_places)

get_key = favorite_places.get("id_2")
print(get_key)

##########

keys = favorite_cities.keys()
print(keys)

values = favorite_cities.values()
print(values)