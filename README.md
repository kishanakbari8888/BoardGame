# BoardGame
---

This repository is created by group-11 - G12. This project is related to Board Game.


# Contributor
---

1.[Jatin Parmar-AU2040118](https://github.com/Jatin-parmar).<br>
2.[Kishan Akbari-AU2040155](https://github.com/kishanakbari8888).<br>
3.[Rashika Jain-AU2020178](https://github.com/kanvipatel16).<br>
4.[Kanvi Patel-AU2040235](https://github.com/kanvipatel16).<br>


# Summary
---

File 1 - Board.py
First, we created a string array to create the board of our game. This is the basic background on which our game works. Next, we make a list named COMMON MOVES. It predicts the next position of the pawns. Common Moves second, similar to common moves, works in the situation when 2 pawns of the same color arrive at the same position. "First move" is a dictionary that gives us the initial location of the pawns of all the different colors. "Final moves" is another dictionary that gives us the final position of pawns. Final moves second is similar to the latter but works only after one of the pawns has reached the end. HOME is a dictionary that contains the location of the homes of the pawns of different colors. Next, we declared a class Board. It contains a constructor and functions like print, initial state, KILL, etc. Kill function eliminates the pawn of a different color and sends it back to its home location. "Check next index" verifies the next position of the pawn. Check next second is similar to this. Get next position function allots the pawn the next position. Place pawn places it to its position. Move the pawn out home moves it from its initial home.

File 2 - User.py
First, we declare a User Class with initializations name, color, and pawns numbers. In this class, the user gets a chance to choose pawn colors according to themselves. Then this class is responsible for updating the position, giving pawn the number, checking up on the pawns outside and inside the home, and also giving them the next position. 

File 3 - Person.py
As the name suggests, Secure Location is a list that contains the 8 safe positions we have on the board. No Pawn can eliminate the rival pawn in this position. Next, we declare a Person class with a constructor and functions like "move". The move is basically responsible for the movement of the pawns on the board. It checks the number on dice. If 6 appears then the pawn can move out of the house and also gets another turn. In the case of other numbers, it moves to required positions as per the numbers appearing on the dice.

File 4 - Piece.py
First, we declare a piece class with initialized color, name, position, status, and steps.
Then we have different functions for returning their values.  

File 5 - Main.py
This file contains functions like roll dice, next turn, previous turn, and start game. Roll dice randomly chooses a number from 1 to 6. "Next turn" is responsible for giving the next turn after one has rolled the dice. "Previous turn" is similar to this and both together are important for a proper movement of dice among the players. Start game initializes the game i.e. all the functions in the previous three files collaborate for the proper working of this function. Starting from giving the user color and pawn to printing the board and taking the game further. After that we have to run the main.py file.


# Youtube Presentation Video
---

https://www.youtube.com/watch?v=EjWccSGgbKY


# References
---

Ludo game project in Python. (n.d.). Retrieved November 25, 2021, from https://projectworlds.in/python-projects-with-source-code/ludo-game-project-in-python/

Geometric algorithms. (n.d.). Retrieved November 25, 2021, from https://www.geeksforgeeks.org/geometric-algorithms/

Petersen, V. (n.d.). Retrieved November 25, 2021, from http://pachisi.vegard2.net/ludo.html

http://www.banglagym.com/wp-content/uploads/2016/06/Ludo_Rules.pdf


