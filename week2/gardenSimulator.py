# Create Tree, Gnome, Woodchucks, Garden Class
# Garden has seperate lists for Tree, Gnome, Woodchuck
import random
    

class Tree:                                                                     
    def __init__(self):                                          
        self.reduceWater = -2                                                          # one tree causes water level to decrease by 2
                                                    
class Gnome:
    def __init__(self):                                                                # gnome class 
        self.makeRain = 5                                                              # chance of gnomes making it rain
    
class WoodChuck():
    def __init__(self):                                              
        self.removesTree = 5                                                           # chance of woodchuck removing a tree = 5%

class Garden:                                                                          # garden class
    def __init__(self, trees, gnomes, woodchucks):
        self.trees = trees
        self.gnomes = gnomes
        self.woodchucks = woodchucks
        self.chanceOfRain = 5
        self.woodchucksappear = 5
        self.removeTree = 5
        self.waterLevel = 0
        self.chanceOfStorm = 2

    def chance(self):                                                                   # chance function, choosing a number between 0-100
        return random.randint(0, 100)

    def raining(self):                                                                  # rain function to increase water level
        self.waterLevel = self.waterLevel + 10

    def addWoodChucks(self):                                                            # function to add woodchucks
        chucks = WoodChuck()
        self.woodchucks = self.woodchucks + 1                                           # incrementing amount of woodchucks
        # self.removeTree = self.removeTree + chucks.removesTree                        # 

    def addGnomes(self):
        gnomes = Gnome()                                                                # adding gnomes and incrementing
        self.gnomes = self.gnomes + 1
        
    def addTree(self):
        tree = Tree()                                                                   # adding trees and incrementing
        self.trees = self.trees + 1

    # def storm(self):                                                                    # storm function to decrease gnome and woodchucks amount
    #     self.waterLevel = self.waterLevel + 60


turnTracker = 0
day = 1
myGarden = Garden(1, 1, 1)
myTree = Tree()

while myGarden.trees < 10:    
    print('--------------------------')  
    print("day: ", day)
    print("gnomes: ", myGarden.gnomes)
    print("woodchucks: ", myGarden.woodchucks)
    # print("water level: ", myGarden.waterLevel)
                                                                                                   
    # myGarden.waterLevel = myGarden.waterLevel - (myTree.reduceWater * myGarden.trees)    # everyday that goes by, water level will be subtracted by
                                                                                           # the amount of trees * reduceWater


    if turnTracker == 10:                                                                          # every 10th day, the days will reset
        turnTracker == 0

        chances1 = myGarden.chance()                                                       # chances of adding a tree or a gnome into garden
        if chances1 <= 99:
            myGarden.addTree()
            print('One tree added!')
        else:
            myGarden.addGnomes()
            print('One gnome added!') 
        

    chances2 = myGarden.chance()
    if chances2 <= myGarden.woodchucksappear:
        print('A woodchuck appeared!')                                                      # if there's a chance of a woodchuck moving into garden
        myGarden.addWoodChucks()
        
    
    chances3 = myGarden.chance()                                                            # if it will rain or not
    if chances3 <= 50:
        print('It is raining!')
        myGarden.raining()
    else:
        myGarden.addWoodChucks()

    # chances4 = myGarden.chance()                                                            # chances of a tree being removed by a woodchuck
    # if chances4 <= (myGarden.removeTree):
    #     print('Woodchucks removed a tree!')
    #     print('trees: ', myGarden.trees)                                                
    #     myGarden.trees = myGarden.trees - 1
    # else:
    #     print("trees: ", myGarden.trees)
        

    if myGarden.waterLevel > 100:                                                           # if water level is < 100, then a tree will be added
        myGarden.waterLevel = 0                                                             # and water level will be resetted
        myGarden.trees = myGarden.trees + 1
        print('Tree added!')

    if myGarden.trees == 10 or myGarden.trees < 0:
        break

    day += 1                                                                                # incrementing each day                                                       

if myGarden.trees == 10:    
    print('***********************')                                                
    print("\nWe got to 10 trees!")
    print("day: ", day)
    print("trees: ", myGarden.trees)
    print("gnomes: ", myGarden.gnomes)
    print("woodchucks: ", myGarden.woodchucks)
    print("water: ", myGarden.waterLevel)
    

if myGarden.trees < 0:
    print('***********************')         
    print("Oh no! There are no more trees!")
    print("day: ", day)
    print("trees: ", myGarden.trees)
    print("gnomes: ", myGarden.gnomes)
    print("woodchucks: ", myGarden.woodchucks)
    print("water level: ", myGarden.waterLevel)

