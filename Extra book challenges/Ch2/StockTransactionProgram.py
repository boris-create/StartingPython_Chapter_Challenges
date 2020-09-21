# Stock Transaction Program

# joe purchased stock from ACME Software
shares = 2000
purchasePrice = 40.00  # $40 .00 per share
totalPaid = shares * purchasePrice  # Total paid for 2000 shares
buyComission = 0.03 * (purchasePrice * shares)  # 3 % amount paid for stocks

# 2 weeks later sold stock
sharesSold = 2000
salePrice = 42.75  # $42 .75 per share
totalGain = sharesSold * salePrice  # amount gained from sale
saleComission = 0.03 * (salePrice * sharesSold)

# Money left buy / sell
moneyLeft = -(totalPaid + buyComission)
moneyGain = totalGain - saleComission
profit = moneyLeft + moneyGain
# display
print('Total Paid to Buy: ', totalPaid)
print('')
print('Amount Comission Paid to Buy: ', buyComission)
print('')
print('Amount Stock Sold at: ', totalGain)
print('')
print('Comission Paid when Sold: ', saleComission)
print('')
print('Money Left when Bought: ', moneyLeft)
print('')
print('Money Left when Sold: ', moneyGain)
print('')

# did joe gain / lose money ?
print('Profit after buying shares.')
if moneyLeft >= 0:
    print('After the transaction, you gained', moneyLeft, 'dollars.')
else:
    print('After the transaction, you lost', moneyLeft, 'dollars.')
print('')
print('Profit after selling shares.')
if moneyGain >= 0:
    print('After the transaction, you gained', moneyGain, 'dollars.')
else:
    print('After the transaction, you lost', moneyGain, 'dollars.')
print('')
print('Your profit is: ', profit)
