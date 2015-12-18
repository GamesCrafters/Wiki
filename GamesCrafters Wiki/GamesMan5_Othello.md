GamesMan5\_Othello
==================

Description
===========

Implementation of Othello on the web interface.

Members
-------

-   Alex (Tong) Wu
-   Howard Guan

Done
----

-   Othello now works on the web interface.
-   A transparent circle of the current player’s color shows all the possible moves for that player.
-   Clicking on the transparent circle will make the move for the current player.

Notes
-----

-   Board structure: Columns from left to right goes from a -&gt; d. Rows from top to bottom goes from 3 -&gt; 0.

To-Do
-----

-   Implement a better way of telling the current player that he/she has no more moves and must skip their turn. The way that it is currently implemented is that if there are no moves, it draws a smaller circle with the color of the current player at the center of the board. When the player clicks that circle, it skips the turn and it becomes the second player’s turn.

<!-- -->

-   Implement a bar at the bottom that shows a ratio of black to white pieces so the players can easily see who is winning by looking at the bar at the bottom. If the bar has more white than black then there are more white pieces than black on the board so white is wining and vise versa.

