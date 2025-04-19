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

    def test_on_click(self):
        # Verify initial player is X
        self.assertEqual(self.window.current_player, "X")
        
        # Test valid move - should update button and switch player
        self.window.on_click(0, 0)
        self.assertEqual(self.window.buttons[0][0].text(), "X")
        self.assertEqual(self.window.current_player, "O")
        
        # Test clicking an occupied cell - should not change anything
        original_player = self.window.current_player
        self.window.on_click(0, 0)  # Click the same button again
        self.assertEqual(self.window.buttons[0][0].text(), "X")  # Text remains X
        self.assertEqual(self.window.current_player, original_player)  # Player unchanged
        
        # Test another valid move - player O should play
        self.window.on_click(1, 1)
        self.assertEqual(self.window.buttons[1][1].text(), "O")
        self.assertEqual(self.window.current_player, "X")  # Back to X

if __name__ == "__main__":
    unittest.main()
