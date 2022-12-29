import random

num=random.randint(1,100) #assign random number

print('How quickly can you guess our number?')

guess = int(input('Enter a number between 1 and 100:')) #prompt user
count=1 #intialize counter variable

while num != guess: 
    if guess > num: # guess is too high
        guess = int(input("Too high!\nGuess again:"))
    else: #guess is too low
        guess = int(input("Too low!\nGuess again:"))
    count+=1 #counter

if count==1: # got number on the first try
    print('Congrats! You guessed the number on your first try!')
else: # 2 or more tries
    print('Congrats! After',count, 'tries you guessed the correct number!')

                        

