Spring 2012 Mancala
===================

**Goal:**
---------

To create a user-friendly program that simulated the board game Mancala in HTML5.

**Members:**
------------

Christopher Fluttershy Jernigan

Eric Kim

Juan Gonzalez

**Introduction:**
-----------------

Mancala is a two-player board game where each player tries to gather the most amount of pebbles in their respective goal pockets called “stores”. A player makes a move by first choosing a pocket with pebbles in it, then dropping pebbles in consecutive pockets. If the last pebble they place lands in an empty pocket, the move is done; otherwise, they pick up the contents of the pocket and continue to place pebbles in consecutive pockets. This continues until there are no more non-goal pockets.

**Implementation:**
-------------------

Animation in mancala is handled by creating a seperate class for pebbles themselves so they can be drawn to the screen and so that pits can keep track of the number of pebbles in it via a stack. The stack is an array of pebbles that are added to the pit and each item in the stack is a pebble object with properties such as color and location on the screen. The pebbles, when created, are randomly placed in the vicinity of each pit and clicking on a pit starts the animation process of moving each pebble to the next pit. The location it moves to is a random location in the next pit and a timer is used to control the velocity of each pit as it travels upon a line to the next pit. Its speed is proportional to its distance.
