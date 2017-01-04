#A program that is a 'guess the number' game
import random

#gets user's name
print('Hi, what is your name?')
name = input() 

#tells user what the game is and generates the random number
print('Well, ' + name + ', I am thinking of a number between 1 and 100, please guess.  You have ten chances.')
secretNumber = random.randint(1,100)

#for loop where game takes place
for guessesTaken in range(1,10):
    #asks for and receives user's guess
    print('Take a guess!')
    guess = input()
    #evalutes the guess and responds accordingly
    try:
        guess = int(guess)
        if guess < secretNumber:
            print ('Your guess is too low')
        elif guess > secretNumber:
            print ('Your guess is too high')
        else:
            break
    except ValueError:
        print('Please enter a number.')
       
        
if guess == secretNumber:
    print('Good Job, ' + name + '.  You took ' + str(guessesTaken) + ' guesses and correctly guessed the number!')
else:
    print('Sorry, you did not guess the number, it was ' + str(secretNumber))
