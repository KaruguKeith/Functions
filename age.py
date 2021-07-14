#Given the current year and the year of birth provided by the user calculate and return 
#the age of the user 
#1 Provide at least two functions
#2 separate business logic to user logic
#3 function should take at least one or more parameters
#4 function should return a value
#5 Call a function within a function
#6 print the age
'''Beginning of code'''




def calculateAge(currentYear,birthYear):
    
    age = currentYear - birthYear
    return age

def userYearInput ():

    currentYear = int(input("Which year is it ? "))
    birthYear = int(input("What is your year of birth? "))
    return calculateAge(currentYear,birthYear)

print(("You are") , userYearInput() , ("years old"))

    

    