# Given a string, create a function that returns the string reversed.

userIn = input("ENTER A STRING : ")

def reverseStr(str):
    reversedIn= userIn[::-1]
    print(reversedIn)

#Using a FOR loop -------------------------------------------------------
def reverseStr(str):
    strIn = ''
    for i in userIn:
        strIn = i + strIn
    print(strIn)

reverseStr(str)