Quarto Web GUI Writeup Spring 2011
==================================

Overview
--------

=

The goal of this project was to create a GUI for Quarto in HTML 5 Canvas. It was meant to fit on a wide range of page sizes and any browser that supports the Canvas tag (i.e. Chrome, Firefox, and Safari, at least).

### Current State of the Project

The GUI is partly functional at this time. A game can be played: there is no winning position detection, but the player turn is displayed and simple rules have been implemented (e.g. a piece can no longer be selected once it has been played, a player must play the piece from the platform before he can choose the piece for his opponent, a square on the board can only house one piece). Most critical is the absence of value moves and delta remoteness, but also missing are a game menu, CSS that will center the board on the page, and highlighting of board squares that will activate when the cursor hovers over a square on which a piece can be played. The latter is perhaps one of a few aesthetic changes that can be made to the GUI to make it more intuitive and attractive. The time the GUI takes to load in the page needs to be cut down, and that can be achieved by greater compression of the large background image and the individual square images (the wood textures).

All of the changes mentioned above will be made next semester, when the Quarto database will finally be complete and serious work can be done with the value moves and delta remoteness display.
