#imports the ability to get a random number (we will learn more about this later!)
from random import *

#Create the list of words you want to choose from.
aList = ["Stringy Sam","Chatty Chad","Strapping Strap","Meaty Meat"]

#Generates a random integer.

response = input("Would you like a fun name?(Y/N?)")
while response != "N":
    if response == "Y":
        aRandomIndex = randint(0, len(aList)-1)
        print(aList[aRandomIndex])
    else:
        print("{} is an invalid input.".format(response))
    response = input("Would you like a fun name?(Y/N?)")
