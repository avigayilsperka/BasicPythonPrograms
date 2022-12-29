#Amount of cookies
amount=float(input("How many cookies would you like to bake?"))

#Multiplier
mult = amount/48
sugar= mult * 1.5
butter= mult *1
flour= mult *2.75

#Print Recipe
print("You need:")
print(format(sugar,'.2f'), "C. of sugar")
print(format(butter,'.2f'),"C. of butter")
print(format(flour,'.2f'), "C. of flour")

