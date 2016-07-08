#!/usr/bin/python3

WHITE = 0
BLACK = 1
__version__ = "1.0.0"    

def main():
    b = board()
    b.draw_init_board()
   

class player():
    def __init__(self , name):
        self._name = name
        
    
class game():
    def __init__(self):
        self._turn = WHITE
        player_white = player()
        player_black = player()
        

class cell():
    def __init__(self , row , col , chessman):
        self.row = row
        self.col = col
        self.chessman = chessman
    def is_empty(self):
        return (True if chessman == None else False)

class board():
    def __init__(self):
        self.board_cells = []
        for i in range(8):
            for j in range(8):
                self.board_cells.append(cell(i , j , ))
    
    
    def draw_init_board(self):
        print ("------------------------") 
        for i in range(0 , 64 , 8):
            print(self.board_cells[i : i + 8])
        print ("------------------------")

class chessman():
    def __init__(self , cell , color):
        self._color = color
        self._cell = cell
    
    def is_legal_move(self):
        pass
    
    def is_legal_capture(self):
        return self.is_legal_capture()
    
    @property
    def row(self):
        return self._cell.row
    @property
    def col(self):
        return self._cell.col

class Pawn(chessman):
    def is_legal_move(self , new_cell):
        if self.col == new_cell.col:
            if self._color == WHITE:
                    if self.col == 2 and (new_cell.row - self.row == 1 or new_cell.row - self.row == 2):
                        return True
                    elif self.col > 2 and new_cell.row - self.row == 1:
                        return True
            else:
                    if self.col == 7 and (new_cell.row - self.row == -1 or new_cell.row - self.row == -2):
                        return True
                    elif self.col < 7 and new_cell.row - self.row == -1:
                        return True
        return False
    
    def is_legal_capture(self , new_cell):
        if self._color == WHITE:
            if (abs(self.col-new_cell.col), new_cell.row - self.row)==(1,1):
                return True
        else:
            if (abs(self.col-new_cell.col), new_cell.row - self.row)==(1,-1):
                return True
        return False
        
class Knight(chessman):
    pass

class Bishop(chessman):
    pass

class Queen(chessman):
    pass
    
class Rook(chessman):
    pass
    
class King(chessman):
    pass

        
if __name__ == "__main__": main()