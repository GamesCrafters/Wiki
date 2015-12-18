GamesMan Abalone - CS3 Writeup SP09 (by Danica Shei)
====================================================

What we did - Overview
======================

We designed the game Abalone for the CS3 Final Project. It is considered a difficult game and consists of a board similar to Tic Tac Toe.

How to play
===========

Abalone is played on a board with n rows, m columns. For an arbitrary n, m, black occupies the lower left edges and right the upper-right resulting in n +m -3 pieces each. The NW and SE corners are empty. The implementation must handle an arbitrary number of rows and columns. Players can move their pieces across the board and can "push" opponents pieces when they have numerical superiority.

To Move
=======

The players, Black and White, take turns moving one their pieces one position in a row, column, or diagonal. This may result in other pieces moving as well.

To Push:
========

`When one player has numerical superiority in a line or diagonal, she may push the opponent’s pieces down the line or diagonal. If the push results in one of the opponent’s pieces going off the board, the player captures that piece. `

To Win
======

The player who achieves c captures ﬁrst wins. A player loses if she cannot make a move, and is ‘trapped’.

Compulsory Rule Changes
=======================

Misere Rule: The player who achieves c captures ﬁrst loses. A player winsif she cannot make a move, and is ‘trapped’. Freeze-piece: If an unmoved piece could be pushed by opponent on the following turn, the the piece is frozen and cannot move.

Position Representation
=======================

(T row row row …) T stores whose turn it is (b or w). Each row is in the form ppp… where p is “b” or “w”, representing the corresponding piece on the board, or “-” if blank. E.g., here’s the default board: (b bbb- b--w b--w –www)

Future
------

Future versions can add the gui as well as a better way to work the simple graphics so that it doesn't scrunch together when the board is expanded. More compulsory rules can be added as well like hitting your own hand or splitting.
