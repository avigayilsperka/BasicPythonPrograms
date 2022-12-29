

#Ask user for object's weight
weight=float(input('Enter the weight of the package:'))

#Determine the charge based on weight
if weight <= 2:
    charge=weight*1.50

elif  weight <= 6:
    charge=weight*3.00

elif weight <= 10:
    charge=weight*4.00

elif weight > 10:
    charge=weight*4.75

#print total formatted charge
print()
print('The total shipping charge is: $', end='')
print(format(charge,',.2f'))
print()
print('Thank you for using this program!')

