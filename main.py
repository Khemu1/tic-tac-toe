from utils.index import check_winner, is_board_full
from utils.ai_algos import minimax, ai_next_move

def playGame():
    board = [[" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]]

    ai_symbol = "X"
    player_symbol = "O"

    turn = "Player"
    while True:
        for row in board:
            print(row)
        
        winner = check_winner(board)
        if winner:
            print(f"{winner} wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break
        
        if turn == "Player":
            print("\nYour turn!")
            try:
                row, col = map(int, input("Enter your move (row and col): ").split())
                if board[row][col] == " ":
                    board[row][col] = player_symbol
                    turn = "AI"
                else:
                    print("Cell is already taken, try again!")
            except (ValueError, IndexError):
                print("Invalid input. Please enter row and col as two integers (0, 1, or 2).")
        else: 
            print("\nAI's turn!")
            row, col = ai_next_move(board, ai_symbol, player_symbol)
            board[row][col] = ai_symbol
            turn = "Player"

playGame()
