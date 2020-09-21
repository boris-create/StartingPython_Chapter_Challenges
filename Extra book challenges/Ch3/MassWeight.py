# Mass and Weight

# mass in kilograms and weight in newtons
# if you know the mass in in kilograms you can calcualte mass in newtons

mass = float(input("What is objects weight in Kilograms: "))

# calculate weight
weight = float(round(mass * 9.8, 2))

# display weight of object
if weight > 500:
    print("Object is too heavy.")
elif weight < 100:
    print("Object is too light.")
else:
    print("Object weight is:", weight, "newtons")
