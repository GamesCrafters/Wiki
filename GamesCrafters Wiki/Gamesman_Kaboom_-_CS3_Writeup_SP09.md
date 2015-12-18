Gamesman\_Kaboom\_-\_CS3\_Writeup\_SP09
=======================================

What we did - Overview
======================

CS3 was in need of more games for their final project. And so, we originally designed the regular Connect 4 for gamesman. However, we decided the game was too easy and similar to the programming involved in tomorrow's tic tac toe. Therefore, Gamescrafters decided to add bombs to make the game a little more difficult.

How to play
===========

Kaboom is played on a rectangular i rows by j columns board. The X pieces belong to X-player, and O pieces to O-player. \* symbolizes Xplayer’s bomb, while @ symbolizes O-player’s bomb. The implementation handles an arbitrary number of rows, columns, and number of pieces needed in a row to win.

To Move
=======

The game begins with a blank board. On one’s turn, a player “drops” their piece or bomb into a column from the top. It falls vertically until it reaches another piece, or end of the column. On their turn, a player may choose to detonate a bomb instead of dropping a piece, which removes the bomb and all adjacent pieces to the bomb (i.e. left, right, top, bottom pieces). If another bomb happens to be one of the adjacent pieces, it is also detonated. You must move if you can. I.e., If the board is full but has one of your bombs in it, you must detonate it

To Win
======

N number pieces/bombs in a row from the same player causes a win for that player. Pieces or bombs may connect vertically, horizontally, or diagonally. If both players have n-in-a-row as a result of detonation, it is a draw. If the board becomes full with no n-in-a-rows and no bombs remaining to detonate, it is also a draw.

Compulsory Rule Changes
=======================

**Misére Rules:** The player who connects n pieces loses. **Super-bomb:** Bombs remove entire rows and columns

Position Representation
=======================

(Player xbombsleft obombsleft row row row …) Player stores whose turn it is (x or o). xbombsleft and obombsleft store X-player and O-player’s number of remaining bombs, respectively. Each row is in the form pppp… where p is “x”, “o”, “\*”, or “@”, representing the corresponding piece or bomb on the board; “–” if blank.

Future
------

Future versions can add the gui as well as a more efficient way to search the board for bombs and detonating them. More compulsory rules can also be added.
