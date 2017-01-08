#This program says hello and asks for a name and age

print('Hello!  What is your name?') #asks for their name
myName = input() #gets input, should be their name
print('It is good to meet you, ' + myName) #greeting
print('The length of your name is:') 
print(len(myName)) #prints length of the name
print('What is your age?') #asks for their age
myAge = input() #gets input, should be their age
print('You will be ' + str(int(myAge) + 1) + ' in a year.') #outputs their age + 1
