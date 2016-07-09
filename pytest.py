#!/usr/bin/python3
import re
from chessMan import *
chessman_classes = dict(k = King , q = Queen , r = Rook , b = Bishop , n = Knight , p = Pawn , o = lambda x,y:None)


def main():
    b = board()
    b.draw_init_board()
   

class player():
    def __init__(self , name):
        self._name = name
        self._chessmans = []
    
        
    
class game():
    def __init__(self):
        self._turn = 'w'
        self._board = None
        players = dict(w = player() , b = player())

    def setup_board(self , fen_string):
        piece_placement , turn , casting , \
            en_passant , halfmove_clk , fullmove_num = fen_string.split(" ")
        self._board=board(piece_placement)

class cell():
    def __init__(self , row , col , chessman = None):
        self.row = row
        self.col = col
        self.chessman = chessman
    
    def set_chessman(self , chess_man = None):
        self.chessman = chess_man
    

    def is_empty(self):
        return (True if self.chessman==None else False)

class board():
    #===========================================================================
    # __init__
    #===========================================================================
    def __init__(self, piece_placement):
        piece_placement = re.sub("\d", lambda mtch:mtch.group(0).replace(mtch.group(0),
                        "o" * int(mtch.group(0))), piece_placement)
        fen_ranks = piece_placement.split("/")
        fen_ranks.reverse()
        self.board_cells = {m:[] for m in 'abcdefgh'}
        #self.board_cells = [[cell(j,i) for i in range(8)] for j in range(8)]
        for i , fen_rank in enumerate(fen_ranks):
            for file_label , (j , piece_name) in zip('abcdefgh' , enumerate(fen_rank)):
                color = BLACK if piece_name.islower() else WHITE
                self.board_cells[file_label].append(cell(j ,i))
                self.board_cells[file_label][i].set_chessman(chessman_classes[piece_name.lower()](self.board_cells[file_label][i] , color)) 
#        self.board_cells = [[cell(j,i) for i in range(8)] for j in range(8)]
#         for i , j , color in [(x,y,c) for x in range(8) for y,c in ((2,0),(7,1))]:
#             self.board_cells[j][i].set_chessman(Pawn(self.board_cells[j][i] , color))
    def get_board_chessmans(self , color):
        return [chessman for file_label in 'abcdefgh' for cell in self.board_cells[file_label] if cell.chessman and cell.chessman.color == color]

    #===========================================================================
    # draw_init_board
    #===========================================================================
    def draw_init_board(self):
        print ("------------------------") 
        for i in range(0 , 64 , 8):
            print(self.board_cells[i : i + 8])
        print ("------------------------")

        
if __name__ == "__main__": main()