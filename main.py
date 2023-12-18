name = str(input("Name: "))
age = int(input("Age: "))
has_driver_licence = input("has_driver_licence: ")

if name and age >= 18 and has_driver_licence == True:
    print(f"User {name} can rent a car")
else:
    print(f"User can't rent a car")
