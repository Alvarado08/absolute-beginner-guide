# and, or, not

# and
temperature = 25
is_raining = True
if temperature > 20 and is_raining:
    print("It's cold outside")
else:
    print("It's warm outside")

# or
temperature = 25
is_raining = True
if temperature > 20 or is_raining:
    print("It's cold outside")
else:
    print("It's warm outside")

# not
temperature = 25
is_raining = True
if not is_raining:
    print("It's cold outside")
else:
    print("It's warm outside")