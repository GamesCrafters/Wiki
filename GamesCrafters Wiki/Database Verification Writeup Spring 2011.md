Database Verification Writeup Spring 2011
=========================================

Overview
========

Out team's goal was to write and test a Loopy Solver that is easily parallelized with the Hadoop Map-Reduce Framework.

Members
-------

-   **Alex Degtiar**
-   **Royce Cheng-Yue**

Loopy Hadoop Solver
-------------------

The function of the Loopy Hadoop Solver is to solve games that have circular move histories making the game tree more like a game graph. This is different from a regular tier game since a loopy game may last infinitely long and a given position may be seen multiple times on the same path of play. This required us to distinguish a Tie, where the game ends with neither play winning, from a Draw, where the game is stuck in a loop and if one play deviates, that player will lose.

To tackle this problem, we split the solver up into 3 stages, each with its own mapper and reducer.

##### Stage 1

The task of the Stage 1 map-reduce pair is to create a blank database for the game being solved.

The mapper simply goes through each range in the game's input splits and creates a database that will eventually hold its values. For each position in the range, the value is initially set to IMPOSSIBLE since we do not know which positions can be reached from playing the game at this stage.

After all the databases are created, the mapper gives these to the reducer which then creates a file that maps a given hash of a position to the database files created in the mapper.

##### Stage 2

The stage 2 map-reduce pair traverses the game tree and marks all seen positions as a Draw and also records the number of children they have in a separate file. At the end of this stage, all possible positions will be DRAW while all impossible positions will still be marked as IMPOSSIBLE. Also, when it hits a primitive position, the traversal records that primitive position in a separate database. Unlike this first stage, this stage is iterative which many iterations of map-reduce pairs before completion.

The mapper in this stage merely takes a position, generates its children and outputs their hashes to the reducer.

The reducer first sorts the hashes that it gets.

-   If the position has been seen, it ignores it.
-   If the position is a primitive, it records the value and does not pass it on to the next iteration of the mapper.
-   Else, the position has not been seen and is not primitive so it is marked as a Draw and the number of children it has is recorded.

This loop continues until the reducer has seen all the legal positions and outputs nothing to the mapper.

##### Stage 3

The bulk of the actual solving happens in the stage 3 map-reduce pair. This stage starts with the file of primitive positions that stage 2 created and does a bottom-up solve of the game tree. On a high level, it takes a position, generates its parents, and does a sequence of checks described later. This continues until there are no more updates to be bubbled up. At this time, the game is declared as solved.

The mapper for this stage will take a given position and its record which contains its value and remoteness among other information regarding the value of the position. Then it will generate its parents and pass each parent along with the flip of the record (ie add to the remoteness and change win to lose) to the reducer.

The reducer basically check the following logic:

-   If the current position is a LOSE, then the parent must be a WIN since is has a losing child. Therefore, update the parent if it isn't a win already.

<!-- -->

-   If the current position is a TIE, then the parent must be at least a TIE so update it if it is worse than a tie.

<!-- -->

-   The current position cannot be a DRAW.

<!-- -->

-   If the current position is a WIN, decrement the parent's numChildren counter in the file that was created in stage 2. If this counter reaches 0 then mark the parent as a LOSE since all its children are loses

The Reducer will output all updates for the next iteration of the mapper. This will continue until the reducer outputs no more updates meaning the game must be finished.

Testing
-------

-   We have verified the output from this solver against the GamesmanClassic loopy solver for the following quick cross boards:
    -   3 by 3 with 3 in a row to win
    -   4 by 3 with 3 in a row to win

Results
-------

-   We have solved the following quick cross variants:
    -   4 by 4 with 3 in a row to win
        -   This is a Draw game
    -   4 by 4 with 4 in a row to win
        -   This is also a Draw game

Future Goals
------------

-   Use it to Solve more loopy games on the icluster

