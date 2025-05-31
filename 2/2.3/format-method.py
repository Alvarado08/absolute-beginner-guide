# before the f-strings were introduced, the format() method was used

# using positional arguments
name = "John"
age = 25
print("My name is {0} and I am {1} years old".format(name, age))

# using named arguments
print("My name is {name2} and I am {age2} years old".format(name2 = "Jane", age2 = 30))

# aligning text
print("Left aligned: {0:<10}".format("Hello"))
print("Right aligned: {0:>10}".format("Hello"))
print("Center aligned: {0:^10}".format("Hello"))

# formatting numbers with commas
print("Number with commas: {:,}".format(1000000))
print("Number with commas: {:,}".format(1000000000))

# formatting numbers with commas and decimal places
print("Number with commas and decimal places: {:,.2f}".format(12389.123456)) # 12,389.12

# padding with zeros
print("Number with zeros: {:0>10}".format(5))
print("Number with zeros: {:0<10}".format(5))
print("Padded with zeros: {:05d}".format(42))