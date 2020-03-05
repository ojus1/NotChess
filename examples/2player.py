import random
import sys
sys.path.append("../NotChess")

from NotChess import Board

# Setting a seed to generate the same board everytime this file is ran
random.seed(420) # Blaze it B)
'''
_̅┌─_̅(̲̲(̅_̅_̲̅м̲̅a̲̅я̲̅i̲̅j­­u̲̅a̲̅n̲̅a̲̅_̅_̅_̅()ڪے
　│▒│ /▒/
　│▒│/▒/
　│▒ /▒/─┬─┐
　│▒│▒|▒│▒│
┌┴─┴─┐-┘─┘
│▒┌──┘▒▒▒│
└┐▒▒▒▒▒▒┌┘
　└┐▒▒▒▒┌┘
'''

# Initialize the Board
board = Board(
    num_players=2, # Number of Players
    board_size=4, # Size of the Board (2x2)
    pool_size=4 # Number of Pieces in board to generate
    )

print(board) # Print Current Board State
# + is an empty tile
# Pieces sufixed by an asterisk(*) are pieces that don't currently belong to any player 
# and are up for grabs

print("Active Pieces:", board.active_pieces) # Print the list of pieces that in currently in the board
print("Current Turn for Player", board.turn) # Who's turn is it? 
print("Number of turns played:", board.turn_count) # How many turns have been played till now?
print("Current Game Phase:", board.phase) # What phase of game is it?
# Phase 1 = Drafting Phase
# Phase 2 = Playoff Phase
# Phase 3 = Finished Phase (Game complete, winners and losers decided)


board.pick_piece((1, 2), 0) # Pick the piece at position (1, 2) for player 0
print(board) # Notice one of the Knights names is suffixed by 0, that piece is owned by Player 0

board.pick_piece((0, 0), 1)
board.pick_piece((2, 3), 0)
board.pick_piece((3, 2), 1)
print("--------------------Phase 2--------------------")
print("Active Pieces:", board.active_pieces) # Print the list of pieces that in currently in the board

# Phase 1 is now over
print(board)
print("Current Turn for Player", board.turn) # Who's turn is it? 
print("Number of turns played:", board.turn_count) # How many turns have been played till now?
print("Current Game Phase:", board.phase) # What phase of game is it?

print("List of valid moves for (2, 3): ", board.get_valid_moves((2, 3))) 
board.move_piece((2, 3), (3, 2), 0) # move the piece at (2, 3) to (3, 2). Pawn0 kills the Knight1
print("Active Pieces:", board.active_pieces) # Print the list of pieces that in currently in the board
board.move_piece((0, 0), (1, 0), 1)
board.move_piece((3, 2), (3, 1), 0)
board.move_piece((1, 0), (2, 0), 1)
board.move_piece((1, 2), (2, 0), 0)
print(board)
print("Is the game over?:", board.game_complete) # Has the game concluded?
print("Current Game Phase:", board.phase) # What phase of game is it?
print("Winner: Player", board.winner)

#board.move_piece((1, 2), (0, 1), 0)
#board.move_piece((, 3), (2, 2), 1)