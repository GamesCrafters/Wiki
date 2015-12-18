GameDroid\_(Android\_-\_Othello)\_Writeup\_Fall\_2010
=====================================================

Project Team
------------

### Mission

To create a playable Android Application for Connections capable of connecting to a server to receive move values (winning, losing, or tying)

### Members and Responsibilities

**Derrick Cheng** and **Kyle MacNamara** worked as a pair in programming in order to increase productivity and decrease error. Both of us had equal contribution in the internal representation, its incorporation with the Android Graphical Interface, and its connection to the server.

The Code
--------

### Game.java

This class is the main internal representation of our board. In order to create a clear-cut abstraction layer from the Android Gui which we implement in Gameboard.java), we keep this code clean of any mention of Android API.

Our board is represented by 2-D array of integers. Each integer represents a different type of piece, which we use static finals to represent: horizontal/ vertical lines and nodes of each player as well as blank spaces.

In order to check whether the game state is primitive, we use a depth first graph traversals across our 2-D array. For example, for Player 1's who's goal is to connect North or South. For each Player 1 (blue) node on the north edge of the board, we follow the connected blue nodes and blue lines of Player 1 and check if it eventually reaches the corresponding South side. If this case is reached, player 1 has won. Same algorithm is applied for Player 2 except that Player 2 is red and is trying to connecting East and West.

We also create a generate moves values, which generates the position of valid moves of players. This GenerateMoves method is useful in our utilization of the server for move values and move value visualization in our Android framework.

### GameBoard.java

This class is the Android load frontend of our Game.java backend.

Our current graphical representation of our board is using a table layout of image views, where each image view is a different microsoft paint jpg, hand crafted my Kyle MacNamara himself.

Each image view has an onclicklistener waiting for that imageview to be pressed. if that image view is pressed the image of the piece will swap out.

In the future, we will convert this layout using 2-D graphics in order to make dynamic piece placements possible.

### Other classes

GamevalueService, MoveValue, RemoteGameValueService are classes use to implement our menu as well as the conversation with the web server

Accomplishments
---------------

completed talking to the server, allowing for moveValues, showPrediction, unDo Redo Functionality, the slider, as well as Visual Value history for Connections. Basically, every button that is allowed by pressing menu during connections game play works. moveValues and unDo redo, and Visual Value history only works for 4 by 4 since thats the only one that the server solved.

The Future
----------

### Short-term goals

-   Use canvas to allow for dynamic piece placement as well as making our game board look almost identical to the physical board game
-   misere functionality once misere is solved by the solver team

### Long-term goals

-   2 player phone to phone battle
-   Implement AI computer.

