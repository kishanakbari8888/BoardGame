from Person import Person
from board import Board
import random


# ORDER_TURN = ['red', 'blue', 'green', 'yellow']


def roll_dice():
    return random.randrange(1, 7, 1)


def next_turn(players, current_turn):
    index = players.index(current_turn)
    index = (index + 1) % len(players)
    return players[index]


def previous_turn(players, current_turn):
    index = players.index(current_turn)
    index = (index - 1) % len(players)
    return players[index]


def start_game(players, board):
    current_turn = players[0]
    current_board = board
    winner = []
    print("Press 0 to roll dice and 1 to exit game")
    game_live = int(input())
    while game_live == 0 and len(players) != 0:
        current_turn = next_turn(players, current_turn)
        win_pawn = 0
        for pawn in current_turn.pawns:
            if pawn.get_status == 1:
                win_pawn += 1
        if win_pawn == 4:
            print("{} Won!!!".format(current_turn.name))
            winner.append(current_turn)
            players.remove(current_turn)
            continue
        print("Turn of {} rolling dice.....".format(current_turn.name))
        step = roll_dice()
        print("Dice number= {}".format(step))
        allowed_pawns = current_turn.get_piece_not_in_home()
        if step == 6:
            for pawn in current_turn.get_piece_in_home():
                allowed_pawns.append(pawn)

        if len(allowed_pawns) == 0:
            print("You don't have any pawn to move!!")
        else:
            print("Enter name of pawn to move from below")
            for pawn in allowed_pawns:
                print(pawn, end=" ")
            print("\n")
            choosen_pawn_name = input()
            current_pawn = current_turn.get_pawn_by_name(choosen_pawn_name)
            status = current_turn.move(current_pawn, step, current_board)
            if status != 0:
                for player in players:
                    for pawn in player.pawns:
                        if pawn.name == status:
                            current_board.kill(pawn)
            else:
                print("No merge 2 pawn")
        current_board.print_board()
        if step == 6:
            print("It's your turn again rolling dice...")
            current_turn = previous_turn(players, current_turn)
            continue
        print("Press 0 to roll dice and 1 to exit game")
        game_live = int(input())

    print("List of winners")
    for player in winner:
        print(player.name)


if __name__ == "__main__":
    print("Welcome to LUDO!")
    print("Please enter number of player \n\
           1) Play with computer\n\
           2) 2 player\n\
           3) 3 player\n\
           4) 4 player\n")
    no_player = int(input())
    players = []

    for _ in range(1, no_player + 1):
        name = input("Enter name of person: ")
        colour = input("Enter colour of pawn in small letters: ")
        player = Person(name, colour)
        players.append(player)

    pb = Board()
    pb.initial_state(players)
    print("!!!!!!!!!!!!Initial state of game!!!!!!!!!!!!!!")
    pb.print_board()

    # start the game
    start_game(players, pb)