class Piece:
    """
    This is Piece class
    """

    def __init__(self, name, colour):
        """
        Initialize the class

        Args
            colour(str): color of Piece
            name(str): name of Piece
        """
        self.colour = colour
        self.name = name
        self.position = [0, 0]
        self.status = 0         # 0 = Not Win and 1 = Win
        self.steps = 0             

    def get_name(self):
        """
        This function return the name of Piece

        Return
            name(str)
        """
        return self.name
    
    def get_colour(self):
        """
        This function return the colour of Piece

        Return
            colour(str)
        """
        return self.colour

    def set_position(self, position):
        """
        This function set the position of Piece

        Args
            position(str): Home or Not Home

        """
        self.position = position
    
    def get_position(self):
        """
        This function return position of Piece

        Return
            position(list)
        """
        return self.position

    def set_steps(self, steps):
        """
        This function set the steps of Piece

        Args
            steps(int): no of step pawm move

        """
        self.steps = steps
    
    def get_steps(self):
        """
        This function return step of Piece move so far

        Return
            step(int)
        """
        return self.steps

    def get_status(self):
        """
        This function return status of Piece
        Return
            status(int): 0 or 1
        """
        return self.status

    def set_status(self, status):
        """
        This function set the status of Piece

        Args
            status(int): this will 0 or 1
        """
        self.status = status

    def __str__(self):
        tem = "name of Piece is {}\n".format(self.name)
        tem += "colour of Piece is {}".format(self.colour)
        return tem