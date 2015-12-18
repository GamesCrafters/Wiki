GamesMan5
=========

Note
----

The current version of VVH was written to be used in conjunction with the Gamesman5 web interface. Some of our code -- as well as the general visual style -- was inspired by the VVH utilized in the Connect4 game on [gamescrafters.berkeley.edu](http://gamescrafters.berkeley.edu), so we would like to extend our thanks for the help in both getting started and figuring out where we wanted to go.

VVH
---

VVH stands for Visual Value History and is essentially a graphical representation of the quality of the moves made by each player and acts as an at the moment depiction of who "should" win, provided perfect play is exhibited by each player.

Tweaks
------

During our final showing of the VVH, there were several comments/suggestions that were made:

-   Make the lines connecting each of the dots thicker.
-   Get rid of the borders on the dots.
-   Make the dots larger.
-   Look into changing the background color to something other than pitch black; pretty sure that you'll have to discuss this with whoever's in charge of keeping up the entire Gamesman5 interface, since the Canvas is black by default.

Bugs
----

-   When the Undo button is pressed, the VVH did not accurately redraw the board devoid of the dots representing the move prior to the Undo action. To correct this, a black rectangle is redrawn over the VVH during each call to the draw function, and the dots are then redrawn over this clean slate. However, even when this action was taken, a single white outline of a dot would appear in the place of one of the dots from the most recent move that was just undone. In order to exact a quick fix, we simply made a call to the draw function twice; however, this is clearly not ideal and deserves some looking into during future updates.

<!-- -->

-   Further, while we were working on VVH, there wasn't an "endgame" notification sent out by Gamesman5, so the final drawing after the endgame isn't accurate, and the grid goes blank. Obviously this is something that ought to be rectified.

