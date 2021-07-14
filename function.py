'''Given the exclusive price of milk calculate the inclusive price of items in tuskys supermarket
'''
#The below function calculates the inclusive price  
def calculateInclusivePrice(exclusivePrice, vatTax ): #Has parameters exclusivePrice & vatTax
    inclusivePrice = exclusivePrice + (exclusivePrice * vatTax)#Calculates inclusivePrice
    return inclusivePrice #returns InclusivePrice

#The below function requests input of exclusivePrice and vatTax
def userInput ():
    exclusivePrice = float (input("Enter exclusive price"))#accepts exclusivePrice iput
    vatTax =float(input ("Enter vat Tax "))
    return calculateInclusivePrice (exclusivePrice, vatTax)

print(userInput()) 
