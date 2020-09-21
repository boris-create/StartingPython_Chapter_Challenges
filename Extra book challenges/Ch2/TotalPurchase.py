# Total Purchase

# user input for each item (5)
item1 = float(input('price of item 1: '))
item2 = float(input('price of item 2: '))
item3 = float(input('price of item 3: '))
item4 = float(input('price of item 4: '))
item5 = float(input('price of item 5: '))

salesTax = float((item1 * 0.07) + (item2 * 0.07) +
(item3 * 0.07) + (item4 * 0.07) + (item5 * 0.07))  # 7%

subtotal = float((item1 + item2 + item3 + item4 + item5))
totalCost = float(subtotal + salesTax)

print('sales tax: ', salesTax)
print('sub total: ', subtotal)
print('total cost: ', totalCost)
