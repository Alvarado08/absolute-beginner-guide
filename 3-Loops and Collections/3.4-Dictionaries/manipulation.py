# Dictionaries are dynamic
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# Adding a new key-value pair
person["city"] = "Los Angeles"
print(person)

# Removing a key-value pair
del person["city"]
print(person)

# Practical use cases
# 1. Storing user information(user profile)
# 2. Storing product information(inventory)