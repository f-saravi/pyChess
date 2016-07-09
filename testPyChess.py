'''
Created on Jul 9, 2016

@author: farid
'''

import unittest
import pytest

class testBoard(unittest.TestCase):   
    def setUp(self):
        self._tst_board = pytest.board("rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR")
        
    def test_hasCells(self):        
        for key in self._tst_board.board_cells:
            assert type(self._tst_board.board_cells[key])==list
            for cell in self._tst_board.board_cells[key]:
                assert type(cell)==pytest.cell
                assert (cell.is_empty() or isinstance(cell.chessman, pytest.chessman))
    
    def test_countPieces(self):
        pass

if __name__ == "__main__":
    unittest.main()