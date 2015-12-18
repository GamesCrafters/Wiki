TierCutDatabase Alpha-Beta Pruning
==================================

Project Overview
----------------

### Goal

-   The goal is to add alpha-beta pruning to the TierCutDatabase as an optimization over the basic minimax search. Alpha-beta pruning is an algorithm that decreases the number of nodes evaluated in a minimax search tree by stopping the evaluation of a move when there is evidence that the move is worse than a previously examined move. Adding such logic prunes away branches of the search tree that cannot influence the final result of the search.

### Member/Task

-   **Kevin Lee** added alpha-beta pruning to the TierCutDatabase and benchmarked its performance using hadoopTierTicTacToe.

Change Description
------------------

### TierCutDatabase.java

-   Code has been added to allow for alpha-beta pruning.

Problems/Bugs
-------------

-   Code has not been thoroughly tested yet.

Next Steps/Future Plans
-----------------------

### Continue benchmarking/testing

-   Further benchmarking and testing needs to be done with games that are less trivial than Tic Tac Toe.

