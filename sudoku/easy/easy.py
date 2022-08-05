def solve(puzzle):
    #solve sudoku using backtracking
    #Our puzzle is a list of lists where each sublist is a row of the puzzle
    #Return whether or not the puzzle is solvable
    #If the puzzle is solvable, return the solution
    #If the puzzle is not solvable, return None


    #Step 1: Choose somewhere in the puzzle to make a guess

    row, col = find_next_empty(puzzle)

    if row == None: #if there's no empty space in the puzzle, then the puzzle is solved
        return True
    

    #Step 2: If there's an empty space, try all possible values for that space

    for guess in range(1, 10):
        #Step 3: If the guess is correct, go to step 1
        if is_valid(puzzle, guess, row, col):
            #Step 3.1: If the guess is correct, place it in the puzzle and go to step 1
            puzzle[row][col] = guess
            if solve(puzzle):
                return True
        
        #Step 4: If the guess is incorrect, OR if the guess doesn't solve the puzzle, then
        #remove the guess from the puzzle and go to step 2
        puzzle[row][col] = -1
    

    #Step 5: If there are no possible values for the empty space, then the puzzle is unsolvable
    return False








#finds the next empty space(row, col) in the puzzle that's not already filled(represented by a -1)
#Returns row, col tuple (or None if (None, None)if there's no empty space)
def find_next_empty(puzzle):
    for row in range(9):
        for col in range(9):
            if puzzle[row][col] == -1:
                return row, col

    #There's no empty space in the puzzle
    return None, None

#checks if the guess is valid for the given row, col
def is_valid(puzzle, guess, row, col):

    #take all the values in the row and check if the guess is in there
    row_values = puzzle[row]
    if guess in row_values:
        return False
    

    #take all the values in the column and check if the guess is in there
    col_values = []
    #for i in range(9):
        #col_values.append(puzzle[i][col])
    col_values = [puzzle[i][col] for i in range(9)]

    if guess in col_values:
        return False

    #take all the values in the 3x3 box and check if the guess is in there
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3

    for r in range(row_start, row_start+3):
        for c in range(col_start, col_start+3):
            if puzzle[r][c] == guess:
                return False
    

    #if the guess is valid, return True
    return True