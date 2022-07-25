from board import Board
import re

#Easy: https://www.hackerrank.com/challenges/minesweeper/problem 10/8 bombs = 10
#Medium: https://www.hackerrank.com/challenges/minesweeper/problem 18/14 bombs = 40
#Hard: https://www.hackerrank.com/challenges/minesweeper/problem 24/20  bombs = 99
def play(dim_size = 10, num_bombs = 10):
    #step 1: create a board and plant bombs
    board = Board(dim_size, num_bombs)



    #Define a variable to control if the dug location is safe or not
    safe = True
    #step 2: display the board and ask the user for where they want to dig
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        #board.display()
        print(board)
        user_input = re.split(',(\\s)*',input("Where do you want to dig? Input as row,column between 0 and {}:".format(dim_size - 1)))
        row, column = int(user_input[0]), int(user_input[-1])

        if row < 0 or row >= dim_size or column < 0 or column >= dim_size:
            print("Invalid location! Please dig again.")
            continue


        #step 3: 
            # a)if the user digs a bomb, show game over
            #if the input is valid, dig at the location
        safe = board.dig(row, column)
        if not safe:
            #Game over
            break
    
    # b)if the user digs a safe square, dig recursively until each square is at least next to a bomb.
    #step 4: repeat the step 3 until there are no more places to dig ->Victory:
    if safe:
        #board.display()
        print("YOU DUG ALL THE SAFE SQUARES! CONGRATULATIONS!!! YOU WIN!")
    else:
        #board.display()
        board.dug = [(row,column) for row in range(dim_size) for column in range(dim_size)]
        print(board)
        print("YOU DUG A BOMB! GAME OVER!")







if __name__ == '__main__': #this is the main function: We want to run this code only if this file is run directly
    play()
