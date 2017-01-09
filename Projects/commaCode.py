#program that takes a list and removes quotes and brackets as well as adding an and to the semifinal item
def addAnd(someList):       
    someList.insert(-1, 'and')  #inserts the and before the last item
    someList = str(someList)    #converts the list to a string in order to remove quotes and brackets
    someList = someList.replace("'","").replace("[","").replace("]","") #removes quotes and brackets
    print (someList)
    
someList = ['cats', 'dogs', 'monkeys', 'foxes']
addAnd(someList)

