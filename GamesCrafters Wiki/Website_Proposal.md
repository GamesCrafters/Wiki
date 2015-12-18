Website\_Proposal
=================

Our long term goal is to be able to phase out Tcl/Tk as the presentation layer and instead move to Javascript/AJAX. This will allow for richer games (alpha blending) and the ability to work on nearly every computer. We will be targeting Webkit (Safari rendering engine) and eventually integrate Webkit into Gamesman itself. The benefit of this is that theoretically, we will be writing the game just once, and the games will be able to run on any modern browser.

Backend
-------

We will need to create a REST interface to interact with the C backend. Given a board position, we will return a list of the move values in XML or JSON format for easy parsing and maximum flexibility in case we decide to switch our presentation layer away from Javascript.

Frontend
--------

We will use (X)HTML, CSS, Javascript, and AJAX to create our games. Game logic will reside in the javascript files. However, if there is no server connection, the player will not be able to determine the move values.
