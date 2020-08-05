# Tic Tac Toe

import game

# play function starts one game.
def play():
    g = game.Game()
    g.print_valid_entries()
    player = g.player1
    num = 9
    while num > 0:
        num -= 1
        g.print_board()
        while True:
            position = input("{} turn, what's your move? ".format(player))
            if g.is_valid_position(position):
                break
            print("Valid options are {}".format(g.valid_positions()))
        g.modify_board(position.upper(), player.type)
        if g.won_game(player):
            print("{} is the Winner!".format(player))
            break
        else:
            player = g.switch_turn(player)
    if num == 0:
        print("Game over! It's a tie!")


if __name__ == "__main__":
    play()
    while True:
        print('Do you want to play again?(Yes or No)', end=' ')
        x = input().lower()
        if x == 'yes':
            play()
        else:
            break
