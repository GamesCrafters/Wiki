Local Loopy Solver Writeup Fall 2010
====================================

Overview:
=========

The local loopy solver/quickcross team and the alignment team joined together as the alignment team could not solve the loopy version of their game without the solver.

Local Loopy Solver:
-------------------

The local loopy solver is built loosely off of the top-down solver, allowing for loopy games to be solved on a local machine (as opposed to the mapreduce loopy solver).

How the solver works: stuff goes here

QuickCross:
-----------

QuickCross is a very basic loopy game. A win is achieved by being the player to put down a piece that accomplishes 4 in a row horizontally, vertically, or diagonally. These pieces must all be oriented either all vertically or all horizontally. The default board is a 4x4 board which begins empty, with each of its 16 slots capable of holding either a horizontal or vertical piece. On a player's turn, the 2 possible moves are placing a new piece down on an empty space, or rotating a piece already on the board. All pieces are identical, and the loopy nature arises from the ability to rotate pieces.

Alignment:
----------
