# Main game logic and play in terminal mode

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows
    for row in board:
        if all(s == player for s in row):
            return True
    # Check columns
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)

    while True:
        try:
            move = input(f"Player {current_player}, enter your move (row,col from 1-3): ")
            row, col = map(int, move.strip().split(","))
            row -= 1
            col -= 1

            if board[row][col] != " ":
                print("This cell is already taken. Try again.")
                continue

            board[row][col] = current_player
            print_board(board)

            if check_winner(board, current_player):
                print(f"Player {current_player} wins!")
                break

            if is_full(board):
                print("It's a draw!")
                break

            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("Invalid input. Please enter in the format row,col (e.g., 2,3).")

if __name__ == "__main__":
    tic_tac_toe()
