from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout, QMessageBox
import sys
# Main game logic and play in UI mode
class TicTacToe(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe")
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        layout = QGridLayout()

        for row in range(3):
            for col in range(3):
                button = QPushButton(" ")
                button.setFixedSize(100, 100)
                button.setStyleSheet("font-size: 28px;")
                button.clicked.connect(lambda _, r=row, c=col: self.on_click(r, c))
                self.buttons[row][col] = button
                layout.addWidget(button, row, col)

        self.setLayout(layout)

    def on_click(self, row, col):
        button = self.buttons[row][col]
        if button.text() == " ":
            button.setText(self.current_player)
            if self.check_winner(self.current_player):
                QMessageBox.information(self, "Game Over", f"Player {self.current_player} wins!")
                self.disable_all()
            elif all(self.buttons[r][c].text() != " " for r in range(3) for c in range(3)):
                QMessageBox.information(self, "Game Over", "It's a draw!")
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self, player):
        for i in range(3):
            if all(self.buttons[i][j].text() == player for j in range(3)) or \
               all(self.buttons[j][i].text() == player for j in range(3)):
                return True
        if all(self.buttons[i][i].text() == player for i in range(3)) or \
           all(self.buttons[i][2 - i].text() == player for i in range(3)):
            return True
        return False

    def disable_all(self):
        for row in self.buttons:
            for button in row:
                button.setEnabled(False)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = TicTacToe()
    window.show()
    sys.exit(app.exec_())
