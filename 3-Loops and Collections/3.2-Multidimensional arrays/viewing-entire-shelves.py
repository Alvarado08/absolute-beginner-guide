first_shelf = ["apple", "banana", "cherry",]
second_shelf = ["pear", "melon", "orange",]
third_shelf = ["pineapple", "strawberry", "blueberry",]

all_fruits = [first_shelf, second_shelf, third_shelf]

for shelf_number, shelf in enumerate(all_fruits):
    print(f"Shelf {shelf_number} contains:")
    for fruit in shelf:
        print(f" - {fruit}")
    print()