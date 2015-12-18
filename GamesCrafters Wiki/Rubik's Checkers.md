Rubik's Checkers
================

Rules
-----

-   The game is played on a 4x6 grid (4 columns, 6 rows). Every other row is shifted slightly to the right. Think of a checkers board with 2 less rows using only one of the colors.
-   The game starts with each player having 8 kings (double-colored pieces) on the two rows closest to that player. The one row that is closest to a player is called the "home row."
-   On a turn, a player can either move a piece, jump an enemy piece, or promote a man on his home row into a king.
-   Kings can move diagonally forward or backwards into an empty space. They can also jump an enemy piece diagonally in one direction and landing on an empty space. Kings that are jumped turn into men; men that are jumped are captured.
-   Men can only move diagonally backwards and cannot capture. Men that reach the home row can be promoted into a king again the next turn (the player cannot move a piece if he decides to promote).
-   There are no forced jumps like in checkers, but players can still do multiple jumps.
-   The game ends when one player cannot move (either he has lost all his pieces, or they are all trapped).

Data Structures
---------------

Even though alternating rows are shifted horizontally slightly, each row still has the same number of pieces, so the entire board can be represented as a 4x6 array. There are 2 kinds of pieces which can be either face up or face down, or a square can be empty, which leads to 5 possibilities. Therefore a square can be represented as either a byte or an integer in the array.

Currently the 4x6 array is actually a one-dimensional array that is the same as the one used by the Generic Hash function. We treat the 1D array as a 2D array using the usual 1D-to-2D array transformations.

Text UI
-------

PrintPosition() provides a board that looks like:

      abcdefgh
     ----------
    6|G G G G | Green: 8 pieces
    5| G G G G|
    4|        |
    3|        |
    2|O O O O |
    1| O O O O| Orange: 8 pieces (Orange's Turn)
     ----------

Note that like in Checkers, each other square is not used. Also note that this is for a 4x6 board. Due to current hash function limitations, we are using a smaller board (such as 4x4 or 2x6) as a starting point.

Variants
--------

Rubik's Checkers is very similar to normal Checkers (who'd have guessed?). We plan on having every single rule that makes Rubik's Checkers different from normal Checkers be controlled by a boolean that can be toggled at runtime. This lets one play regular Checkers rules, or something in between, if so desired.

The board size can also be reconfigured. As stated before, we are using a smaller board than the full 4x6 due to hash limitations. Hopefully one day we can get a 4x8 board (for normal Checkers) working.

Things to look into include all the international variants of Checkers rules ([Draughts](http://en.wikipedia.org/wiki/Draughts), etc).

Project Members
---------------

Johnny Tran

Steve Wu
