age = input("Enter your age: ")

if int(age) > 0 and int(age) < 10:
    print("You are a child")
elif int(age) > 10 and int(age) < 18:
    print("You are a teenager")
elif int(age) > 18 and int(age) < 65:
    print("You are an adult")
else:                               
    print("You are a senior")