#!/usr/bin/env python

class TicTacToe:

    def __init__(self):
        """Inits an object that holds the board's plays and combinations of val
            id win moves
        """
        self.board = ["-"] * 9
        self.wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6],
                     [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    def insert_play(self, player, position):
        """Insert a play by a player at a specified position on the board
        Args:
            player (string): The player string, either X or O are valid
            position (int): The index in the board list for the specicied play

        Returns:
            (Bool): Whether the play inserted was successful or not
        """
        if self.board[position] == "-":
            self.board[position] = player
            return True
        else:
            print("Position {} already played by {}".format(
                position, self.board[position]))
            return False

    def check_for_win(self):
        """Checks the board list for valid win combinations
        """
        for win in self.wins:
            first_val = self.board[win[0]]
            if first_val == "-":
                continue
            if first_val == self.board[win[1]] and first_val == self.board[win[2]]:
                print("Found win in indicies: {}".format(win))
                return first_val
        return None

    def print_board(self):
        """Print the current board positions to console, pretty-style
        """
        print("Current board: ")
        for i in range(3):
            print("{} {} {}".format(self.board[i * 3],
                                    self.board[i * 3 + 1],
                                    self.board[i * 3 + 2]))


def parse_play(move):
    """Parse the input from the user for valid player strings and play positions
    Args:
        move (string): Input from the user in the expected format "X,5"

    Returns:
        (Bool): Returns if parse was successful or not
    """
    try:
        split_move = move.split(',')
        # check for invalid split
        if len(split_move) != 2:
            print("Could not parse player and position")
            return None
        # check for valid player
        if split_move[0] != "X" and split_move[0] != "O":
            print("Player must be X or O")
            return None
        # check if position is valid
        if int(split_move[1]) > 8 or int(split_move[1]) < 0:
            print("Position must be 0-8")
            return None
        print("Player {} plays position: {}".format(
            split_move[0], split_move[1]))
        return split_move
    except Exception as e:
        print("Could not parse player and position")
        return None


def main():
    ttt = TicTacToe()
    for i in range(9):
        move = input("Make a play (eg, X,5) ")
        play = parse_play(move)
        if not play:
            continue
        if not ttt.insert_play(play[0], int(play[1])):
            continue
        ttt.print_board()
        winner = ttt.check_for_win()
        if winner:
            print("Player {} wins!".format(winner))
            exit(0)
    print("Tie game")


if __name__ == "__main__":
    main()
