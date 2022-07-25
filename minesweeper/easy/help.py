import random
def plant_bombs(self, board):
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