# Compund Interest
# suppose you want to deposit money into a savings account
# and earn interest for "x" years
# use this formula:  A = P(1 + (r / n)) ** nt

# ask user input for the following:
# principle amount that was originally deposited into the account
P = int(input('What is the amount of interest ORIGINALLY deposited? '))
print('')

# annual interest rate paid by the account
print('User should enter the interest rate as a percentage...')
print('for example: 2% should be entered as "2", not as "0.02"')
r = int(input('What is the ANNUAL % rate paid by the account? '))
print('')

# # number of times per year the interest in compounded
print('for example: if interst in compounded monthly enter 12...')
print(' ..if quarterly enter 4, if bi-annually enter 2')
n = int(input('Number of times per year interest will be compounded? '))
print('')

# number of years account will be left to earn interest
t = int(input('How many years will the account be left to earn interest? '))
print('')

# calculate for A: amount of money in the account after "x" years
new_r = float(r / 100)
A = float(round(P * (1 + (new_r / n)) ** (n * t)))
print('Total balance of the account after "specified" amount of years: ', A)
