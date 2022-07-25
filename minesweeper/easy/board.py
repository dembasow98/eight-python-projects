import random

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        #let's create a board using a helper function
        self.board = self.make_new_board()
        #let's assign values to the board
        self.assign_values_to_board()


        #Initalize  a set to keep track of which squares is uncovered, we'll save (row, col) tuples into the set
        self.dug = set() #if we dig at (1,1) we'll add (1,1) to the set ->self.dug = {(1,1)}
    
    def make_new_board(self):
        #Construct a new board based on dim_size and num_bombs:
        #We should construct a list of lists, since we have a 2D board, list of lists is more appropriate


        board = [[None for _ in range (self.dim_size)] for _ in range (self.dim_size)] 
        #This create a bord of size dim_size x dim_size, with each element being None
        #[[None, None, None, None, None, None, None, None, None, None],
        # [None, None, None, None, None, None, None, None, None, None],
        # [None, None, None, None, None, None, None, None, None, None],
        #............................................................
        # [None, None, None, None, None, None, None, None, None, None]]

        #Todo: pass the board to the plant_bombs function
        #self.plant_bombs(board)
        #Plant bombs on the board, return the number of bombs planted
        bombs_planted = 0

        while bombs_planted < self.num_bombs:
            
            #return a random integer N such that a <= N <= b(a = 0 and b = largest possible number in the list)
            location = random.randint(0, self.dim_size**2 - 1) 

            row = location // self.dim_size #we want the number of times the dim_size goes into location to tell us the row
            column = location % self.dim_size  #we want the remainder of location divided by dim_size to tell us the column

            if board[row][column] == '*':
                #This means we actually planted a bomb at this location, so we should skip this location
                continue
            #else:
            board[row][column] = '*' #plant a bomb at this location
            bombs_planted += 1

        return board
    
    def assign_values_to_board(self):
        #After the bombs are planted, we should assign values to the board(number of bombs in the 8 neighboring squares)
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c] == '*':
                    #This means we have a bomb at this location, so we should skip this location
                    continue
                #else: we have a non-bomb location, so we should assign a value to it
                self.board[r][c] = self.get_neighboring_bombs_count(r, c)
    

    def get_neighboring_bombs_count(self, row, column):
        #Return the number of bombs in the 8 neighboring squares of the given location
        #Let's iterate through the 8 neighboring squares of the given location and sum the number of bombs
        #top lef: (row - 1, column - 1) 
        #top: (row - 1, column)
        #top right: (row - 1, column + 1)
        #left: (row, column - 1)
        #righ:  (row, column + 1)
        #bottom left: (row + 1, column - 1)
        #bottom: (row + 1, column)
        #bottom right:  (row + 1, column + 1)

        num_neighboring_bombs = 0
        #for r in range(row - 1, (row + 1) + 1):
            #for c in range(column - 1, (column + 1) + 1):
                #if r < 0 or c < 0 or r >= self.dim_size or c >= self.dim_size:
                    #This means we are out of bounds, so we should skip this location
                    #continue
                #if self.board[r][c] == '*':
                    #num_bombs += 1
        
        #This means we are out of bounds, so we should skip this location
        for r in range(max(0, row - 1), min(self.dim_size - 1, (row + 1) + 1)):
            for c in range(max(0, column - 1), min(self.dim_size - 1, column + 1) + 1):
                if r == row and c == column:
                    #Our current location, so we should skip this location
                    continue
                if self.board[r][c] == '*':
                    num_neighboring_bombs += 1

        return num_neighboring_bombs


    def dig(self, r, c):
        #dig at the given location, return the number of bombs in the 8 neighboring squares
        #if the location is already dug, return 0
        #if the location is a bomb, return -1(game over) 
        #if the location is not a bomb, return the number of bombs in the 8 neighboring squares
        
        self.dug.add((r,c)) #keep track of which squares we dug

        if self.board[r][c] == '*':
            return False #return -1
        elif self.board[r][c] > 0:
            return True #we dug a non-bomb location, so return True(neighboring bombs)
        
        #else: self.board[row][column] == 0
        for r in range(max(0, r - 1), min(self.dim_size - 1, (r + 1) + 1)):
            for c in range(max(0, c - 1), min(self.dim_size - 1, c + 1) + 1):
                if (r,c) in self.dug:
                    continue  #Don't dig at this location, since we already dug it
                #else: dig at this location
                self.dig(r,c) #Continue digging at this location until we reach a non-bomb location
        return True #If our initial dig didn't hit a bomb, we *shouldn't* hit a bomb, so we should return True


    def __str__(self):
        #This is a magic method, it's called whenever we print an object of type Board
        #It's used to print the board as a string representation to the player


        visible_board = [[None for _ in range (self.dim_size)] for _ in range (self.dim_size)]
        #This create a bord of size dim_size x dim_size, with each element being None
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if (r , c) in self.dug:
                    visible_board[r][c] = str(self.board[r][c])
                else:
                    visible_board[r][c] = ' '
            
        #Todo: put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(len(max(columns, key = len)))

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
        
    #def display(self):
    #   print(self)