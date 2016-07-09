'''
Created on Jul 9, 2016

@author: farid
'''
from definitions import * 

class chessman():
    def __init__(self , cell , color):
        '''
        Constructor
        '''
        self._color = color
        self._cell = cell
    
    def is_legal_move(self):
        pass
    
    def is_legal_capture(self):
        return self.is_legal_capture()
    
    def get_short_name(self):
        return type(self).__name__[0]
        
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
    def is_legal_move(self , new_cell):
        deltaMatrix=(abs(self.col-new_cell.col), abs(new_cell.row - self.row))
        if deltaMatrix==(1,2) or deltaMatrix==(2,1):
            return True
        return False
    
    def get_short_name(self):
        return 'N'
    

class Bishop(chessman):
    def is_legal_move(self , new_cell):
        if abs(self.col-new_cell.col)==abs(new_cell.row - self.row):
            return True
        return False

class Rook(chessman):
    def is_legal_move(self , new_cell):
        if self.col==new_cell.col or new_cell.row == self.row:
            return True
        return False        

class Queen(chessman):
    def is_legal_move(self , new_cell):
        if self.col==new_cell.col or new_cell.row == self.row:
            return True
        elif abs(self.col-new_cell.col)==abs(new_cell.row - self.row):
            return True
        return False 
    
class King(chessman):
    def is_legal_move(self , new_cell):
        if abs(self.col-new_cell.col)<=1 and abs(new_cell.row - self.row)<=1:
            return True
        return False

        