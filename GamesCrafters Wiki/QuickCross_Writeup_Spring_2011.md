QuickCross\_Writeup\_Spring\_2011
=================================

Process
=======

First I learned about the Android platform through reading the Android documentation on the Android website and then I started to learn the GamesmanMobile Code Base. After learning both of these, I reviewed the code for Connect 4 and 1,2...10 to understand the structure of making a game. After this, I started coding QuickCross and completed it to its current state.

Bugs present/fixed
==================

-   The option menu still needs to be changed so that only 3x3, 3x4, 4x3, and 4x4 sized boards can be selected.
-   Need to add the option of changing \# of pieces in a row to win
-   Currently, when two computers play, there is no delay so the user can't see the computers make the move. This needs to be changed so that computers will delay there moves for a bit.
-   The delay option in the Option menu does not work.

Code Structure of QuickCross: (3 classes)
=========================================

-   Board: Coded the GUI for QuickCross that changes the board size given what is entered in the Options menu. Added touch events so that the direction that you drag, after touching the spot you want to place your piece, determines the orientation of the piece placed. In the case that the move is a spin, this direction will not matter.
-   Game: Coded game to accept variable rows, columns, and pieces in align (though never gave the option of changing pieces in align). The data structure used to represent the board is an array.
-   Options: Gets user input data such as board size and communicates with the game.

Final Product
=============

QuickCross can be played without the server for any variable board size but the \# in a row is set to 3. You can play with both players as computers or just one player as a computer or both players as humans. Undo and Redo works for every case. For when player is a computer, undo will undo both the computer's move and your move so that it will be your turn again. QuickCross is not connected with the server yet so perfect play + VVH + remoteness do not function yet. However, random play is supported.

Future Development
==================

The option menu needs to be standardized throughout the GamesmanMobile platform. QuickCross needs to be connected to the database and VVH + remoteness needs to be added.
