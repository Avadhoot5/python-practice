my_dict = {
    "name": "Alice",
    "age": 30,
    "city": "New York",
    "occupation": "Engineer",
    "hobbies": ["reading", "hiking", "coding"],
    "favorite_color": "blue",
    "is_student": False,
    "height_cm": 165,
    "birth_year": 1993,
    "languages_spoken": ["English", "Spanish"]
}

# dict methods - items, keys, values, updated, get

# print(my_dict.items())

# print(my_dict.keys()) # returns the keys of the dict

# print(my_dict.values())

# If the key does not exist, it returns None (or a specified default value if provided).
print(my_dict.get('city'))

# If the key does not exist, it raises a KeyError.
print(my_dict['city'])


