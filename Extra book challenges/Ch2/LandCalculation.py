# Land Calculation

# One acre in footage
oneAcre = 43560

# Users total square footage
totalSquarefeet = float(input('what is the total square footage? '))

#  Calculates total acerage
totalAcerage = round(float(totalSquarefeet / oneAcre), 2)

# displays Total acerage to user
print ('Total Acerage: ', totalAcerage)
