def check_winner(board):
    winning_combinations = [
        # Rows
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        # Columns
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        # Diagonals
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)],
    ]

    for combination in winning_combinations:
        a, b, c = combination
        if (
            board[a[0]][a[1]] is not None
            and board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]]
        ):
            return board[a[0]][a[1]]

    return 0 

def is_board_full(board):
    rows = len(board);
    columns = len(board); 
    for x in range(rows):
        for y in range(columns):
            if board[x][y] is None: 
                board[x][y] = 0  
                print(f"Cleaned: {x}, {y}")
                return True  
  
    return False 
