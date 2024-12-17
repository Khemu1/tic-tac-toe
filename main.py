from utils.index import check_winner, is_board_full
from utils.ai_algos import ai_next_move

def playGame():
    x_score = 0
    o_score = 0
    ai_symbol = "X"
    player_symbol = "O"

    while True: 
        board = [[" ", " ", " "],
                [" ", " ", " "],
                [" ", " ", " "]]
        
        turn = "Player"  

        while True:

            for row in board:
                print(row)

            winner = check_winner(board)
            if winner:
                print(f"\n{winner} wins!")
                if winner == ai_symbol:
                    x_score += 1
                else:
                    o_score += 1
                print(f"Scores -> X: {x_score}, O: {o_score}\n")
                break
            elif is_board_full(board):
                print("\nIt's a draw!")
                print(f"Scores -> X: {x_score}, O: {o_score}\n")
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

        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again not in ["yes", "y"]:
            print("Thanks for playing! Final Scores:")
            print(f"X: {x_score}, O: {o_score}")
            break

playGame()
