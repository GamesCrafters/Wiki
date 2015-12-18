GamesmanWeb (Connections) Writeup Spring 2010
=============================================

About the Project
-----------------

### Goal

To create a fully functional version of Connections using HTML and JavaScript available for play online.

### Members

-   **Ziang Xie**:
    -   Coded the board generation function
    -   Figured out how to handle events and possible spaces to move
    -   Integrated Connectons into the gc-web framework--currently makes server requests but location/format of parameter string unknown

Overview
--------

-   **Connections**

The following instructions taken from board game geeks:

1.  Players sit at right angles to each other.
2.  Each player chooses a color.
3.  Players take alternate turns at starting play.
4.  Players place one tile of their colour at each turn.
5.  Players must place their colour tiles end to end with their colour squares on the grid.
6.  Players must NOT place their tiles between the colour square and the edge of the board.
7.  Players may start anywhere on the grid (as per paragraph 5)
8.  Players are not obliged to place their colour tiles end to end with tiles already laid.
9.  Average duration of each contest 2 to 5 minutes.

-   Objective: Is to establish a line or connection of your colour across the board connecting your color squares \[the sides where your color of squares are right next to the gameboard edge\] OR surround your opponent's color \[including just one of the board's square dots that is their color\].

When boxing in you must completely surround them with your color - you can't use the edges of the board.

-   **Interaction with the Game**
    -   Players click on the spaces between the small squares to make a connection between them
    -   Hovering in allows players to see whose turn it is--squares where it is possible for red to move is colored pink, for blue, lightblue
    -   Dummy move-values and prediction can also be turned on and off

Code Overview
-------------

### Design

-   **Resizeable Board**
    -   Board is square and constructed with nested looping
    -   Rules for the number of starting spaces and empty spaces are kept in these loops.

<!-- -->

-   **Bridging Squares**
    -   Clicking on a given space creates either a vertical or horizontal connection, depending on the current turn value and the row and column of the space that was clicked
    -   Pieces are animated and moved with the JQuery library for easy animation modifications/maintenance.
    -   Move values are currently displayed on the clickable areas as well
    -   There is currently primitive win detection for bridges all the way across; however, boxing in is not included

### Code

Pending Issues and Bugs
-----------------------

-   Currently the move-values and predictions are simply dummies due to request not having server to connect to
-   The interface also needs to be put and formatted for the nyc server
-   JQuery animation has vertical bridges coming in slightly from the left

Future
------

-   **Final Product**
    -   Human vs. Computer and Computer vs. Computer play.
    -   Larger and smaller boards solved.
    -   Variations such as misere
    -   Move value history
    -   Undo

