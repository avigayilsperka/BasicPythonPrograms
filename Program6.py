

def main():
     #Ask user for number of work days
     num=int(input('Enter the number of work days:'))

     #input validation
     while num < 1:
          num=int(input('Invalid number of days. Please enter a value of 1 or greater:'))
          
     #Set up column headings
     print('Day: \t Pay:')

     #Initalize salary to 0
     salary=0
  
     #Salary per day is the square of the day number
     #Calculate running total in the loop
     #Print chart in loop
     for x in range(num):
          total=2**x
          salary+=total
          print(x+1,'\t',total)

     print() 
     print('Your total salary is: $',comma(salary/100), sep="")
     print() 
     print('Thank you for using my program!')

def comma(salary):
     return ("{:,}".format(salary))


main()



