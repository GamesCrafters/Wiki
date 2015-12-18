Reversi Writeup Fall2010
========================

Goals
-----

-   To implement the game Reversi so that it would be playable after being solved.

Initially, our team thought that we had to write a hasher specific to Reversi to use, but we ended up using the general DartboardHasher instead. Additionally, the game took more time to implement than we had originally anticipated.

Implementation
--------------

### What we did

The game uses the DartboardHasher to hash the boards of this game. The game also has an internal representation of the board, based off of the DartboardHasher. We included an isChildrenValid field to avoid repeated calculations of obtaining the children of the current board. Most of the work done for the game is in the method getChildren. In the method getChildren, we check all the empty spaces on the game board to see if there is at least one adjacent opposing piece cell that also has a cell with a piece of the same color at the end of a straight line projecting from that opposing cell. ![](Othello_Ex2.png "fig:Othello_Ex2.png")

In the game board shown above, the first cell that will be checked is C4. It is currently black's turn and in this cell, getChildren will be able to find that it a flippable piece to its bottom-left. Since there is a valid move at C4, it will place a black piece on C4, flip the pieces that were found, then take another pass through all the neighbors to see if there are any more pieces to flip. In the second pass of the game board shown above, getChildren will find that it has another neighbor that is flippable to its bottom. Even though the next closest flippable piece is two pieces away, getChildren will still recognize this and flip the pieces between C4 and C1.

### Changes to other files

Our team added a file, edu.berkeley.gamesman.solver.ReversiSolver.java, which is a solver specific to Reversi that incorporates the passes needed for the game of Reversi. The solver allows for passes to be counted as a valid move. A job file was also created to solve 4x4 Reversi.

Future changes
--------------

-   The current Reversi implementation does not include a way to pass the current player's turn if there are no more valid moves when playing. The solver, however, will take into account passes.
-   Optimize getChildren and isFlippable to consume less memory and time.

