Solver\_journey
===============

Overview
--------

This article is intended to give an in-depth description of all the steps used to solve Connect 4 in GamesmanJava. The goal here is not to provide documentation for the code, but rather to outline the method utilized and draw a "larger picture" which can be implemented in any programming language. I will try my best to refrain from using Java-dependent terminology. In the descriptions that follow, all examples will be on a standard connect 4 board with a width of 7 and a height of 6. I'll try to indicate when numbers are dependent on the width or height of the board.

The Solver
----------

The solver for Connect 4 is a type of [Tier\_Solver.md](Tier_Solver.md "wikilink"). Briefly, this means, it runs through all the positions in the final tier of the game (a position in which the board is completely full, on 7x6, this means all 42 pieces have been played) and recorded in the database. The database record contains information about the value of the position (ie win, lose, or tie) and may or may not also contain the remoteness (how far from the end of the game at best play). When the remoteness is zero (as is the case for all positions in the last tier of connect 4), this is known as a primitive position. The game is already finished.

When the solver has finished evaluating every position in the final tier, it runs through all the positions one tier below, ie the positions where the board is completely full, except for one piece (41 pieces on the board). If a position is either a win, a lose, or a tie, it is marked as such. If it is none of the above (meaning the game is not yet finished), then the [children.md](children.md "wikilink") of the position are all in the final tier (the one solved previously). The values of these positions are looked up, flipped (win becomes lose and lose becomes win), and the best one is chosen to be the record for this position.
