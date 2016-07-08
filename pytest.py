#!/usr/bin/python3


__version__ = "1.0.0"    

def main():
    b = board()
    b.draw_init_board()

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
        self.cell = cell


    def move(self , new_x , new_y):
        if 0 <= new_x and new_x <= 8 and 0 <= new_y and new_y <= 8:
            self._x = new_x
            self._y = new_y
        else:
            print("invalid move")
            
        
    def get_position(self):
        return (self._x , self._y)


class Pawn(chessman):
    def __init__(self , cell , color , identity):
        super(Pawn, self).__init__(cell , color)
        self._identity = identity
       
    def move(self, new_x, new_y):
        
        chessman.move(self, new_x, new_y)
    
    def is_possible_pawn_move(self , new_x , new_y):
        if self._color == "white":
            if self._y == new_y:
                if self._x == 2 and (new_x - self._x == 1 or new_x - self._x == 2):
                    return True
                elif self._x > 2 and new_x - self._x == 1:
                    return True
            elif abs(self._y - new_y) == 1 and is_emply_and_in_board(new_x, new_y):
                
            retu
        
class Knight(chessman):
    def __init__(self , x , y , color , identity):
        super(Knight, self).__init__(x , y , color)
        self._identity = identity

class Bishop(chessman):
    def __init__(self , x , y , color , identity):
        super(Bishop, self).__init__(x , y , color)
        self._identity = identity

class Queen(chessman):
    def __init__(self , x , y , color , identity):
        super(Queen, self).__init__(x , y , color)
        self._identity = identity
    
class Rook(chessman):
    def __init__(self , x , y , color , identity):
        super(Rook, self).__init__(x , y , color)
        self._identity = identity
    
class King(chessman):
    def __init__(self , x , y , color , identity):
        super(King, self).__init__(x , y , color)
        self._identity = identity

        
if __name__ == "__main__": main()