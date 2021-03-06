from copy import deepcopy

BOARD = [['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
          '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
          '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
          '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
          '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
          '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
          '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               'R', 'E', 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', 'V', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', 'B', 'L', 'U', 'E', ' ', ' ', ' ', 
         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', 
               '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 
         '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
         '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', 
               '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 
         '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
         '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', 
               '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 
         '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', ' ', '-', '-', '>', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
         ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
         '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
         ['#', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', 
               ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', 
               ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', 
         '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '#'], 
         ['#', '-', '-', '-', '-', '-', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '-', '-', '-', '-', '-', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', 
               ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', 
               ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', 'X', ' ', ' ', '|', ' ', ' ', ' ', 
               ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', 
               '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', '-', '-', '-', '-', '-', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '-', '-', '-', '-', '-', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '-', '-', '-', '-', '-', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', 
               ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', 
               ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', 
               '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '<', '-', '-', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', 'G', 'R', 'E', 'E', 'N', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', 'Y', 'E', 'L', 'L', 'O', 'W', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', 
               '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 
               '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', 
               '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 
               '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', 
               '|', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '-', '-', 
               '-', '-', '-', '-', '-', '-', '-', '-', '-', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', 
               '-', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '^', ' ', '#', '-', '-', 
               '-', '-', '-', '#', '-', '-', '-', '-', '-', '#', '-', '-', '-', 
               '-', '-', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '|', ' ', '#', ' ', ' ', 
               ' ', ' ', ' ', '|', ' ', ' ', ' ', ' ', ' ', '|', ' ', ' ', ' ', 
               ' ', ' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 
               ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'], 
              ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', 
               '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#', '#']
            ]

# List of two sized tuples. The content of tuple correspond
# with address of matrix BOARD. While list index correspond
# with pawn share position from board class
COMMON_MOVES = [
    [14, 2], [14, 8], [14, 14], [14, 20], [14, 26], [14, 32], [14, 38],
    [12, 38], [10, 38], [8, 38], [6, 38], [4, 38], [2, 38], [2, 44],
    [2, 50], [4, 50], [6, 50], [8, 50], [10, 50], [12, 50], [14, 50],
    [14, 56], [14, 62], [14, 68], [14, 74], [14, 80], [14, 86], [16, 86],
    [18, 86], [18, 80], [18, 74], [18, 68], [18, 62], [18, 56], [18, 50],
    [20, 50], [22, 50], [24, 50], [26, 50], [28, 50], [30, 50], [30, 44],
    [30, 38], [28, 38], [26, 38], [24, 38], [22, 38], [20, 38], [18, 38],
    [18, 32], [18, 26], [18, 20], [18, 14], [18, 8], [18, 2], [16, 2]
]

# If in one block there are 2 pawn then this address used to movw second pawn
COMMON_MOVES_SECOND = [
    [14, 4], [14, 10], [14, 16], [14, 22], [14, 28], [14, 34], [14, 40],
    [12, 40], [10, 40], [8, 40], [6, 40], [4, 40], [2, 40], [2, 46],
    [2, 52], [4, 52], [6, 52], [8, 52], [10, 52], [12, 52], [14, 52],
    [14, 58], [14, 64], [14, 70], [14, 76], [14, 82], [14, 88], [16, 88],
    [18, 88], [18, 82], [18, 76], [18, 70], [18, 64], [18, 58], [18, 52],
    [20, 52], [22, 52], [24, 52], [26, 52], [28, 52], [30, 52], [30, 46],
    [30, 40], [28, 40], [26, 40], [24, 40], [22, 40], [20, 40], [18, 40],
    [18, 34], [18, 28], [18, 22], [18, 16], [18, 10], [18, 4], [16, 4]
]
# first position of pawn when it comes out from home
FIRST_MOVE = {
      'red': [14, 8],
      'blue': [4, 50],
      'green': [28, 38],
      'yellow': [18, 80]
}

# tuple correspond with address of matrix BOARD
# color correspond to pawn colour
# index of colour's list correspond with pawn private position
FINAL_MOVES = {
    'red': [[], [16, 8], [16, 14], [16, 20], [16, 26], [16, 32], [16, 38]],
    'blue': [[], [4, 44], [6, 44], [8, 44], [10, 44], [12, 44], [14, 44]],
    'yellow': [[], [16, 80], [16, 74], [16, 68], [16, 62], [16, 56], [16, 50]],
    'green': [[], [28, 44], [26, 44], [24, 44], [22, 44], [20, 44], [18, 44]]
}

FINAL_MOVES_SECOND = {
    'red': [[], [16, 10], [16, 16], [16, 22], [16, 28], [16, 34], [16, 40]],
    'blue': [[], [4, 46], [6, 46], [8, 46], [10, 46], [12, 46], [14, 46]],
    'yellow': [[], [16, 82], [16, 76], [16, 70], [16, 64], [16, 58], [16, 52]],
    'green': [[], [28, 46], [26, 46], [24, 46], [22, 46], [20, 46], [18, 46]]
}

# tuple correspond with address of matrix BOARD
# color correspond to pawn colour
# index of colour's list correspond with pawn initial position
HOME = {
    'red': [[], [6, 14], [6, 19], [8, 14], [8, 19]],
    'blue': [[], [6, 71], [6, 76], [8, 71], [8, 76]],
    'yellow': [[], [24, 71], [24, 76], [26, 71], [26, 76]],
    'green': [[], [24, 14], [24, 19], [26, 14], [26, 19]]
}


class Board():

      def __init__(self):
            self.board_tmpl_curr = deepcopy(BOARD)
            # self.current_position = HOME

      def print_board(self):
            for temp in self.board_tmpl_curr:
                  print(*temp)

      def initial_state(self, players):
            for player in players:
                  for index in range(1, 5):
                        row, column = HOME[player.colour][index]
                        self.place_pawn(player.pawns[index - 1], row, column)

      def kill(self, kill_pawn):
            index = kill_pawn.name[1]
            index = int(index)
            row, column = HOME[kill_pawn.colour][index]
            self.board_tmpl_curr[row - 1][column - 1] = kill_pawn.name[0]
            self.board_tmpl_curr[row - 1][column] = kill_pawn.name[1]
            temp_list = []
            temp_list.append(row)
            temp_list.append(column)
            kill_pawn.set_position(temp_list)

      def check_for_index(self, pawn, next_index, next_step):
            pawn_colour = pawn.colour
            if next_step <= 54:
                  if next_index >= len(COMMON_MOVES):
                        remain_index = next_index - len(COMMON_MOVES) 
                        next_position = COMMON_MOVES[remain_index]
                  else:
                        next_position = COMMON_MOVES[next_index]
            elif next_step < 61:
                  remain_step = next_step - 54
                  next_position = FINAL_MOVES[pawn_colour][remain_step]
            elif next_step == 61:
                  pawn.set_status(1)
                  next_position = [0, 0]
            else:
                  next_position = pawn.get_position()
            return next_position

      def check_for_index_second(self, pawn, next_index, next_step):
            pawn_colour = pawn.colour
            if next_step <= 54:
                  if next_index >= len(COMMON_MOVES_SECOND):
                        remain_index = next_index - len(COMMON_MOVES_SECOND)
                        next_position = COMMON_MOVES_SECOND[remain_index]
                  else:
                        next_position = COMMON_MOVES_SECOND[next_index]
            elif next_step < 61:
                  remain_step = next_step -54
                  next_position = FINAL_MOVES_SECOND[pawn_colour][remain_step]
            elif next_step == 61:
                  pawn.set_status(1)
                  next_position = [0, 0]
            else:
                  next_position = pawn.get_position()
            return next_position

      def get_next_position_pawn(self, pawn, step):
            current_position = pawn.get_position()
            current_step = pawn.get_steps()
            next_step = current_step + step
            pawn.set_steps(next_step)
            print(next_step)
            if current_position in COMMON_MOVES:
                  current_index = COMMON_MOVES.index(current_position)
                  next_index = current_index + step
                  next_position = self.check_for_index(pawn, next_index, next_step)
            elif current_position in COMMON_MOVES_SECOND:
                  current_index = COMMON_MOVES_SECOND.index(current_position)
                  next_index = current_index + step
                  next_position = self.check_for_index_second(pawn, next_index, next_step)
            elif current_position in FINAL_MOVES[pawn.colour]:
                  current_index = FINAL_MOVES[pawn.colour].index(current_position)
                  next_index = current_index + step
                  next_position = self.check_for_index(pawn, next_index, next_step)
            else:
                  current_index = FINAL_MOVES_SECOND[pawn.colour].index(current_position)
                  next_index = current_index + step
                  next_position = self.check_for_index_second(pawn, next_index, next_step)
            return next_position    

      def place_pawn(self, pawn, x_cord, y_cord):
            current_position = pawn.get_position()
            raw = current_position[0]
            column = current_position[1]
            self.board_tmpl_curr[raw -1][column - 1] = " "
            self.board_tmpl_curr[raw -1][column] = " "
            self.board_tmpl_curr[x_cord - 1][y_cord - 1] = pawn.name[0]
            self.board_tmpl_curr[x_cord - 1][y_cord] = pawn.name[1]
            temp_list = []
            temp_list.append(x_cord)
            temp_list.append(y_cord)
            pawn.set_position(temp_list)

      def move_pawn_out_home(self, pawn):
            x_cord, y_cord = FIRST_MOVE[pawn.colour]
            if self.board_tmpl_curr[x_cord - 1][y_cord - 1] != " ":
                  self.place_pawn(pawn, x_cord, y_cord + 2)
            else:      
                  self.place_pawn(pawn, x_cord, y_cord)
