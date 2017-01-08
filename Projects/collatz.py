#this program shows how the Collatz sequence works by having a user enter a number and using the sequence to get the number down to 1

#definition where the number is analyzed
def collatz(number):
    #continues until number is 1
    while number != 1:
        #examines if number is even
        if number % 2 == 0:
            number = number //2
        #examines if number is odd
        elif number % 2 == 1:
            number = (number * 3) + 1
        print (number)

#asks user to enter number
print ('Please enter a number')
while True:
    number = input()
    try:
        #if a valid number is entered it's passed into the defnition
        number = int(number)
        collatz(number)
    except ValueError:
        #if an invalid integer is entered a message is shown until a valid integer is entered
        print ('Please enter a valid number')
        continue


        
