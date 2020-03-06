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

enum_PIECES = {'<empty>': 0}
for i, item in enumerate(PIECES, 1):
    enum_PIECES[item] = i


#print(sum(WEIGHTS.values()))
import random
from itertools import product, cycle
from pprint import pprint, pformat
from .Piece import Piece
from copy import deepcopy
'''
sample = lambda num_samples: random.choices(PIECES, list(WEIGHTS.values()), k=num_samples)

import matplotlib.pyplot as plt
plt.hist(sample(10000))
plt.show()
'''
backup = None

def roll_back():
    return backup

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
        global backup
        backup = deepcopy(self)
        
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
        global backup
        backup = deepcopy(self)
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
        global backup
        backup = deepcopy(self)
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
    
    def board_state(self, player=0):
        rows = list()
        for i in range(self.board_size):
            row = list()
            for j in range(self.board_size):
                tile = self.board[i][j]
                if isinstance(tile, str):
                    piece_encoded = Board.one_hot(enum_PIECES['<empty>'], len(enum_PIECES))
                    player_encoded = Board.one_hot(None, self.num_players) 
                else:
                    piece_encoded = Board.one_hot(enum_PIECES[tile.piece_type], len(enum_PIECES))
                    player_encoded = Board.one_hot(tile.owner, self.num_players) 
                player_encoded = Board.swap_player(player, player_encoded, p2=0)
                tile_encoded = piece_encoded + player_encoded
                row.append(tile_encoded)
            rows.append(row)
        return rows, self.game_complete

    def all_valid_moves(self, player):
        moves = list()
        for piece in self.active_pieces:
            if piece.owner == player:
                moves_per_piece = piece.get_valid_moves()
                moves += [(piece.position, item) for item in moves_per_piece]
        return moves
    
    @staticmethod
    def swap_player(p1, player_encoded, p2=0):
        temp = player_encoded[p2]
        player_encoded[p2] = player_encoded[1]
        player_encoded[1] = temp
        return player_encoded

    @staticmethod
    def one_hot(x, size):
        temp = [0] * size
        if x is not None:
            temp[x] = 1
        return temp

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
    print(board.board_state())
