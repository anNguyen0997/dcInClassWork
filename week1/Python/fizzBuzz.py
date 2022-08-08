
# number = 1
# while number <= 100:
#     if number % 3 == 0 and number % 5 == 0:
#         print('FIZZ')
#     elif number % 5 == 0:
#         print('BUZZ')
#     elif number % 3 == 0:
#         print('FIZZBUZZ')
    
#         print(number)
#         number = number + 1


for num in range(1,101):
        if num % 15 == 0:
            print('fizzbuzz')
        elif num % 5 == 0:
            print('buzz')
        elif num % 3 == 0:
            print('fizz')
        else:
            print(num)