#this program asks for a name and password, authenticating if the name is Mary and the password is MaryPW123
print('What is your name?')
name = input()  #gets name
if name == 'Mary':
    print('Hi Mary')
    print('What is your password?')
    password = input() #gets password
    if password == 'MaryPW123':
        print('Login Successful') #displays correct password message
    else:
        print('Wrong Password') #displays wrong password message
else:
    print('Sorry, a log-in is not available for you') #if any user other than 'Mary' is entered this displays
