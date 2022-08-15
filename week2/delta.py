import random

class Flight():                                             # Flight class
    def __init__(self):
        self.happinessMeter = 100                           # Happiness meter will start at 100
        self.delayedFlight = 0
        self.turn = 0
        self.passengersToKick = 6
        
    def stats(self):                                        # show stats functin for every round
        print(' - Turns: %d' % turn)
        print(' - Happiness: %d' % self.happinessMeter)
        print(' - Passengers to remove: %d' % self.passengersToKick)
        if self.delayedFlight > 0 :
            print('Curent Delay: %d' % self.delayedFlight)


class First(Flight):                                        # First Class class
    def __init__(self): 
        self.negativeReview = 80                        # 80% chance of negative review
        self.refuseMove = 50                            # 50% chance of refusing to removed from flight (?)
        self.violent = 1                                # 1% chance of punching flight attendant
        self.passengers = 8

class Business(Flight):                                     # Business class                   
    def __init__(self):
        self.negativeReview = 70             # 70% chance of negative review 
        self.refuseMove = 30                 # 30% chance of refusing to removed from flight (?)
        self.violent = 2                     # 2% chance of punching flight attendant  
        self.passengers = 12

class Comfort(Flight):                                      # ComfortPlus class
    def __init__(self):
        self.negativeReview = 50       # 50% chance of negative review
        self.refuseMove = 20            # 20% chance of refusing to removed from flight (?)
        self.violent = 5               # 5% chance of punching flight attendant
        self.passengers = 20  

class Economy(Flight):                                      # Economy class
    def _init__(self):
        self.negativeReview = 10        # 10% chance of negative review
        self.refuseMove = 10            # 10% chance of refusing to removed from flight (?)
        self.violent = 15               # 15% chance of punching flight attendant
        self.chuckNorris = 5            # 5% special ability to knock out a flight attendant which will cancel flight
        self.passengers = 24



def firstClassActions(negativeReview, refuseMove, violent):     # function for first class
        
        for passengers in range(1, 9):
            print('Passenger : ', passengers)
            
            refuse = random.randint(1, 100)
            punch = random.randint(1, 100)
            negRev = random.randint(1, 100)

            if refuse <= refuseMove:
                flight.delayedFlight += 5
                print('Passenger has refused to move and cause a 5 minutes delay!')

            elif negRev <= negativeReview:
                flight.happinessMeter -= 1
                print('Negative review recieved!')

            elif punch == violent:
                flight.happinessMeter -= 10
                print('Oh no! A flight attendant has been punched!')

            else:
                flight.passengersToKick -= 1
                print('Passenger kindly leaves the flight.')
        passengers += 1

def businessActions(negativeReview, refuseMove, violent):       # function for business class
        for passengers in range(9, 21):
            print('Passenger : ', passengers)
            
            refuse = random.randint(1, 100)
            punch = random.randint(1, 100)
            negRev = random.randint(1, 100)

            if refuse <= refuseMove:
                flight.delayedFlight += 5
                print('Passenger has refused to move and cause a 5 minutes delay!')

            elif negRev <= negativeReview:
                flight.happinessMeter -= 1
                print('Negative review recieved!')

            elif punch == violent:
                flight.happinessMeter -= 10
                print('Oh no! A flight attendant has been punched!')

            else:
                flight.passengersToKick -= 1
                print('Passenger kindly leaves the flight.')
        passengers += 1

def comfortActions(negativeReview, refuseMove, violent):        # function for comfort class
        for passengers in range(21, 41):
            print('Passenger : ', passengers)
            
            refuse = random.randint(1, 100)
            punch = random.randint(1, 100)
            negRev = random.randint(1, 100)

            if refuse <= refuseMove:
                flight.delayedFlight += 5
                print('Passenger has refused to move and cause a 5 minutes delay!')

            elif negRev <= negativeReview:
                flight.happinessMeter -= 1
                print('Negative review recieved!')

            elif punch == violent:
                flight.happinessMeter -= 10
                print('Oh no! A flight attendant has been punched!')

            else:
                flight.passengersToKick -= 1
                print('Passenger kindly leaves the flight.')
        passengers += 1

def economyActions(negativeReview, refuseMove, violent, chuck): # function for economy class
        for passengers in range(41, 65):
            print('Passenger : ', passengers)
            
            refuse = random.randint(1, 100)
            punch = random.randint(1, 100)
            negRev = random.randint(1, 100)
            knockOut = random.randint(1, 100)

            if refuse <= refuseMove:
                flight.delayedFlight += 5
                print(' - Passenger has refused to move and cause a 5 minutes delay!')

            elif negRev <= negativeReview:
                flight.happinessMeter -= 1
                print(' - Negative review recieved!')

            elif punch == violent:
                flight.happinessMeter -= 10
                print(' - Oh no! A flight attendant has been punched!')

            elif knockOut <= chuck:
                print('Oh no! A flight attendant just got knocked out!')
                flight.happinessMeter  -= 100

            else:
                flight.passengersToKick = flight.passengersToKick - 1
                print('Passenger kindly leaves the flight.')

        passengers += 1



# Running the simulator
flight = Flight()
turn = flight.turn

def simulator():
    
    while flight.happinessMeter > 70 and flight.passengersToKick > 0 :      # condition for the simulator
        print('---------------------------------------')
        print('\n -----  Delta Airlines Classes  -----')
        flight.stats()
        print('''\n1 - First Class
2 - Business Class
3 - Comfort +
4 - Economy
5 - Close menu''')

        userIn = input('\n- Select a class to remove passengers from : ')

        if userIn == '1':
            flight.stats()
            firstClassActions(80, 50, 1)
        elif userIn == '2':
            flight.stats()
            businessActions(70, 30, 2)
        elif userIn == '3':
            flight.stats()
            comfortActions(50, 20, 5)
        elif userIn == '4':
            flight.stats()
            economyActions(10, 10, 15, 5)
        elif userIn == '5':
            pass
      
    if flight.delayedFlight % 30 == 0 and flight.delayedFlight > 0 :
            flight.delayedFlight -= 3

    if flight.passengersToKick == 0 and flight.happinessMeter >= 70:
            print('Success')
    if flight.passengersToKick == 0 and flight.happinessMeter < 70:
            print('Failed')

simulator()