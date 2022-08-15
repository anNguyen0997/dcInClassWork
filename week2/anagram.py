# When given two srings, write a function that checks if each string is an anagram of the other
# If yes, return true, otherwise false

userIn1 = input("Enter the first word : ")
userIn2 = input("Enter the second word : ")

# using sorted()
def anagram(str1, str2):
    # sortedIn1 = sorted(str1)
    # sortedIn2 = sorted(str2)

    # sortedIn1 = sortedIn1.lowercase()
    # sortedIn2 = sortedIn2.lowercase()

    # if sortedIn1 == sortedIn2:
    #     print("The two words are anagrams.")
    # else:
    #     print("The two words are not anagrams of each other.")

# --------------------------------------------------------------------------------------------------------------------------
# not using sorted()

    for letters in str1:

        str1 = str1.replace(' ', '')
        str2 = str2.replace(' ', '')

        if letters not in str2:
            return False
        else:
            return True

if len(userIn1) != len(userIn2):
    print('NOT SAME LENGTH')
elif anagram(userIn1, userIn2) == True:
    print("is anagram")
else:
    print("is NOT anagram")

anagram(userIn1, userIn2)