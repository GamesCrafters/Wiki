Go
==

Rules
-----

1.  The game board is a square grid of intersections.
    1.  The size of the grid is notionally arbitrary, but the standard board size is 19x19.
        1.  9x9 and 13x13 are also commonly used for special purposes.
        2.  The board size should be an odd number.

    2.  Each intersection has between one two and four neighbors, defined as the intersections adjacent along grid-lines.

2.  There are two players, Black and White.
    1.  Or abstractly, there are two players, full stop.

3.  Each player has a notionally infinite number of stones in his color.
    1.  More abstractly, each player has notionally infinite pieces distinct from those of his opponent.

4.  The players alternate turns; Black goes first.
    1.  Well, one of them goes first.

5.  On a turn, a player may pass or play.
    1.  When a player passes, it becomes his opponent's turn with no other change in the game state.
    2.  To play, the player places one of his stones on an empty intersection on the board.
    3.  When both players pass in succession, the game ends and is scored.

6.  Adjacent stones of the same color are part of the same "string".
7.  Empty intersections adjacent to a string are referred to as its "liberties".
8.  If a play reduces the number of liberties on a string to zero, all the sting's component stones are removed from the board as "captives".
    1.  Note that the liberties of strings on the board are resolved before the liberties of the last played stone.

... and more ...
