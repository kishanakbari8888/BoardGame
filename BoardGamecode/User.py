from Piece import Piece
import board


class User:
    """
    This is User class
    """
    def __init__(self, name, colour):
        """
        Initialize the class

        Args
            name(str): name of User
        """
        self.name = name
        self.colour = colour
        self.pawns = []
        for i in range(1, 5):
            pawn = Piece(colour[0] + str(i), colour)
            self.pawns.append(pawn) 
                
    def set_color(self, color):
        """
        This function set color of Pieces

        Args
            color(str): color of piece
        """
        self.color = color
        for i in range(4):
            name = "{}{}".format(color[0], i+1)
            tem_piece = Piece(name, color)
            self.pieces.append(tem_piece)

    def update_position(self, name, position):
        """
        this funnction Update the position of piece

        Args
            name(str): name of piece
            position(list): new position of piece
        """
        tem_name = int(name[1]) - 1
        self.pieces[tem_name].set_position(position)

    def get_pawn_by_name(self, name):
        """
        this function gives pawn object for given name

        Args
            name(str) : name of pawn
        """
        for pawn in self.pawns:
            if pawn.name == name:
                return pawn
        return 0

    def get_piece_not_in_home(self):
        """
        This function return the list of pieces
        which is not in home

        Return
            list
        """
        not_home_pawns = list()
        for pawn in self.pawns:
            tem = pawn.get_position()
            if (tem not in board.HOME[pawn.colour]) and pawn.status == 0:
                not_home_pawns.append(pawn.name)
        return not_home_pawns
    
    def get_piece_in_home(self):
        """
        This function return the list of pieces
        which is in home

        Return
            list
        """
        home_pawns = list()
        for pawn in self.pawns:
            tem = pawn.get_position()
            if (tem in board.HOME[pawn.colour]) and pawn.status == 0:
                home_pawns.append(pawn.name)
        return home_pawns

    def get_new_location(self, name, step):
        """
        This return the new location of piece

        Args
            step(int): number of step
            location(list): current locattion
        """
        tem = int(name[1])
        location = self.pieces[tem]
        for _ in range(step):
            x = location[0]
            y = location[1]
            location[0] += self.board[x][y][0]
            location[1] += self.board[x][y][1]
        return location

    def __str__(self):
        tem = "Name of Player is {}\n".format(self.name)
        tem += "Color of piece is {}".format(self.color)
        return tem

        