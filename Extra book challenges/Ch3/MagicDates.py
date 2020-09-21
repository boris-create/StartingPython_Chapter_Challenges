# Magic Dates

# ex = june 10 1960... 6/10/60 (day*month=year)

# ask user to enter month day and year
print("pick a month, day, and year in numeric value..")
print("ex... day: 01, month: 07, year: 89")
month = int(input("\nPick a month in numeric value: "))
day = int(input("Pick a day: "))
year = int(input("Pick a year in 2 digit format: "))

# display if magic date or not
if (month * day) == year:
    print("\nThis is a magic date")
else:
    print("\nThis is not a magic date")
