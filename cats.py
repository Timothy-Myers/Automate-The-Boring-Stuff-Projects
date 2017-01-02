print('How many cats do you have?')
numCats = input() #gets the number of cats a user has
try:
    if int(numCats) >= 4:
        print('You have a lot of cats..')
    elif int(numCats) > 0 and int(numCats) < 4:
        print('You have a regular amount of cats')
    elif int(numCats) == 0:
        print('You should get a cat')
    elif int(numCats) < 0:
        print('How does one have negative cats?')
except ValueError: #if they enter something besides a number
    print('Please enter a number.')
