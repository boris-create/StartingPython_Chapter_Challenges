#  Day of the Week

# ask user for number between range of 1-7
number = int(input("Pick a number between One and Seven: "))
if number > 7:
    print("Sorry, please choose a number between 1 and 7.")
elif number == 1:
    day = "Monday"
elif number == 2:
    day = "Tuesday"
elif number == 3:
    day = "Wednesday"
elif number == 4:
    day = "Thursday"
elif number == 5:
    day = "Friday"
elif number == 6:
    day = "Saturday"
else:
    day = "Sunday"
print("Day of the weeek is: ", day)
