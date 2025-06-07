first_shelf = ["apple", "banana", "cherry",]
second_shelf = ["pear", "melon", "orange",]
third_shelf = ["pineapple", "strawberry", "blueberry",]

all_fruits = [first_shelf, second_shelf, third_shelf]

new_book = "Moby Dick"

# Add a new book to the second shelf
all_fruits[1].append(new_book)

print(f"The second shelf: {all_fruits[1]}")