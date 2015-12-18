Game analysis
=============

The purpose of the **Game analysis** project is to extend the current Gamesman game analysis functionality. Currently, the analysis is limited to displaying a sum of wins, loses, and ties. It is the purpose of this project to extend this analysis to include the number of wins, loses, and ties at each remoteness level, as well find the number of draws. This extended analysis tool will then be used to find patterns in games to use as an 'interestingness' metric, which can then be used to assist in finding mate in N puzzles.

Interestingness metric
----------------------

A game is boring to play if it is not interesting. 1,2...10 is not interesting, for example, because the solution is easily memorized. By contrast, chess is extremely interesting, and for many reasons, one of which is the sheer number of games that can be played. But, in general, how does one tell if a game G is interesting? That is where the interestingness metric comes into play. By analyzing game values, it should be possible to create a heuristic that will determine if a game is interesting.

Mate in N puzzles
-----------------

Most chess puzzles fall in this category - given an artificially constructed board and a given N, the player must find a way to mate his opponent in N moves, against any possible defense his opponent could erect. Once an interestingness metric is found, it should be relatively easy to generate fun mate in N puzzles. An important criteria of mate in N puzzles is that the first move, the key move, *must* be unique.

Current issues
--------------

There are some games that break when subject to analysis - that is, they segfault or otherwise exit abnormally when the user attempts to analyze the game. The following games have been found to break during analysis (this list is by no means complete):

-   Dao
-   Lite-3

Project team
------------

The following people are working on this project:

-   Matt Johnson
-   [Alan Wu](User:Alanwu "wikilink")

