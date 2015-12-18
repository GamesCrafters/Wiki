Visual\_Value\_History\_for\_GUI
================================

Visual Value History

Current Problems
----------------

1.  how to find max remoteness (including max tie remoteness)
2.  managing scrolling after a long game (it would take a very long game, but we have to assume it will happen)
3.  decide on a "look and feel" (pieces? colors?)
4.  what should bottom buttons be? need new words, to win/to move is to long. what about for "visual value history", also to long.

Desired Additional Features
---------------------------

1.  click on a move to go back to that point in the game
    1.  we would want to add a description explaining this feature near the title at the top of the sidebar
    2.  simple way is to call Undo X number of times
    3.  what if someone accidentlaly clicks "undo 20", we should have some way to "Redo" so they won't have lost their current game state. this would probably be harder to do though. one way would be to keep track of a list of past moves, and when someone goes back to an earlier game state, don't cut the list until they make another move. where would we put this "Redo button". maybe at the top of the history graph? maybe right below the last piece on the graph?

2.  
