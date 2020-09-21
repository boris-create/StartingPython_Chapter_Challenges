# Roman Numerals

# ask user to enter number between 1-10
# if number is not 1-10 display error
number = int(input("Pick a number between 1 and 10: "))
if number < 1 or number > 10:
    print("Sorry, please pick a number between 1 and 10.")
# display roman numeral conversion
elif number == 1:
    romanNumeral = "I"
elif number == 2:
    romanNumeral = "II"
elif number == 3:
    romanNumeral = "III"
elif number == 4:
    romanNumeral = "IV"
elif number == 5:
    romanNumeral = "V"
elif number == 6:
    romanNumeral = "VI"
elif number == 7:
    romanNumeral = "VII"
elif number == 8:
    romanNumeral = "VIII"
elif number == 9:
    romanNumeral = "IX"
elif number == 10:
    romanNumeral = "X"
print(romanNumeral)
