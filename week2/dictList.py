# Create a list that holds the first name of everyone in this class, return any name that is duplicated

students = ['Carlos', 'Wes', 'Jordan', 'Fiona', 'Jonothan', 'Matt', 'Khanh', 'Jordan', 'An', 'Jorge', 'An']

def sameName(list):

    same = {}
    sameNameList = []

    for name in students:

        if name in same.keys():
            same[name] = same.get(name) + 1
        else:
            same[name] = 1

    for names in same.keys():
        if same.get(names) > 1:
            sameNameList.append(names)

    return sameNameList

print(sameName(students))


