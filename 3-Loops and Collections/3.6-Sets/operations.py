# Sets support various operations that mirror those you might find in mathematics
# Union: combines elements from both sets without duplicates
# Intersection: finds elements common to both sets
# Difference: elements in one set but not in the other
# Symmetric difference: elements in either set but not both

# Example of set operations
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union
union_set = set1.union(set2)
# or
union_set = set1 | set2
print(union_set) # {1, 2, 3, 4, 5, 6}

# Intersection
intersection_set = set1.intersection(set2)
# or
intersection_set = set1 & set2
print(intersection_set) # {3, 4}

# Difference
difference_set = set1.difference(set2)
# or
difference_set = set1 - set2
print(difference_set) # {1, 2}

# Symmetric difference
symmetric_difference_set = set1.symmetric_difference(set2)
# or
symmetric_difference_set = set1 ^ set2
print(symmetric_difference_set) # {1, 2, 5, 6}