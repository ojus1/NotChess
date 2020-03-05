class Piece:
    def __init__(self, piece_type, position, board, pid, owner=None):
        self.piece_type = piece_type
        self.owner = owner
        self.position = position
        self.board = board
        self.id = pid
        
    def get_valid_moves(self):
        valid_moves = []
        if self.piece_type == "q":
            #Check for UP valid moves
            for i in range(self.position[0]+1, self.board.board_size):
                tile = self.board.board[i][self.position[1]]
                if isinstance(tile, str):
                    valid_moves.append((i, self.position[1]))
                elif tile.owner != self.owner:
                    valid_moves.append((i, self.position[1]))
                    break
                else:
                    break
            # Check for DOWN valid moves 
            for i in range(self.position[0]-1, -1, -1):
                tile = self.board.board[i][self.position[1]]
                if isinstance(tile, str):
                    valid_moves.append((i, self.position[1]))
                elif tile.owner != self.owner:
                    valid_moves.append((i, self.position[1]))
                    break
                else:
                    break
            
            #Check for RIGHT valid moves
            for i in range(self.position[1]+1, self.board.board_size):
                tile = self.board.board[self.position[0]][i]
                if isinstance(tile, str):
                    valid_moves.append((self.position[0], i))
                elif tile.owner != self.owner:
                    valid_moves.append((self.position[0], i))
                    break
                else:
                    break
            
            #Check for LEFT valid moves
            for i in range(self.position[1]-1, -1, -1):
                tile = self.board.board[self.position[0]][i]
                if isinstance(tile, str):
                    valid_moves.append((self.position[0], i))
                elif tile.owner != self.owner:
                    valid_moves.append((self.position[0], i))
                    break
                else:
                    break
            

            i, j = self.position
            while True:
                i, j = i-1, j-1
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    break
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
                    break
                else:
                    break
            
            #Check for LEFT DIAG DOWN valid moves
            i, j = self.position
            while True:
                i, j = i+1, j+1
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    break
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
                    break
                else:
                    break

            #Check for RIGHT DIAG UP valid moves
            i, j = self.position
            while True:
                i, j = i-1, j+1
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    break
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
                    break
                else:
                    break

            #Check for RIGHT DIAG DOWN valid moves
            i, j = self.position
            while True:
                i, j = i+1, j-1
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    break
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
                    break
                else:
                    break

            return valid_moves

            
        elif self.piece_type == 'r':
            #Check for UP valid moves
            for i in range(self.position[0]+1, self.board.board_size):
                tile = self.board.board[i][self.position[1]]
                if isinstance(tile, str):
                    valid_moves.append((i, self.position[1]))
                elif tile.owner != self.owner:
                    valid_moves.append((i, self.position[1]))
                    break
                else:
                    break
            # Check for DOWN valid moves 
            for i in range(self.position[0]-1, -1, -1):
                tile = self.board.board[i][self.position[1]]
                if isinstance(tile, str):
                    valid_moves.append((i, self.position[1]))
                elif tile.owner != self.owner:
                    valid_moves.append((i, self.position[1]))
                    break
                else:
                    break
            
            #Check for RIGHT valid moves
            for i in range(self.position[1]+1, self.board.board_size):
                tile = self.board.board[self.position[0]][i]
                if isinstance(tile, str):
                    valid_moves.append((self.position[0], i))
                elif tile.owner != self.owner:
                    valid_moves.append((self.position[0], i))
                    break
                else:
                    break
            
            #Check for LEFT valid moves
            for i in range(self.position[1]-1, -1, -1):
                tile = self.board.board[self.position[0]][i]
                if isinstance(tile, str):
                    valid_moves.append((self.position[0], i))
                elif tile.owner != self.owner:
                    valid_moves.append((self.position[0], i))
                    break
                else:
                    break
            return valid_moves

        elif self.piece_type == "b":
            #Check for LEFT DIAG UP valid moves
            i, j = self.position
            while True:
                i, j = i-1, j-1
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    break
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
                    break
                else:
                    break
            
            #Check for LEFT DIAG DOWN valid moves
            i, j = self.position
            while True:
                i, j = i+1, j+1
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    break
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
                    break
                else:
                    break

            #Check for RIGHT DIAG UP valid moves
            i, j = self.position
            while True:
                i, j = i-1, j+1
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    break
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
                    break
                else:
                    break

            #Check for RIGHT DIAG DOWN valid moves
            i, j = self.position
            while True:
                i, j = i+1, j-1
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    break
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
                    break
                else:
                    break
            
            return valid_moves
        elif self.piece_type == 'k':
            to_add = [
                (2, -1),
                (2, 1),
                (-2, -1),
                (-2, 1),
                (1, 2),
                (-1, 2),
                (1, -2),
                (-1, -2)
            ]
            for a in to_add:            
                i, j = self.position
                i, j = i + a[0], j + a[1]
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    continue
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
            return valid_moves
        elif self.piece_type == 'p':
            to_add1 = [
                (1, 0),
                (0, 1),
                (-1, 0),
                (0, -1)
            ]
            to_add2 = [
                (1, 1),
                (-1, -1),
                (-1, 1),
                (1, -1)
            ]
            for a in to_add1:            
                i, j = self.position
                i, j = i + a[0], j + a[1]
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    continue
                tile = self.board.board[i][j]
                if isinstance(tile, str):
                    valid_moves.append((i, j))
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))

            for a in to_add2:            
                i, j = self.position
                i, j = i + a[0], j + a[1]
                if not (i >= 0 and j >=0 and i < self.board.board_size and j < self.board.board_size):
                    continue
                tile = self.board.board[i][j]
                #try:
                #    print(i, j, tile.position, tile.owner)
                #except:
                #    pass
                if isinstance(tile, str):
                    continue
                elif tile.owner != self.owner:
                    valid_moves.append((i, j))
            return valid_moves
    '''
    def move(self, target_position):
        if target_position in self.get_valid_moves():
            self.position = target_position
            if self.board.get_tile(target_position) != "+":
                self.board.delete_piece(target_position)
    '''    
    def __repr__(self):
        if self.owner != None:  
            return self.piece_type + str(self.owner)
        else:
            return self.piece_type + "*"
  
if __name__ == "__main__":
    from .Board import Board
    while True:
        b = Board(board_size=4, pool_size=4)
        pieces = b.get_active_pieces()
        for i, p in enumerate(pieces):
            if p.piece_type == "p":
                break
        if i != b.pool_size-1:
            valid = p.get_valid_moves()
            print(p.position)
            print(valid, len(valid))
            print(b)    
            break