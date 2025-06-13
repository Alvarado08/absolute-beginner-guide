# Converting a list to a set
response_list = ["yes", "no", "maybe", "yes", "no"]
response_set = set(response_list)
print(response_set) # {'maybe', 'no', 'yes'}

# Membership testing
# Checking if an item in=s in a set is faster than in a list
allowed_users = {"Alice", "Bob", "Charlie"}
user = "Bob"
if user in allowed_users:
    print(f"{user} is allowed to access the system")
else:
    print(f"{user} is not allowed to access the system")

# Removing duplicates from a list
numbers = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
numbers_set = set(numbers) # {1, 2, 3, 4, 5}