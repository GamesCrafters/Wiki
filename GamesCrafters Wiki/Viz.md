Viz
===

Project Overview
----------------

### Description

The previous status of the Debugger PPM maker is that of which created portable picture map (PPM) files and vectorized PostScript (PS) files. However, that previous implementation did not create the fractal images of the game Tic-Tac-Toe that we wish to have. Furthermore, not only do we want fractal images, we also want the images in a vectorized Scalable Vector Graphics (SVG) format. This will create the basis for the road map that we will eventually take to print vectorized graphical game trees of all games that we currently have and will have.

### Goals

-   Create fractal PPM using using the classical text based tic-tac-toe game.
-   Create fractal SVGs afterwards

### Members

-   Ali Kayes

Project Status
--------------

### To Do

-   I am told that the color red does not render correctly, as a colorblind person, fixing this is nearly impossible for me as I don't have a way to test it.
    -   This applies to the portable picture maps, postscripts, and scalable vector graphics.
-   PPM is nearly perfect, just fix the red and it will render perfectly
-   Postscripts do not render perfectly because there are holes in the game tree. Something must be off in the parsing.
-   SVG do not render perfectly. After my changes, I am not directly creating SVGs, but the code converts PS to SVG. If we fix the postscript rendering, the SVG rendering will be fixed automatically.
    -   Note! It would be better to render the SVG files directly since in will yield greater compatibility with different systems. After my changes, SVGs render in all Unix like systems (Mac, Linux, Unix).

### Done

-   Allow the debugger in mttt.c to work
-   Implement the new spacing algorithm where S(0)=1, S(1)=5, S(n)=3\*S(n-1) + (2/3)\*S(n-1)
-   Lines change thickness as depth goes up
-   Output the graphical game tree as an SVG

