
#Explain program
print('This program calculates the average amount of rainfall over a period of years.')
print()

#receive number of years
years=int(input('Enter the number of years you wish to calculate:'))
print()

#input validation
while years < 1:
    years=int(input('Error: Year amount must be 1 or greater. Please re-enter the number of years:'))

#Instructions to user
print('Please enter the amount of rainfall per month:')
print()

#Set accumulator
total=0

#for every year, print year title followed by 12 months. Each month receives input which is accumulated.

for x in range(years):
    print('Year',x+1,'-')  
    for month in range(12):
          print('Month',month+1, end=':')
          amt=float(input(''))
          while amt < 0:
                amt=float(input('Positive numbers only. Please re-enter the monthly total:'))
          total+=amt

#calculate average
avg=format(total/(years*12),'.2f')

#print final results
print()
print('Over',years*12,'months, there was a total of',total,'inches of rainfall.')
print()
print('The average amount of rainfall per month is',avg,'inches.')
print()
print('Thank you for using this program!')
         
             
              
