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
from itertools import product, cycle
from pprint import pprint, pformat
from .Piece import Piece
'''
sample = lambda num_samples: random.choices(PIECES, list(WEIGHTS.values()), k=num_samples)

import matplotlib.pyplot as plt
plt.hist(sample(10000))
plt.show()
'''

class Board:
    def __init__(self, board_size=8, pool_size=12, num_players=2):
        self.board_size = board_size
        self.pool_size = pool_size
        self.board = []
        for i in range(self.board_size):
            self.board.append(["+"] * self.board_size)
        self.active_pieces = []
        self.init_board()
        self.phase = 1
        self.num_players = num_players
        self.turn_count = 0
        self.turn_cycle = cycle(range(self.num_players))
        self.inactive_pieces = []
        self.winner = None
        self.game_complete = False
        self.turn = 0
    def init_board(self):
        valid_positions = list(product(list(range(self.board_size)), list(range(self.board_size))))
        chosen_positions = list()
        for piece in range(self.pool_size):
            pos = random.choice(valid_positions)
            chosen_positions.append(pos)
            valid_positions.remove(pos)
        #print(valid_positions[0])
        sampled_pieces = self.sample(self.pool_size)
        for i, (pos, sampled_piece) in enumerate(zip(chosen_positions, sampled_pieces)):
            #print(pos)
            p = Piece(sampled_piece, pos, self, i)
            self.board[pos[0]][pos[1]] = p
            self.active_pieces.append(p)
        
    def sample(self, num_samples):
        return random.choices(PIECES, list(WEIGHTS.values()), k=num_samples)

    def get_tile(self, pos):
        return self.board[pos[0]][pos[1]]

    def delete_piece(self, pos):
        assert(self.board[pos[0]][pos[1]] != "+")
        piece = self.board[pos[0]][pos[1]]
        for i, p in enumerate(self.active_pieces):
            if p.id == piece.id:
               ind = i
               break
        del self.active_pieces[ind] 
        self.board[pos[0]][pos[1]] = "+"

    def get_active_pieces(self):
        return self.active_pieces

    def pos_to_pid(self, pos):
        return self.board[pos[0]][pos[1]].id

    def pick_piece(self, pos, player_id):
        #print(player_id)
        assert(self.phase == 1)
        t = next(self.turn_cycle)
        assert(t == player_id)
        self.turn = t
        pid = self.pos_to_pid(pos)
        self.active_pieces[pid].owner = player_id
        self.turn_count += 1
        if self.turn_count == self.pool_size:
            self.phase = 2
            self.turn_count = 0
            self.turn = 0
            self.turn_cycle = cycle(range(self.num_players))

    def move_piece(self, old_pos, target_pos, player_id):
        assert(self.phase == 2)
        t = next(self.turn_cycle)
        assert(t == player_id)
        
        old_p = self.board[old_pos[0]][old_pos[1]]
        self.temp_valid_moves = old_p.get_valid_moves()
        
        assert(target_pos in self.temp_valid_moves)        
        
        self.turn_count += 1
        
        target_tile = self.get_tile(target_pos)
        

        if isinstance(target_tile, str):
            pass
        else:
            self.delete_piece(target_pos)
        for i, piece in enumerate(self.active_pieces):
            if piece.id == old_p.id:
                break
        self.active_pieces[i].position = target_pos
        self.board[target_pos[0]][target_pos[1]] = self.active_pieces[i]
        self.board[old_pos[0]][old_pos[1]] = "+"
        players_remain = set()
        for item in self.active_pieces:
            players_remain.add(item.owner)
        if len(players_remain) == 1:
            self.phase = 3
            self.winner = next(iter(players_remain))
            self.game_complete = True

    def get_valid_moves(self, pos):
        tile = self.board[pos[0]][pos[1]]
        assert(isinstance(tile, Piece))
        self.temp_valid_moves = tile.get_valid_moves()
        return self.temp_valid_moves
    
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
    for i in range(board.pool_size):
        board.pick_piece(i, i % 2)
    print(board)
    
