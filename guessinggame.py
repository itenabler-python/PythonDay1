
# import math
from random import *
# import math
# piv = math.pi

pinumber = random.pi()
print(pinumber)
# guess_number = 21
attempt = 0
secret_number = randint(1,20)
guess_number = secret_number + 1
# secret_number = 6
while (guess_number != secret_number):
    attempt += 1
    if attempt>6:
        break;
    guess_number = int(input("Please enter your guess number {}: ".format(attempt)))

    if(attempt <= 6):
        if(guess_number < secret_number):
            print("Guess a higher number")
        elif (guess_number > secret_number):
            print("Guess a lower number")
        else:
            print("Good guess")
