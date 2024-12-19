from flask import Flask, request, jsonify # type: ignore
from flask_cors import CORS  # type: ignore
from utils.index import check_winner, is_board_full
from utils.ai_algos import ai_next_move

app = Flask(__name__)
CORS(app)
board = [[" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]]
x_score = 0
o_score = 0

def update_score(winner):
    global x_score, o_score
    if winner == 'X':
        x_score += 1
    elif winner == 'O':
        o_score += 1

def reset_game():
    global board 
    board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]


@app.route('/player_turn', methods=['POST'])
def player_turn():
    global board, x_score, o_score

    data = request.get_json()
    row, col = data.get('row'), data.get('col')

    if row < 0 or row >= 3 or col < 0 or col >= 3 or board[row][col] != " ":
        return jsonify({"error": "Invalid move"}), 400

    board[row][col] = 'O'

    winner = check_winner(board)
    if winner:
        update_score(winner)
        return jsonify({
            "message": f"{winner} wins!",
            "cell": (row, col),
            "score": {"X": x_score, "O": o_score},
            "winner": winner
        })

    if is_board_full(board):
        return jsonify({
            "message": "It's a draw!",
            "score": {"X": x_score, "O": o_score},
            "winner": None
        })

    return jsonify({
        "message": "Player's turn completed.",
        "score": {"X": x_score, "O": o_score},
        "winner": None
    })


@app.route('/ai_turn', methods=['GET'])
def ai_turn():
    global board, x_score, o_score

    row, col = ai_next_move(board, 'X', 'O')
 
    board[row][col] = 'X'
 
    winner = check_winner(board)
    if winner:
        update_score(winner)
        return jsonify({
            "message": f"{winner} wins!",
            "cell": (row, col),
            "score": {"X": x_score, "O": o_score},
            "winner": winner
        })

    if is_board_full(board):
        return jsonify({
            "message": "It's a draw!",
            "score": {"X": x_score, "O": o_score},
            "winner": None
        })

    return jsonify({
        "message": "AI's turn completed.",
        "cell": (row, col),
        "score": {"X": x_score, "O": o_score},
        "winner": None
    })


@app.route('/reset', methods=['POST'])
def reset():
    global board, x_score, o_score
    reset_game()
    return jsonify({
        "message": "Game reset successful",
        "score": {"X": x_score, "O": o_score},
        "winner": None
    })


if __name__ == "__main__":
    app.run(debug=True)
