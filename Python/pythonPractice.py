idNumber = int(input('enter ID number : '))
 
if idNumber <= 100 and idNumber >= 1:
    print('1st')
elif idNumber > 100 and idNumber <= 250:
    print('2nd')
elif idNumber > 250:
    print('ALL RESERVATIONS TAKEN')
else :
    print('not a number')