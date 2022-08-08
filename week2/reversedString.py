# Given a string, create a function that returns the string reversed.

userIn = input("ENTER A STRING : ")

def reverseStr(str):
    reversedString = userIn[::-1]
    print(reversedString)

reverseStr(str)