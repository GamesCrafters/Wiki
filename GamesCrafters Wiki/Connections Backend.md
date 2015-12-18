Connections Backend
===================

### Goal

The goal of my project was to better understand the architecture and working of GamesmanJava by implementing the game Connections.

=== Change Description == I modified and added to existing code in src.game.Connections.java. The existing code took care of one win condition (if a player manages to complete a line from one end of the board to the other), and implemented the check for the other winning condition (if a player manages to complete a closed box of any dimensions).

Problems
--------

-   Code needs more testing.
-   I figure a more elegant way to check for the second win condition is in order. Presently I'm just using an ArrayList to store all the "traversed" points of a player, and returning true if a point is repeated (ie if the path is cyclic).

Next Steps
----------

David mentioned a new hashing function for Connections, I figure that would be the next step in fully implementing the game.
