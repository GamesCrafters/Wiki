GamesmanMobile\_(Android\_-\_Connections)\_Writeup\_Spring\_2010
================================================================

The Project and Its Members
---------------------------

### Goals

To create a playable Android Application for Connections capable of connecting to a server to receive move values (winning, losing, or tying)

### Members and Responsibilities

**Derrick Cheng** and **Kyle MacNamara** worked as a pair in programming in order to increase productivity and decrease error. Both of us had equal contribution in the internal representation, its incorporation with the Android Graphical Interface, and its connection to the server.

Code Framework
--------------

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

Problems and Bugs
-----------------

### Using TableLayout

### Integrating Connect4 and VisualValueHistory

This was the most long-standing bug we had to fix in this project. In Android systems, only one application can be displayed on the screen; other applications cannot be actively displayed on the screen at the same time. We needed information from the Connect4 application to be passed to the VisualValueHistory class, but we could not pass information to the VisualValueHistory application if it was inactive. We also had problems retaining a single VisualValueHistory application and resuming the same application upon start, instead of having the Connect4 class create a new VisualValueHistory application each time the visual value history was accessed. The first problem was solved by retaining information in the Connect4 class and having the VisualValueHistory application access this information as needed upon the resuming of the VisualValueHistory application. The second problem was solved by enabling a flag in a variable required to begin the application such that an existing application would be resumed each time the application was called.

Future Development
------------------

### Short-term goals

-   Use canvas to allow for dynamic piece placement as well as making our game board look almost identical to the physical board game
-   Implement visual value history done by our android visual value history team.
-   Implement methods of the librarified methods/classes created by the Connect 4 Android team, such as Redo/Undo move and the sliding bar.

### Long-term goals

-   2 player phone to phone battle
-   Implement AI computer.

