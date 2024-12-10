from index import check_winner, is_board_full

def minimax(board:list[list[str]], depth:int, is_maximizing:bool, ai_symbol:str, player_symbol:str):
    """
    The Minimax algorithm is a recursive function that evaluates the best move for the AI.

    - If it's the AI's turn (is_maximizing=True), the goal is to maximize the AI's score aka finding the best scenario to which early
    - If it's the player's turn (is_maximizing=False), the goal is to minimize the AI's score (as the player tries to block the AI) aka finding the work scenario which is lose early

    Depth represents the level of recursion. The deeper the recursion, the further ahead the algorithm is looking.

    Args:
        board (list[list[str]]): The current game board.
        depth (int): The depth of the recursion (used for scoring).
        is_maximizing (bool): True if it's the AI's turn, False if it's the player's turn.
        ai_symbol (str): The symbol representing the AI ('X' or 'O').
        player_symbol (str): The symbol representing the player ('X' or 'O').

    Returns:
        int: The score of the board state.
    """
    winner = check_winner(board)
    if winner == ai_symbol:
        return 10 - depth  # AI wins the earlier the win, the better
    if winner == player_symbol:
        return depth - 10  # player wins the later the loss, the better for the AI
    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -float('inf')  
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = ai_symbol  
                    score = minimax(board, depth + 1, False, ai_symbol, player_symbol)
                    board[i][j] = " "
                    best_score = max(score, best_score)  
        return best_score
    else:
        best_score = float('inf')  
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = player_symbol  
                    score = minimax(board, depth + 1, True, ai_symbol, player_symbol)
                    board[i][j] = " " 
                    best_score = min(score, best_score) 
        return best_score

def ai_next_move(board:list[list[str]], ai_symbol:str, player_symbol:str):
    """
    Determines the best move for the AI using the Minimax algorithm.
    
    This function tries every empty cell, simulates the AI's move, and evaluates the result using Minimax.

    Args:
        board (list[list[str]]): The current game board.
        ai_symbol (str): The symbol representing the AI ('X' or 'O').
        player_symbol (str): The symbol representing the player ('X' or 'O').

    Returns:
        tuple[int, int]: The row and column indices of the best move for the AI.
    """
    best_score = -float('inf')
    best_move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = ai_symbol 
                score = minimax(board, 1, False, ai_symbol, player_symbol)  
                board[i][j] = " " 
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
    return best_move





