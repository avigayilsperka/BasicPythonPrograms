#Number of people
ppl= int(input("Number of attendees:"))

#Hotdogs per persom
hdpp= float(input("How many hotdogs per person?"))

#Total hot dogs
totalhd= hdpp*ppl

#Number of hot dog packages
hdpack= totalhd/10
print('You need',(hdpack),'packages of hotdogs.')


#Number of hot dog buns packages
buns= totalhd/8
print('You need',buns,'packages of buns.')


#Leftover hot dogs and buns
if totalhd%10 > 0:
    hdleft = 10 - (totalhd%10)
    print('There will be',int(hdleft),'hotdogs leftover.')
else:
    print('All of the hotdogs will be eaten.')
    

if totalhd%8 > 0:
    bunsleft = 8 - (totalhd%8)
    print('There will be',int(bunsleft),'buns leftover.')
else:
    print('All of the buns will be eaten.')





