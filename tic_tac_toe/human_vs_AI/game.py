from human import Human
from AI import AI

import time as t

class TicTacToe:
    def __init__(self):

        #The game board
        self.board = [' ' for i in range(9)] #Single list 3x3 to represent our board
        self.current_winner = None #keeps track of the winner(if there's one)

    def display_board(self):
        #Get the rows of the board
        for row in [self.board[i * 3 : (i + 1) * 3] for i in range(3)]:
            print('| '+' | '.join(row)+ ' |')


    #static method because it doesn't relate to any specific board
    @staticmethod
    def display_board_spot_indexes(): #We'll track which number corresponds to which spot
        board_spot_index  = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in board_spot_index:
            print('| '+' | '.join(row)+ ' |')


    def available_spots(self):
        #moves = []
        #for(index, spot) in enumerate(self.board): # | X | O | X | -->(0, 'X') (1, 'O') (2, 'X')
            #if spot == ' ':
                #moves.append(index)
        #return moves
        return [index for index, spot in enumerate(self.board) if spot == ' ']

    def empty_spots(self):
        return ' ' in self.board
    

    def empty_spots_count(self):
        #return len(self.available_spots())
        return self.board.count(' ')

    def make_move(self, spot, letter):
        if self.board[spot] == ' ':
            self.board[spot] = letter

            #Check if there's a winner or not:
            if self.winner(spot, letter):
                self.current_winner = letter
            return True
        return False

    #if there's 3 same letters in a row everywhere:
    #We have to check all the posibilities:
    def winner(self, spot, letter):
        #let's check the row:
        row_index =  spot // 3
        row = self.board[row_index * 3 : (row_index + 1) * 3]

        if all([square == letter for square in row]):
            return True
        

        #let's check the column:
        column_index = spot % 3
        column = [self.board[column_index + i * 3] for i in range(3)]
        
        if all([square == letter for square in column]):
            return True
        

        #let's check the diagnols:
        #first we'll check if the lattest move was in the diagnol spot:(0, 2, 4, 8)
        #That means even spot:
        if spot % 2 == 0:

            first_diagonal = [self.board[i] for i in [0, 4, 8]]
            if all([square == letter for square in first_diagonal]):
                return True

            second_diagonal = [self.board[i] for i in [2, 4, 6]]
            if all([square == letter for square in second_diagonal]):
                return True


        #If all the checks above are false; there's no win yer
        return False



def play(game, x_player, o_player, display = True):

    if display:
        game.display_board_spot_indexes()

    letter = 'X' #Starting letter(for human)

    #iterate while the game has an empty spot or there's a win:
    while game.empty_spots():
        if letter == 'O':
            spot = o_player.get_move(game)
        else:
            spot = x_player.get_move(game)
        

        #Define a function to make a next move!
        if game.make_move(spot, letter):
            if display:
                print(letter + ' has made a move to the spot number {}.'.format(spot))
                game.display_board()
                print('') #just an empry line

            if game.current_winner:
                if display:
                    print(letter + ' has won!!!')
                return letter #end the loop and return the winner(letter)

            #After making the move we need to alternate the letters:
            letter = 'O' if letter == 'X' else 'X'
            #if letter == 'X':
                #letter = 'O'
            #else:
                #letter = 'X'

            #Wait for the computer to make it's move
            print('Wait for the AI to make it\'s move...')
            t.sleep(.8)
    if display:
        print('It\'s tie!!!')




#LET'S PLAY THE GAME:


if __name__ == '__main__':

    
    x_player = Human('X')
    o_player = AI('O')
    

    game = TicTacToe()

    play( game,x_player, o_player,display=True)