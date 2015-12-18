Hex
===

Status
------

Segfault resolved, all core functions appear to work properly except DoMove. Primitive needs to be revised to deal with S-shaped paths.

History
-------

Hex was developed independently by Piet Hein at the Niels Bohr institute, and John Nash at Princeton University. The name "Hex" was first coined by the Parker Brothers as a name for their commercial version of the game.

Rules
-----

A Hex board consists of an N x N rhombus of hexagonal cells. Alternatively, it can be represented as a square board whose cells have 6-connectedness (each cell is "connected" to all but two opposing neighbors). There are two players, traditionally Red and Blue. Each player controls two parallel sides of the rhombus. A player wins by connecting their two sides.

Theory
------

John Nash demonstrated that Hex can never end in a tie. Simple strategy-stealing argument demonstrates that the first player always has a winning strategy. It goes as follows:

1.  Given: Hex can't end in a draw.
2.  Given: Having an extra piece is never detrimental to a player's position.
3.  Either the first player or the second player must have a winning strategy (from 1).
4.  Assume the second player has a winning strategy.
5.  The the first player makes a random move and "forgets" about it, and then plays the second player's winning strategy as if the second player is now the first.
6.  Whenever the strategy calls for the first player to place a piece on a cell (s)he already controls (s)he places another piece at a random location.
7.  Because the second player has a winning strategy, when the first player uses it (s)he will win the game. This is a contradiction, as the second player him/herself also has a winning strategy.
8.  Therefore, the first player must have a winning strategy.

Strategy
--------

A winning strategy is known for boards up to and including 9 x 9. It has been solved (strongly) for all boards up to and including 6 x 6 (Maybe [ODeepaBlue](ODeepaBlue "wikilink") will change that...).
