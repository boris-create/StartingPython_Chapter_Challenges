# Planting Grapevines

# vineyard needs to know how many grapevines to plant in each row
# use this formula to calculate total grapevines:  V = (R - (2 * E)) / S

# R - length of rows in feet
R = float(input('what is the length of each row in feet? '))

# amount of space in feet, used by end post assembly
E = float(input('what is the amount of space used by end post in feet? '))

# space between vines feet
S = float(input('What is the space between each vine in feet? '))

# V - Grapevines that will fit in each row
V = float(round(((R - (2 * E)) / S), 2))

# calc and display number of vines that will fit in each row
print('total grapevines per row: ', V)
