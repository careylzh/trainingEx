#put your usual code inside the try block:
# while True:
#     try:
#         a = int(input('Enter an integer : '))
#         print("You enter ")
#     except ValueError:
#         print("valueError!!!")
#     except IOError:
#         print('please give a valid file')

#Exercises: throw exceptions to use 
import random
die = random.choice([1,2,3,4,5,6])

while True: 
    try:
        a = int(input('Guess a number of the dice: '))
        if(a == die):
            print('You are right')
            break
        else:
            print("no luck, try again!")
    except ValueError:
        print('please give valid number')




 # https://plotly.com/python/radar-chart/
