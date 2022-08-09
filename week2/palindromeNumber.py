# Write a program to check if the given number is a palindrome number.
# A palindrome number is a number that is same after reverse.


userIn = input('Enter a palindrome number : ')

reversedIn = (userIn[::-1])
if userIn == reversedIn:
    print('PALINDROME')
else:
    print('NOT PALINDROME')

# -------------------------------------------------------------------------------------------
numbers = input('Please enter a number that has at least three characters: ')    #JONOTHAN'S GROUP

try:
    checkInt = int(numbers)

    if len(numbers) > 2:
        palindrome = numbers[::-1]
        if numbers == palindrome:
            print('The number %s is a palindrome!' % numbers)
        else:
            print('The number %s is not a palindrome!' % numbers)
    else:
        print('Invalid entry.')
except:
    print('Invalid entry.')

# ---------------------------------------------------------------------------------------------
word = input("Enter a word. ")                                                         #JONOTHAN'S GROUP
half = len(word)/2
half = int(half)

print(word[0:half+1])
print(word[len(word):half-1:-1])

if word[0:half+1] == word[len(word):half-1:-1]:
    print("It is a palindrome. ")
else:
    print("Not a palindrome. ")