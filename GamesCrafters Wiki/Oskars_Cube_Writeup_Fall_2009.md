Oskars\_Cube\_Writeup\_Fall\_2009
=================================

**Overview of the Project**

Oskars Cube is a three dimensional maze constructed by attaching three two-dimensional mazes at right angles. The difficulty of the puzzle lies mostly in three dimensional visualization rather than size of the game tree. My efforts this semester fall into three categories- continued improvements to user interface, study of interestingness, and proofs about three dimensional mazes in the effort to better understand and be able to construct mazes.

In the effort to study the interestingness of various mazes- with the eventual goal of creating a puzzle more interesting than the original- many metrics were created. They are remoteness (optimal distance from the start to end), bushiness (the sum of brances from the solution path to each position), number of subcomponents (number of disjoint connected components in the maze), branches (number of branches in the played game tree), branches by degree (sum of branches in game by one minus their degree), max branch degree (maximum branch degree minus two), turns (in solution path, number of changes in direction), and plane turns (in solution path, number of changes of direction leaving the plane of the last two moves). A random puzzle can be created with minimum values of each metric. Next observations of how puzzles look and resultant interestingness for values of the metrics.

The idea of an interesting maze is that at some number of points, it is nonobvious which direction is on the solution path, and that past this point, there is sufficient complexity so as to not immediately return to the solution path. Some of the difficulty in analyzing this is that some of this comes directly form the form of the game tree, such as the number of branches, the degree of branches, and length of the puzzle froms directly from the game tree. While the difficulty of the puzzle is strongly tied to the difficulty in three dimensional visualization, so in how the puzzle twists together. The number of plane turns helps describe this since in testing we found many puzzles analagous in other metics to difficult puzzles that were trivial to solve since they mostly reduced to at least ten moves in one plane, moving down a plane, ten more in plane moves, until the plane of the goal square was acheived (also characteristic of bushiness &gt;200, branches &gt;45). Also found to be boring are puzzle faces where at least four horizontal or verticle lines are open, since they aid in creating the previous problem (bushiness &gt;300 creates this). This hints that interestingness could be tied to not just the three dimensional maze, but could be reduced to combining interesting two dimensional mazes. Puzzles with a branch of degree four (really 6, so maximum) almost always generate characteristic lattice effect in the two dimensional mazes (though some of the most interesting puzzles have the degree without the lattice effect), with a resultant very shallow but high number of false trails.

Just added is a feature that allows saving and loading puzzles. The next step in this is to add the dance dance revolution inspired graphical representation of metrics and generate a large number of puzzles, testing the interesetingness of some of the outlyers and other significant points in hopes of better systematizing the process. Then the most interesting can be added as puzzle of note to the online version of Oskars Cube.

Research this semester had two veins, one followed the proof techinque used to prove there always exists a maze of maximum size for any dimension, the other was an attempt to constructively describe mazes starting from small mazes. The write-up of this will follow with diagrams.

*How does it fit into the Big Picture:* Oskars Cube is was orginally one of the several puzzles added in Fall 2008. It was originaly a python puzzle and was then rewritten as a java puzzle using Jeremey's graphics engine written for the Rubics cube. The following semester the Oscars cube project was adapted to generate random puzzles in the vein of the original maze. And now it has branched into being a research project as well as improvements to the code and interface.

*Source Code Location* GamesmanWeb.src.edu.berkeley.gcweb.gui.gamescubeman.OskarsCube

*Status of the Code* The code is in various states as it is still being hacked for experiemental purposes.

*Room for Future Improvements:*

-   Further proofs about the mazes
-   Improved interesting metrics
-   Improvements to speed
-   Improvements to user interface

*To continue working on the project:* To start working on this project one would need basic knowledge of java. An interest in combinatorics would be helpful. From our code base, only knowledge of Jeremey's graphic engine and the webteam's javascript to tie it to the web page are pertinent.
