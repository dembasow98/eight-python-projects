import random as r


def guess_a_number(minimum,maximum):

    #Generate the random number:
    random_number = r.randint(minimum,maximum)

    #Initialize the guessed number
    guessed_number = 0

    while guessed_number != random_number:
        guessed_number = int(input(f"Guess  a number between {minimum} and {maximum}: "))
        #Some controls:
        if guessed_number < minimum or guessed_number > maximum:
            print(f"The number must be between {minimum} and {maximum}.")
        elif guessed_number < random_number:
            print("This number is lower! Please guess a higher number!!!")
        elif guessed_number > random_number:
            print("This number is higher! Please guess a lower number!!!")
    #Display the guessed number:
    print(f"Well done! You've guessed the number {guessed_number} correctly!!!")

print("**********WELCOME TO NUMBER GUESSING GAME****************")

#Execute the function:
minimum = int(input("Enter the minumum number: "))
maximum = int(input("Enter the maximum number: "))

guess_a_number(minimum,maximum)


print("**********GAME OVER****************")
