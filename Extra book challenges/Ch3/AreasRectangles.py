# Areas of Rectangles

# ask for length and width of 2x rectangles
length1 = int(input("Length of rectangle 1: "))
width1 = int(input("Width of rectangle 1: "))
length2 = int(input("Length of rectangle 2: "))
width2 = int(input("Width of rectangle 2: "))

# area = length * width
area1 = length1 * width1
area2 = length2 * width2

# tell user which rectangle has greater area
if area1 > area2:
    print("\nRectangle 1 is larger!")
elif area1 == area2:
    print("\nThey are the same size!")
else:
    print("\nRectangle 2 is larger!")
