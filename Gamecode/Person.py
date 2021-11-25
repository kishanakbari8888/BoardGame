from User import User

SECURE_LOCATION = [[14, 20], [18, 20], [8, 38], [8, 50],
                   [14, 68], [18, 68], [24, 38], [24, 50]]


class Person(User):

    def __init__(self, name, colour):

        super(Person, self).__init__(name, colour)
    
    def move(self, pawn, step, current_board):
        """
        this update the position

        Args
            pawn(obj): object of pawn
            location(list): current location of piece
            current_board(list): current board
        
        Return
            list
        """
        pawn_at_home = super(Person, self).get_piece_in_home()
        if step == 6 and pawn.name in pawn_at_home:
            current_board.move_pawn_out_home(pawn)
        else:
            new_location = current_board.get_next_position_pawn(pawn, step)
            print(new_location)
            temp = None
            if current_board.board_tmpl_curr[new_location[0] - 1][new_location[1] - 1] != " ":
                temp = current_board.board_tmpl_curr[new_location[0] - 1][new_location[1] - 1]
                temp += current_board.board_tmpl_curr[new_location[0] - 1][new_location[1]]
                concated_pawn = super(Person, self).get_pawn_by_name(temp)
                if concated_pawn == 0 and new_location not in SECURE_LOCATION:
                    current_board.place_pawn(pawn, new_location[0], new_location[1])
                    return(temp)  #kill
                else:
                    current_board.place_pawn(pawn, new_location[0], new_location[1] + 2) 
                    return 0
            elif current_board.board_tmpl_curr[new_location[0] - 1][new_location[1] + 2] != " ":
                temp = current_board.board_tmpl_curr[new_location[0] - 1][new_location[1] + 1]
                temp += current_board.board_tmpl_curr[new_location[0] - 1][new_location[1] + 2]
                concated_pawn = super(Person, self).get_pawn_by_name(temp)
                if concated_pawn == 0 and new_location not in SECURE_LOCATION:
                    current_board.place_pawn(pawn, new_location[0], new_location[1] + 2)
                    return(temp)  #kill
                else:
                    current_board.place_pawn(pawn, new_location[0], new_location[1] + 4) 
                    return 0
            else:
                current_board.place_pawn(pawn, new_location[0], new_location[1])
       
    