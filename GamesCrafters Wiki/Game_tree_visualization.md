Game\_tree\_visualization
=========================

The purpose of the *Game tree visualization* project is to generate visualizations of game trees that can be used to aid analysis. For example, it is possible that the ability to visualize the structure of a game will allow for patterns to be identified that then allow for the game's interestingness (a somewhat intangible quality) to be characterized.

Overview
--------

The visualization process consists of two steps - generation of the game tree data and outputting it in the DOT format, and then using [Graphviz](http://www.graphviz.org) to read the generated file and create an image of the game tree. The generated images contain all relevant data - position values, the children of each position, etc. - necessary for analysis.

Generating visualization files
------------------------------

There are two ways to generate visualization files - through the text-based Gamesman interface, or by using the command line switches '--solve' and '--visualize'.

### Text-based Gamesman interface

Upon starting the text-based game to be visualized, set the various game options and then solve the game. When a solution is found, navigate to the analysis menu by pressing 'A', and then press 'G' to access the visualization menu (shown below).

    e) Toggle (E)dge drawing (currently ON)
    n) Toggle writing text file with (N)ode visualization (currently OFF)
    r) Toggle ordering nodes by (R)emoteness (currently ON)

    v) (V)isualize game graph

Toggling edge drawing selects whether or not edges - moves - are shown in the visualization of the game tree. It is recommended that this option be turned off for games with a large fanout, in order to increase visualization readability, unless it is necessary to see all possible moves.

Writing node visualization to a text file would, theoretically, generate a text file with each valid position and its corresponding text board representation. Unfortunately, due to the current Gamesman architecture, this is impossible (and the option therefore does nothing).

The nodes of the resulting visualization can set to be ordered by remoteness. Turning off this option leaves the vertical position of nodes to Graphviz's discretion; this results in a visualization in which the vertical position of a node usually, but not always, reflects its remoteness. It is recommended that this option be turned on in order to generate accurate visualizations.

### Command line switches

To generate visualization data from the command line, invoke the game executable with the switches '--solve \[ <n> | <all> \]' and '--visualize'. Using this method, it is relatively simple to generate visualization files for some or all variants.

Generating the images
---------------------

The Graphviz tool can be obtained from [<http://www.graphviz.org>](http://www.graphviz.org). Instructions for using Graphviz can be found on the website, and vary depending on the version used. It should be noted, however, that *dot* should be used to generate the images, not *neato* or any of the other graphing tools included with Graphviz.

Unresolved visualization issues
-------------------------------

The original goal of this project was to allow for easy visualization of game trees. Ironically, the large games that would benefit the most from visualization have such dense or large game trees that it is very difficult to effectively study their visualizations. Another problem with such large games is that the number of edges is so high that *dot* dies due to lack of memory.

Fortunately, such large games are almost always loopy, and can thus be broken into several open positions levels. Each level is then visualized separately, allowing for easier visualization (and often making the visualization possible by breaking up the game tree).

Project team
------------

[Alan\_Wu.md](User:Alanwu "wikilink")
