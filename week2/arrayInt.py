# Given an array of numbers, sort the integers from least to greatest

intArray = [9, 5, 7, 6, 8, 3, 12]

# loop through the array from the start to the end using len()
for i in range(0, len(intArray)):
    # print(intArray[i])

    # nested loops to compare each index
    # second loop will take current index and compare to 1st loop index
    for x in range(i, len(intArray)):
        currentIn = intArray[x]
        print(currentIn)

        # if current index from 1st loop is > index from 2nd loop

