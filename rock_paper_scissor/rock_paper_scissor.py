import random as r

from sympy import comp

def rock_paper_scissor():
    #computer = r.choice(['r','p','s'])
    cases = ['r','p','s']
    computer = r.choice(cases)
    human = input("Play r(rock), p(paper) and s(scissors): ")
    if human == computer:
        print(f"The Computer choice is: {computer.upper()}.\nYour choice is: {human.upper()}.\nYou tied!!!")
    elif(is_win(human,computer)):
        print(f"The Computer choice is: {computer.upper()}\nYour choice is: {human.upper()}\nCongrats! You've won!!! {human.upper()} beats {computer.upper()}")
    else:
        print(f"The Computer choice is: {computer.upper()}\nYour choice is: {human.upper()}\nDaamn! You've lost!!! {computer.upper()} beats {human.upper()}")

def is_win(human, computer):
    if (human == 'r' and computer == 's') or (human == 'p' and computer == 'r') or (human=='s' and computer =='p'):
        return True
    else:
        return False


#Start the game here:
print("****************WELCOME TO ROCK, PAPER, SCISSOR GAME********************")
rock_paper_scissor()
choice = ''
while choice.lower() != 'n':
    choice = input("Do you want to play again? yes(y) or no(n): ")
    if choice.lower() == 'y':
        rock_paper_scissor()
    else:
        print("*****************************GAME OVER!!!*******************************")
        break
