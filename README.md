# Tic Tac Toe

A simple command-line Tic Tac Toe game built with Python for two players.

## Features

- Two-player gameplay
- X and O turns
- 3x3 game board
- Win detection for rows, columns, and diagonals
- Draw detection
- Invalid input handling
- Prevents moves on occupied positions
- Option to play multiple games

## Requirements

- Python 3.8 or later
- No external Python packages are required

## How to Run

1. Make sure Python is installed on your system.
2. Open a terminal in the project folder.
3. Run the following command:

    python tic_tac_toe.py

## How to Play

The board positions are numbered from 1 to 9:

    1 | 2 | 3
    ---+---+---
    4 | 5 | 6
    ---+---+---
    7 | 8 | 9

Players take turns selecting an available position.

The first player to get three symbols in a row, column, or diagonal wins the game.

If all positions are filled without a winner, the game ends in a draw.

After a game ends, players can choose whether to play again.

## Input Handling

The game handles:

- Invalid non-numeric input
- Numbers outside the range 1-9
- Already occupied positions

## Project Structure

    Tic-Tac-Toe/
    │
    ├── tic_tac_toe.py
    └── README.md

## Technologies Used

- Python
- Object-Oriented Programming
- Command-Line Interface

## License

This project is provided for educational and personal portfolio purposes.