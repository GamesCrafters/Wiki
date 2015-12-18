QuickCross\_Web\_GUI\_Writeup\_Spring\_2011
===========================================

Overview
========

This semester, we developed the GUI for the games QuickCross on the GamesmanWeb site: [QuickCross](http://nyc.cs.berkeley.edu:8080/gcweb/ui/game.jsp?game=quickcross)).

Members & Responsibilities
--------------------------

-   **Derek Ngai** , **Nancy Wang**, and **Kevin Wang** worked to create GUI for QuickCross. Met 2-3 times every week to work on the javascript and HTML code together.

QuickCross
----------

QuickCross is a very basic loopy game. A win is achieved by being the player to put down a piece that accomplishes 4 in a row horizontally, vertically, or diagonally. These pieces must all be oriented either all vertically or all horizontally. The default board is a 4x4 board which begins empty, with each of its 16 slots capable of holding either a horizontal or vertical piece. On a player's turn, the 2 possible types of moves are placing a new piece down on an empty space, or rotating a piece already on the board. All pieces are identical, and the loopy nature arises from the ability to rotate pieces. Variants of the game are easily derived by altering the size of the board and the number of pieces in a row required to win.

##### Week 1-4

The three of us were new to GamesmanWeb, so we spent this time learning the tutorials and getting use to Javascript and HTML.

##### Week 5-12

We worked on the local version of the Quickcross Web GUI. We implemented: -displaying board and pieces -displaying value moves (no remoteness and randomized since we haven't linked the game to the database yet). -applied rotation animation for turning pieces -ability to change board size -resize game

##### Week 12-14

After getting the local version of the Quickcross Web GUI working, we put it on the server and onto the GamesmanWeb site. The basics of the game works (win with same pieces in a row or column).

##### Things Still need to Fix

-changing some functions to link the game to the database -resize board based on the box games in, not the whole screen

##### Optimizations

-redrawing only the parts that change, not the whole board every frame
