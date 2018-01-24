#!/usr/bin/env python

import itertools

""" Tic Tac Toe

    Allows for two players to alternate turns placing their token
    in a specific location on the game board. The game board consists
    of 9 possible play locations, indexed 0-8.

    0 1 2
    3 4 5
    6 7 8

    Players place their token on the board with strategy placed on forming
    a chain of 3 consecutive tokens in either a row, a column or diagonal.
    The game ends when a player has achived a chain of 3 consecutive tokens.
    If no chain has been created by time all spaces on the board are played,
    the game ends in a tie.
"""


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
            (bool): Whether the play inserted was successful or not
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
            win_values = [self.board[e] for e in win]
            if "-" in win_values:
                continue
            if len(set(iter(win_values))) <= 1:
                return win_values[0]
        return None

    def moves_left(self):
        """The number of valid positions on the board that are left to play
        Returns:
            (int): number of positions on the board that have not been played
        """
        cnt = 0
        for move in self.board:
            if move == "-":
                cnt += 1
        return cnt

    def print_board(self):
        """Print the current board positions to console, pretty-style
        """
        print("Current board: ")
        for i in range(3):
            print("{} {} {}".format(self.board[i * 3],
                                    self.board[i * 3 + 1],
                                    self.board[i * 3 + 2]))


def parse_turn(turn):
    """Parse the input from the user for valid player strings and play positions
    Args:
        turn (string): Input string from the user that contains the played
                       position (0-8)

    Returns:
        (int/None): Returns interger on success or None on failure
    """
    try:
        # check if position is valid
        if int(turn) > 8 or int(turn) < 0:
            print("Position must be 0-8")
            return None
        return int(turn)
    except Exception as e:
        print("Could not parse position")
        return None


def parse_player(player):
    """Parse an input string for the first player
    Args:
        player (string): String to be parsed (eg, X)
    Returns:
        (string/None): The player if valid or None
    """
    if player.lower() == "x":
        return "X"
    elif player.lower() == "o":
        return "O"
    else:
        print("Player must be X or O")
        return None


def opposite_player(player):
    """Finds the opposite player based on the input. Assumes only two players
    Args:
        player (string): Input player to invert
    Returns:
        (string): Opposite player from the input
    """
    if player == "X":
        return "O"
    else:
        return "X"


def main():
    # Determine the first player's token
    player = None
    while player is None:
        player = parse_player(input("Which player goes first? (X,O) "))

    # setup an iterator to switch the player
    player_switcher = itertools.cycle([player, opposite_player(player)])
    # kick off the iterator so that the cycle order is correct
    next(player_switcher)

    # Instantiate our game
    ttt = TicTacToe()

    # Accept turns from alternating player tokens as long as moves are still
    # available on the game board
    while ttt.moves_left() > 0:
        turn_str = input(
            "Player {}'s turn! Choose a location (0-8): ".format(player))
        turn = parse_turn(turn_str)
        if turn is None:
            continue
        if not ttt.insert_play(player, turn):
            continue
        # display the board to the user
        ttt.print_board()
        # check to see if anyone has a winning board combination
        winner = ttt.check_for_win()
        # switch players
        player = next(player_switcher)
        # someone won!
        if winner:
            print("Player {} wins!".format(winner))
            exit(0)

    # if all turns have been played, we must have a tie
    print("Tie game")


if __name__ == "__main__":
    main()
