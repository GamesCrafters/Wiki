GamesmanWeb\_(Dino-Dodg'em)\_Writeup\_Spring\_2010
==================================================

About the Project
-----------------

### Goal

To create a fully functional version of Dino-Dodg'em available for play on GamesmanWeb with all Gamesman Classic supported variants and GUI enhancements such as skins.

### Members

-   **Sam Kazemkhani**:
    -   Coded functions to move pieces, manipulate arrows, and assist in game rule handling
    -   Did a lot of the necessary debugging to keep the project running smoothly

<!-- -->

-   **Omer Sagy**:
    -   Coded board generation algorithms
    -   Created several iterations of art assets (to be reintroduced to the game with the skins feature)
    -   Wrote the project write-up

Overview
--------

-   **Dino-Dodg'em**
    -   Object of the game is to move all of the player's pieces to their goals
    -   Players take turns moving one piece at a time
    -   Stalemates possible and inevitable in perfect play
    -   Gameplay is easy to learn, making it an ideal kid's game
    -   Game can be played with variable board sizes for great variation in play dynamics.
    -   Many rule variations available to implement as development continues.

<!-- -->

-   **Interaction with the Game**
    -   Players click on the trademark Gamesman arrows to interact with the pieces.
    -   Pieces move in the direction of clicked arrows and eventually into the goals.

Code Overview
-------------

### Design

-   **Resizeable Board**
    -   Board is square and constructed with nested looping.
    -   Rules for the number of starting spaces and empty spaces are kept in these loops.

<!-- -->

-   **Pieces and Arrows**
    -   Arrows and pieces are kept updated through hiding and positioning as opposed to repeated generation.
    -   Pieces are animated and moved with the JQuery library for easy animation modifications/maintenance.
    -   Move Values are intended to be displayed on the arrows, not the board spaces.

### Code

Problems and Bugs
-----------------

-   Horizontal lines between rows of the board - to be fixed by manually moving up all squares/pieces 5 pixels.
-   Communication with the server is not yet fully operational.
-   Support for variations is not yet implemented.
-   Only the solutions for the 3x3 Dino-Dodg'em board can currently be accessed.
-   Little documentation in existing framework for GamesmanWeb games

Future
------

-   **Final Product**
    -   Customizable board and play experience, including variations and skins.
    -   Human vs. Computer and Computer vs. Computer play.
    -   Larger and smaller boards solved.
    -   Support for as many browsers as possible!

