fruits = ["apple", "banana", "cherry", "date", "elderberry"]

# Add an item to the end of the list
fruits.append("fig")
print(fruits)

# Add an item to a specific index
fruits.insert(2, "coconut")
print(fruits)

# Remove an item from the list
fruits.remove("cherry")
print(fruits)

# Remove an item from a specific index
fruits.pop(3)
print(fruits)

# Remove the last item from the list
fruits.pop()

# Modify an item in the list
fruits[1] = "blueberry"