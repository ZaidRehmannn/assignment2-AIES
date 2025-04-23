# Tic-Tac-Toe with Minimax and Alpha-Beta Pruning

## Overview

This is a simple command-line Tic-Tac-Toe game where you, the player, compete against an AI opponent. You play as 'O' and the AI plays as 'X'. The game uses two different algorithms for the AI's decision-making: **Minimax** and **Alpha-Beta Pruning**. 

In this game:
- You make your move first by entering the row and column of your desired position on the 3x3 grid.
- The AI then makes its move using both Minimax and Alpha-Beta algorithms. 
- After each AI move, the program displays the **AI's move** and the **time taken** by each algorithm to determine that move.
- The game continues until either a player wins or a draw occurs.

## Game Flow

1. **Starting the Game**:
   - When you start the game, you are prompted with an empty 3x3 Tic-Tac-Toe board.
   - You are playing as 'O', and the AI is playing as 'X'.

2. **Making Your Move**:
   - The game displays a list of available moves (empty cells).
   - You input your desired move in the format `row column`, for example: `0 0` to place your 'O' in the top-left corner.
   - The board is updated after your move, and it’s displayed to you.

3. **AI Makes Its Move**:
   - After your move, the AI will think for a short time (you can adjust this delay).
   - The AI makes its move using **both Minimax** and **Alpha-Beta Pruning** algorithms. 
   - The AI’s move is displayed on the board.

4. **Display Algorithm Times**:
   - Below the board, the time taken by each algorithm to decide the move is displayed:
     - **Minimax Time**: Time taken by the Minimax algorithm.
     - **Alpha-Beta Time**: Time taken by the Alpha-Beta Pruning algorithm.

5. **Game Continuation**:
   - The game continues with both players taking turns making moves until a player wins, or all cells are filled (resulting in a draw).

6. **Game End**:
   - If there is a winner, the program announces the winner ('X' for AI or 'O' for you).
   - If all cells are filled and no player has won, the game ends in a draw.

## Key Features

- **Minimax Algorithm**: The AI calculates the best move based on an exhaustive search of the game tree.
- **Alpha-Beta Pruning**: The AI uses Alpha-Beta Pruning to improve the performance of the Minimax algorithm by eliminating branches that are not useful, reducing the number of moves it needs to evaluate.
- **Move Timing**: After each AI move, the program shows how much time it took for each algorithm to calculate the move.
- **User Interaction**: You make your move interactively by entering the row and column of your desired position on the board.

## Demo

You can download and view the demo video here:

[Download Demo Video](./demo/your_video_file.mp4)

## How to Run the Game

1. Clone or download the repository.
2. Make sure Python 3.x is installed on your machine.
3. Open a terminal/command prompt and navigate to the directory where the script is located.
4. Run the script using the following command: python tic_tac_toe.py
5. Follow the on-screen instructions to play the game.
