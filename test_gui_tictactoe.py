import unittest
from PyQt5.QtWidgets import QApplication
from gui_tic_tac_toe_pyqt import TicTacToe
import sys

app = QApplication(sys.argv)  # Needed to initialize Qt widgets

class TestTicTacToeLogic(unittest.TestCase):
    def setUp(self):
        self.window = TicTacToe()

    def simulate_board(self, layout):
        """Helper to simulate button text from a 2D array"""
        for row in range(3):
            for col in range(3):
                self.window.buttons[row][col].setText(layout[row][col])

    def test_row_win(self):
        self.simulate_board([
            ["X", "X", "X"],
            [" ", "O", " "],
            ["O", " ", " "]
        ])
        self.assertTrue(self.window.check_winner("X"))

    def test_column_win(self):
        self.simulate_board([
            ["O", "X", " "],
            ["O", "X", " "],
            ["O", " ", "X"]
        ])
        self.assertTrue(self.window.check_winner("O"))

    def test_diagonal_win_main(self):
        self.simulate_board([
            ["X", "O", " "],
            ["O", "X", " "],
            [" ", " ", "X"]
        ])
        self.assertTrue(self.window.check_winner("X"))

    def test_diagonal_win_anti(self):
        self.simulate_board([
            [" ", " ", "O"],
            ["X", "O", " "],
            ["O", "X", "X"]
        ])
        self.assertTrue(self.window.check_winner("O"))

    def test_no_win(self):
        self.simulate_board([
            ["X", "O", "X"],
            ["X", "O", "O"],
            ["O", "X", "X"]
        ])
        self.assertFalse(self.window.check_winner("X"))
        self.assertFalse(self.window.check_winner("O"))

if __name__ == "__main__":
    unittest.main()
