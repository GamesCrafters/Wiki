GamesmanWeb (The Game of Y) Writeup Spring 2010
===============================================

About the Project
-----------------

### Goal

At the start of the semester, the group decided that, this semester, one of the primary goals would be to solve and create GUI's for two games: Y and Connections. The particular aim for this project was to design and create the web interface for The Game of Y. Ultimately, we would like to have the game officially on GamesmanWeb and able to communicate with the server.

### Members

-   **Kevin Morgan**:
    -   Came up with idea for using a Voronoi diagram
    -   Programmed code responsible for generating Y Board
    -   Restructured code to represent physical board

<!-- -->

-   **Jimmy Wu**:
    -   Came up with idea for placing centers as arcs
    -   Assisted in debugging the code for Y
    -   Wrote the project report

Overview
--------

-   **The Game of Y**
    -   Consists of an inner triangle surrounded by outer rows in each direction
    -   Players take turn placing pieces on the board
    -   Goal is to link all three edges together with a contiguous chain of pieces
    -   Impossible for the game to end in a tie

<!-- -->

-   **Two Board Types**
    -   Voronoi Diagram
        -   Drawn like a Voronoi diagram, where pieces are placed on the area in between lines
        -   Connections determined by the number of sides a shape is touching
    -   Triangular Board
        -   Similar to a graph where pieces are placed on the vertices
        -   Edges represent the number of connections to a particular piece
    -   Similarities
        -   All centers with the below exceptions are adjacent to exactly six other centers
        -   Edge pieces touch four
        -   Inner corner pieces are adjacent to five
        -   Outer corners are adjacent to three

Code Overview
-------------

### Design

-   **Resizeable Board**
    -   First difficulty encountered was creating a resizeable, dynamically generated board
    -   Board is slightly complicated to generalize in nature
    -   Original idea was to create a Voronoi diagram

<!-- -->

-   **Voronoi Diagram**
    -   Place centers in a triangular shape to represent the inner hex
    -   Outer centers placed linearly in incrementing rows outside of the inner hex
    -   Board is recolored pixel-by-pixel after each change in color based on which center is closest to a pixel
    -   Problem: Number of adjacent centers were incorrect

<!-- -->

-   **Arc Voronoi Diagram**
    -   Fixed original diagram by placing centers on the outside in arcs instead of straight
    -   Added trigonometric calculations in code to place centers in correct locations
    -   Included a bar for user to resize and restart the board
    -   Added win/lose coloring, based on random data (not retrieved from the server)
    -   Uploaded onto GamesmanWeb
    -   Problem: Coloring pixels after each click was too costly

<!-- -->

-   **Triangular Board Representation**
    -   Removed the Voronoi diagram drawing function
    -   Placed centers in arches as before, but drew circles around each one
    -   Drew edges from each piece to adjacent pieces, special casing the exceptions
    -   Only circles and edges are recolored after each click
    -   Added functionality of linking pieces together based on color

<!-- -->

-   **Communication with Server**

### Code

Problems and Bugs
-----------------

-   Changing to object oriented design is bugging up the Javascript
-   Game of Y has yet to be solved, color representations not yet made
-   Little documentation in existing framework for GamesmanWeb games

Future
------

-   **Final Product**
    -   Resize-able GUI up on GamesmanWeb, with ability to display win/lose values obtained from the servers

<!-- -->

-   Communication with the server
-   Possible documentation or more extendable framework for GamesmanWeb

