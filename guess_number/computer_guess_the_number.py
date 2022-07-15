import random as r


def guess_a_number(low, high):
    feedback = ''
    while feedback != 'c':
        if low != high:
            guessed_number = int(r.randint(low,high))
        else:
            guessed_number = low #or guessed_number = low(because min = max)

        feedback = input(f"Is {guessed_number} high(H/h), low(L/l) or correct(c/C)? ")
        if feedback == 'h':
            high = guessed_number - 1
        elif feedback == 'l':
            low = guessed_number + 1
    print(f"Congrats Computer! You've guessed the number {guessed_number} correctly!")

#I'll run the project here
lowest = int(input("Enter the lowest number? "))
highest = int(input("Enter the highest number? "))
guess_a_number(lowest,highest)