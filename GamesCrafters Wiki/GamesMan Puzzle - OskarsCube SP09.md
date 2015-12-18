GamesMan Puzzle - OskarsCube SP09
=================================

(this is a working version, more to come!)

Oskars Cube is a puzzle that was added in the fall of 09 along with several other puzzles. It consists of three 2D mazes joined at the corner to form a three dimensional maze. Although the original Oskars Cube has a relatively small solution space, it offers up many variants by changing the individual mazes that generate the puzzle.

This semester most of my efforts went toward expanding Oskars Cube to a randomly generated puzzle, as well as expandable to a larger puzzle. My initial effort went to combinatorially exploring the situation. From there, the original code was significantly modified to work with a cube generator, which generates three 2D mazes. Currently the generator works by generating random numbers and using this to add to the fixed set of squares in the maze. Unfortunately, at the present, the generator is slowed by checks because not every generated puzzle is viable. This greatly slows the generation of large puzzles. However, several hundred thousand standard size puzzles can be generated and solved in twenty minutes on my laptop.

To further the pursuit of pushing our capabilities to the limit, next semester I intend to make the generator much more efficient, as well as modify the solver to solve in all the solution spaces of a given puzzle, not just the one in which the standard end position appears. Other things to explore in puzzle generation also include generating a puzzle of maximum remoteness (it would actually be boring to play because it would have no branches).

Additional changes this semester include:

Count of achievable positions and internal display on unachievable positions (in a good puzzle, the density of achievable positions makes their display useless).

Internal display of the solution path of a puzzle. For the display of this and unachievable positions, the opposite faces of the puzzle were removed. Some viewers prefer playing the puzzle from the inside.

Control over generating a puzzle, for instance, only return a puzzle with remoteness at least n.

Best move now displays movement arrows like the classic Gamesman games. The next stage in this is to change movement from keyboard directed to clicking on arrow.

Changed representation and coloration of start/end.

Search for the most remote start/end in a given solution space.

Getting a working internet version up on the Gamescrafters website. Menu's, instructions, etc still need to be added, but it is playable.

From here the additional features that need to be added are: Menus (start a new puzzle, hide options, change movement keys, zoom in and out, snap to perspective) Clickable movements
