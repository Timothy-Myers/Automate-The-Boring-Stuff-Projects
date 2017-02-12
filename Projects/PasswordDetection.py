import re

def passwordTest(password):
    return bool(re.search(userPWcomp, ''.join(sorted(password)))) #searched to see if the password provided meets the credentials and returns True if it does.

print ('Please enter the password you want to use')
userPW = input() #gets password
userPWcomp = re.compile(r'\d+[^0-9a-zA-Z]*[A-Z]+[^0-9a-zA-Z]*[a-z]+\w{8}') #checks to see if there is a numeric value, an uppercase value, a lowercase value, and that it's at least 8 characters long

if passwordTest(userPW) == True:  #tests the password and outputs the appropriate message
    print('You have a strong password!')
else:
    print('This is not a strong password')

