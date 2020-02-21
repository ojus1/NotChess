PIECES = (
    'q',
    'p',
    'k',
    'b',
    'r',
)

'''
COST = {
    'q': 10,
    'p': 2,
    'k': 6,
    'b': 6,
    'r': 6
}
'''
WEIGHTS = {
    'q': 0.04,
    'p': 0.5,
    'k': 0.17,
    'b': 0.15,
    'r': 0.11,
}

#print(sum(WEIGHTS.values()))
import random
from itertools import product
from pprint import pprint, pformat
'''
sample = lambda num_samples: random.choices(PIECES, list(WEIGHTS.values()), k=num_samples)

import matplotlib.pyplot as plt
plt.hist(sample(10000))
plt.show()
'''
class Piece:
    def __init__(self, piece_type, position, board, owner=None):
        self.piece_type = piece_type
        self.owner = owner
        self.position = position
        self.board = board
        self.valid_moves = []

        #self.update_valid_moves()
    
    def update_valid_moves():
        raise NotImplementedError

    def move(self, target_position):
        if target_position in self.valid_moves:
            self.position = target_position
            if self.board.get_piece(target_position) != "+":
                self.board.delete_piece(target_position)
    
    def __repr__(self):
        if self.owner:  
            return self.piece_type + str(self.owner)
        else:
            return self.piece_type + "*"
    
    def __add__(self, other):
        if isinstance(other, str):
            if self.owner:
                return other + self.piece_type + str(self.owner)
            else:
                return other + self.piece_type + "*"
    #def is_valid_move(self, target_position):
    #    if target_position[0] + target_position[1] >= 2:
    

class Board:
    def __init__(self, board_size=8, pool_size=12):
        self.board_size = board_size
        self.pool_size = pool_size
        self.board = []
        for i in range(self.board_size):
            self.board.append(["+"] * self.board_size)
        
        self.init_board()
    
    def init_board(self):
        valid_positions = list(product(list(range(self.board_size)), list(range(self.board_size))))
        chosen_positions = list()
        for piece in range(self.pool_size):
            pos = random.choice(valid_positions)
            chosen_positions.append(pos)
            valid_positions.remove(pos)
        #print(valid_positions[0])
        sampled_pieces = self.sample(self.pool_size)
        for pos, sampled_piece in zip(chosen_positions, sampled_pieces):
            #print(pos)
            self.board[pos[0]][pos[1]] = Piece(sampled_piece, pos, self)
    
    def sample(self, num_samples):
        return random.choices(PIECES, list(WEIGHTS.values()), k=num_samples)

    def get_piece(self, pos):
        return self.board[pos[0]][pos[1]]

    def delete_piece(self, pos):
        assert(self.board[pos[0]][pos[1]] != "+")
        self.board[pos[0]][pos[1]] = "+"
    
    #def insert_piece(self, piece, pos):
    @staticmethod
    def join(row1):
        row = []
        for item in row1:
            if isinstance(item, str):
                row.append(item + " ")
            else:
                row.append(item.__repr__())
        return " ".join(row)

    def __repr__(self):
        ret = []
        for i, row in enumerate(self.board):
            if i != 0:
                ret += "\n"
            #print(Board.join(row))
            ret.append(Board.join(row))
        return "".join(ret)
if __name__ == "__main__":
    board = Board()
    print(board)