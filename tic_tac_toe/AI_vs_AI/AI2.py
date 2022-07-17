# In this part of the game we're going to use the minimax algorithm:
# Minimax is a type of adversarial search algorithm for generating and exploring game trees. 
# It is mostly used to solve zero-sum games where one side’s gain is equivalent to other side’s loss,
# so adding all gains and subtracting all losses end up being zero.


from player import Player
import random, math



#Computer player that inherits the player class
class AIO(Player):
    def __init__(self, letter):
        super().__init__(letter)


    def get_move(self, board):
        #spot = random.choice(board.available_spots())
        #return spot
        #we can simply write:
        #return random.choice(board.available_spots())

        #if the game has just started(no moves yet: all the spots are available)
        if len(board.available_spots()) == 9:
            spot =  random.choice(board.available_spots())

        #there's already some occupied spots on the board: get the move according to the minimax algorithm
        else:
            spot = self.minimax(board, self.letter)['position']

        return spot



    def minimax(self, state, player):
        max_player = self.letter #yourself
        min_player = 'O' if max_player == 'X' else 'X' #the other player

        #Let's check if the previous move is a win:
        #Our base case will be:
        if state.current_winner == min_player:
            #We need to track the position and score of the minimax:
            return {
                'position':None,
                'score': 1 * (state.empty_spots_count() +1) if min_player == max_player else -1 * (state.empty_spots_count() + 1) 
            }

        #No winner but there's still empty spots:
        elif not state.empty_spots():
            return {
                'position': None,
                'score' : 0
            }

        #Let's get into the algorithm:

        if player == max_player: #each score should maximize
            best_case = {'position': None, 'score': -math.inf}
        else:                    #each score should minimize
            best_case = {'position': None, 'score': math.inf}
        
        for available_spot in state.available_spots():
            #step 1: Make a move and try that spot:
            state.make_move(available_spot, player)

            #step 2: recurse using minimax to simulate the game after making the move:
            simulated_case = self.minimax(state, min_player) #alternates the players

            #step 3: undo the move:
            state.board[available_spot] = ' '
            state.current_winner = None
            
            simulated_case['position'] = available_spot #otherwise this will get messed up from the recursion
            
            
            #step 4: update the dictionaries if necessary:
            if player == max_player:                                    #maximize max_player
                if simulated_case['score'] > best_case['score']:
                    best_case = simulated_case
            else:                                                       # minimize min_player(other player)
                if simulated_case['score'] < best_case['score']:
                    best_case = simulated_case

        return best_case