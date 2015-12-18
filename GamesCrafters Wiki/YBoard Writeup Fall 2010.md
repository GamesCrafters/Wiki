YBoard Writeup Fall 2010
========================

Goals:
------

Create a new and more efficient Y board representation of the game while still being able to generalize it for different configurations of the game. Release a more stable implementation of Y board and ensure that all code is properly documented in order to avoid confusion for future gamescrafters working on this project due to its complexity.

Members / Tasks:
----------------

-   Glenn Sudgen
    -   Helped in organizing team meets and set-up weekly goals as team leader.
    -   Wrote general code framework for the new implementation of Y Board.
    -   Maintained code documentation.

<!-- -->

-   Ihor Proskurin
    -   Created the mathematical model of the Y board.
    -   Implemented the isWin algorithm.

<!-- -->

-   Daniel Corral
    -   Testing (~250 rigorous test cases).
    -   Ensured algorithms worked properly.

What we did:
------------

### New efficient Y board representation:

-   Instead of geometrical representation, we introduced radial numeration of the nodes on Y Board. Triangles start from 0 (most inner) to N (outer). Each of them has 3\*N nodes (starting from 0..3\*N-1). Therefore, each node is represented as a set of \[Triangle Number, Node Number\].
-   This allows to create representation for the boards of any size and easily computer whether a certain player win or not.

### getNeighbors:

-   Neighbors are divided into outer, inner, and same-layer neighbors. To define each kind of neighbor, we came up with general formulas. Interesting fact is that our generic formulas work for both inner and outer triangles!
-   getNeighbors main task is to find all neighbors for a given node and keep only the ones that contain a specific piece (‘X’ or ‘O’), and sort them in clockwise order.

### isWin:

-   Instead of breadth or depth search, we used custom “maze” search. In general, it works much faster than other algorithms.
    -   Iterate through the nodes on the left side. if it contains a given piece, start maze search from it.
    -   For each node, move to one after previous in clockwise order until
        -   we reach all three sides -&gt; WIN
        -   we reach bottom side (there’s no way we’ll get to the right anymore) -&gt; UNDEFINED
        -   we come to the start-node -&gt; UNDEFINED

Future goals:
-------------

-   ASCII representation for further testing.
-   Interact with database.
-   Work on Web-UI implementation.
-   Optimize mathematical formulas for getNeighbors (if possible).
-   Use pre-calculated database of nodes’ neighbors instead of calculating them on the fly.
-   Maintain proper code documentation (as it can be difficult for new teams to read already written code). We highly recommend commenting code!

