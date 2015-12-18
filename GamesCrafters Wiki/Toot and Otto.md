Toot and Otto
=============

Project Overview
----------------

### Goals

The goal of this project was to implement and solve the game Toot and Otto

### Members/Tasks

-   **Matt Torok** was the sole team member assigned to Toot and Otto.

### Project Description

Toot and Otto is a game similar to Connect 4 where two players have a 6x4 board, and each players 12 pieces: six 'T's and six 'O's. One player has the goal of spelling the word 'Toot' on the board, the other tries to spell the word 'Otto' on the board. The pieces drop in from the top to the lowest position available in that column.

The project focused on attempting to modify the existing solver for Connect 4 to support Toot and Otto. However, this proved challenging for me personally. The code is advanced and the changes I was attempting to make non-trivial. For example, simply modifying the code to check primitive values required that I go in and change bitsetboard to not simply check if there are *n* in a row of a certain color, but to go in and check for either "toot" or "otto". This in turn necessitated changes to helper classes, and existing algorithms.

Additionally, because this was my first semester in Gamescrafters, and I had thus no familiarity with the existing codebase, or combinitoric game theory solving at all, my progress was much slower than I anticipated.

By the end of the semester, Toot and Otto had not been solved.

### Next Steps

I continue to work on Toot and Otto over winter break. I am hoping to work with David Spies in the new year in order to better understand his existing code, and thus fully implement the game. The goal is to have it solved by the start of the next semester.
