#Functions
# - a reusable block of that can be called at any time

#user will pass in parameter(s) within __()
name = input('What is your name? ')

def hey(userName):                                     #def - definition
    print('Hey', userName)
hey(name)

