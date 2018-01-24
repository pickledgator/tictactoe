# tictactoe

## Instructions
Players take turns by marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Usage
```shell
python3 tictactoe.py
```

First, select the token for the first player. The only two tokens allowed are "X" and "O".
```shell
Which player goes first? (X,O): 
```
Then, each player takes turn entering positions cooresponding to their move on the 3x3 board.
```shell
Player X's turn! Choose a location (0-8):
```

```shell
0 1 2
3 4 5
6 7 8
```

## Example
```shell
tictactoe: python3 tictactoe.py
Which player goes first? (X,O) X
Player X's turn! Choose a location (0-8): 4
Current board:
- - -
- X -
- - -
Player O's turn! Choose a location (0-8): 6
Current board:
- - -
- X -
O - -
Player X's turn! Choose a location (0-8): 2
Current board:
- - X
- X -
O - -
Player O's turn! Choose a location (0-8): 5
Current board:
- - X
- X O
O - -
Player X's turn! Choose a location (0-8): 7
Current board:
- - X
- X O
O X -
Player O's turn! Choose a location (0-8): 2
Position 2 already played by X
Player O's turn! Choose a location (0-8): 0
Current board:
O - X
- X O
O X -
Player X's turn! Choose a location (0-8): 1
Current board:
O X X
- X O
O X -
Player X wins!
```
