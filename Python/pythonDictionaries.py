student1 = {
    "id": 59133,
    "name": 'Carlos',
}

student2 = {
    "id": 12132,
    "name": 'Fiona',
}

student3 = {
    "id": 69123,
    "name": 'Matt',
}

student4 = {
    "id": 20123,
    "name": "Jorge",
}

student5 = {
    "id": 31231,
    "name": 'Jonathan',
}

allStudents = [student1, student2, student3, student4, student5]
studentList = []

def listID(dcList):
    for student in dcList:
        currStudent = int(student["id"])
        if currStudent < 50000:
            studentList.append(student)
    return studentList

newList = listID(allStudents)
print(newList)
    
# def sortedList(oldList : list) -> list:
#     newList = []
#     topNumber = 0

#     for i in oldList:
#         idNum = int(i['id'])
#         print(idNum)
#         if idNum > topNumber:
#             topNumber = idNum
#             newList.append(i)

#         elif idNum < topNumber:
#             x = 0
#             while x < len(newList):
#                 newIdNum = int(newList[i]['id'])
#                 if idNum < newIdNum:
#                     newList.insert(x, i)
#                 x = x + 1
#     print(newList)
# newList = sortedList(allStudents)
    
