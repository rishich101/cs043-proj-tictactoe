# This file contains the game implementation.
import board
import player


# This class will be used to play a single game between two players.
class Game:

    # __init__ method creates the board and player objects.
    def __init__(self):
        self.player1 = player.Player("X")
        self.player2 = player.Player("O")
        self.board = board.Board()

    # valid_positions returns the list of valid positions to be used.
    def valid_positions(self):
        return ['TL', 'ML', 'BL', 'TM', 'MM', 'BM', 'TR', 'MR', 'BR']

    # is_valid_position checks if the input position is valid from the list.
    def is_valid_position(self, position):
        positions = self.valid_positions()
        if position.upper() in positions:
            return True
        return False

    # print_valid_entries method shows the valid input for playing the game.
    def print_valid_entries(self):
        print("""
            TL - Top Left    | TM - Top Middle    | TR - Top Right
            ML - Middle Left | MM - Center        | MR - Middle Right
            BL - Bottom Left | BM - Bottom Middle | BR - Bottom Right""")

    # print_board prints the game board.
    def print_board(self):
        self.board.print_board()

    # switch_turn switches the turn between the players after a move.
    def switch_turn(self, player):
        if player is self.player1:
            return self.player2
        else:
            return self.player1

    # won_game returns if the current player won the game.
    def won_game(self, player):
        return self.board.is_winner(player)

    # modify_board makes the move for a player.
    def modify_board(self, position, type):
        if self.board.change_board(position, type) is not None:
            return self.board.change_board(position, type)
        else:
            position = input("Not an available position. Please, try again: ")
            return self.board.change_board(position, type)
