def check_winner(board):

    for row in board:
        if row[0] != " " and row[0] == row[1] == row[2]:
            return row[0]  

    for col in range(3):
        if board[0][col] != " " and board[0][col] == board[1][col] == board[2][col]:
            return board[0][col]  

    if board[0][0] != " " and board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]  
    
    if board[0][2] != " " and board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]  

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
