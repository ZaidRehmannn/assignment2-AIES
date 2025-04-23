import math
import time

# Constants
HUMAN = 'O'
AI = 'X'
EMPTY = ' '

# Initialize the board
def create_board():
    return [[EMPTY for _ in range(3)] for _ in range(3)]

# Print the board
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*5)

# Check for winner
def check_winner(board):
    lines = board + [list(col) for col in zip(*board)] + \
            [[board[i][i] for i in range(3)]] + \
            [[board[i][2-i] for i in range(3)]]
    if [AI]*3 in lines:
        return AI
    elif [HUMAN]*3 in lines:
        return HUMAN
    elif all(cell != EMPTY for row in board for cell in row):
        return 'Draw'
    return None

# Get available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY]

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = AI
            score = minimax(board, depth + 1, False)
            board[i][j] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = HUMAN
            score = minimax(board, depth + 1, True)
            board[i][j] = EMPTY
            best_score = min(score, best_score)
        return best_score

# Alpha-Beta Pruning algorithm
def alphabeta(board, depth, alpha, beta, is_maximizing):
    winner = check_winner(board)
    if winner == AI:
        return 1
    elif winner == HUMAN:
        return -1
    elif winner == 'Draw':
        return 0

    if is_maximizing:
        best_score = -math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = AI
            score = alphabeta(board, depth + 1, alpha, beta, False)
            board[i][j] = EMPTY
            best_score = max(score, best_score)
            alpha = max(alpha, score)
            if beta <= alpha:
                break
        return best_score
    else:
        best_score = math.inf
        for (i, j) in get_available_moves(board):
            board[i][j] = HUMAN
            score = alphabeta(board, depth + 1, alpha, beta, True)
            board[i][j] = EMPTY
            best_score = min(score, best_score)
            beta = min(beta, score)
            if beta <= alpha:
                break
        return best_score

# Get best move using Minimax
def best_move_minimax(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = AI
        score = minimax(board, 0, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Get best move using Alpha-Beta Pruning
def best_move_alphabeta(board):
    best_score = -math.inf
    move = None
    for (i, j) in get_available_moves(board):
        board[i][j] = AI
        score = alphabeta(board, 0, -math.inf, math.inf, False)
        board[i][j] = EMPTY
        if score > best_score:
            best_score = score
            move = (i, j)
    return move

# Play the game with comparison
def play_game_with_comparison():
    board = create_board()

    print("Welcome to Tic-Tac-Toe!\nYou are 'O'. AI is 'X'.")
    print_board(board)

    while True:
        # Human move
        moves = get_available_moves(board)
        if not moves or check_winner(board):
            break

        print("\nAvailable moves (row col):", moves)
        try:
            i, j = map(int, input("Your move (row col): ").split())
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if (i, j) not in moves:
            print("Invalid move. Try again.")
            continue

        board[i][j] = HUMAN
        print("\nYour move:")
        print_board(board)

        if check_winner(board):
            break

        # Add delay for better UI experience
        print("\nAI is Thinking...\n")
        time.sleep(1)  # Sleep for 1 second

        # AI move - Calculating Minimax Time
        start = time.time()
        move_minimax = best_move_minimax(board)
        minimax_time = time.time() - start

        # AI move - Calculating Alpha-Beta Time
        start = time.time()
        move_ab = best_move_alphabeta(board)
        ab_time = time.time() - start

        # Apply the move to the board
        board[move_minimax[0]][move_minimax[1]] = AI
        print("\nBoard after AI move:")
        print_board(board)

        # Show the times taken by Minimax and Alpha-Beta
        print(f"\nMinimax took {minimax_time:.6f}s for move {move_minimax}")
        print(f"Alpha-Beta took {ab_time:.6f}s for move {move_ab}")

        if check_winner(board):
            break

    # Game result
    result = check_winner(board)
    print("\nGame Over!")
    if result == 'Draw':
        print("It's a draw!")
    else:
        print(f"{result} wins!")

if __name__ == "__main__":
    play_game_with_comparison()
