Puzzle\_Writeup\_Fall\_2010
===========================

Overview
========

My project was to make the Python puzzle servers maintainable and use the same infrastructure as GamesmanJava.

Originally the puzzles were all written in our python infrastructure, which consisted of a custom database format as well as a few solvers and a JSON server. The problem is that this server was hard to maintain because it is separate from Java. It had a JSON server, but had to be restarted manually, and in the meantime we had switched everything else to use Thrift.

Some puzzles solved this by doing a port to Java. One example of this is the rubik's cube which is now written entirely in Java and solved using GamesmanJava.

To solve this for other games, doing a port would be too much work, so I wrote a database converter and made Python classes first class Game objects in java using Jython so that they could be served directly.

Code Overview
=============

... finish me ...

Features
========

... finish me ...

Future work
===========

More maintanence on Puzzles.

Most of the work I did was just on the glue code and the javascript.

Some python puzzles like TripleCross would probably be solvable with all settings enabled (I think it should be only 4GB) if only the code wasn't so wasteful, constantly creating and destroying objects. Python just isn't fast enough to solve this, so we would need a native Java port. Triangular Peg Solitaire is incredibly slow considering the small size of its game. I suspect if we made Peg Solitaire use more efficient hashes or even a more compact format (64-bit ints instead of arrays of arrays), we could probably go from 5 (which is the current maximum) all the way to 7 or 8.

The javascript code for some is still broken. Rubik only loads some fraction of the time, and Triangular Peg Solitaire treats all positions as tie (neither win nor loss), which is probably a silly bug somewhere in the database converter or the javascript. I intend to pick off one or two of these over break if they are simple to actually fix.
