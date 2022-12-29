#Enter cost of the meal
cost=float(input("Please enter the cost of the food:"))

#Calculate Tip and Sales Tax
tip=cost*.18
tax=cost*.07
total=cost+tip+tax

#Print Amounts
print("18% Tip=",format(tip,'.2f'))
print("7% Tax=",format(tax,'.2f'))
print("Total=",format(total,'.2f'))

