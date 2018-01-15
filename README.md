# tictactoe

## Instructions
Players take turns by marking the spaces in a 3×3 grid. The player who succeeds in placing three of their marks in a horizontal, vertical, or diagonal row wins the game.

## Usage
```python3 tictactoe.py```

Make a move by typing player,position when prompted (eg., X,0 or O,4) where the position is the row major index of the 3x3 board. 

```
0 1 2
3 4 5
6 7 8
```

## Example
```shell
➜  tictactoe git:(master) python3 tictactoe.py
Make a play (eg, X,5) X,4
Player X plays position: 4
Current board:
- - -
- X -
- - -
Make a play (eg, X,5) O,2
Player O plays position: 2
Current board:
- - O
- X -
- - -
Make a play (eg, X,5) X,1
Player X plays position: 1
Current board:
- X O
- X -
- - -
Make a play (eg, X,5) O,6
Player O plays position: 6
Current board:
- X O
- X -
O - -
Make a play (eg, X,5) X,7
Player X plays position: 7
Current board:
- X O
- X -
O X -
Found win in indicies: [1, 4, 7]
Player X wins!
```
