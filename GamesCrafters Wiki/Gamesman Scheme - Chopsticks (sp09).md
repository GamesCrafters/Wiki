Gamesman Scheme - Chopsticks (sp09)
===================================

What we did - Overview
======================

CS3 was in need of more games for their final project. And so, we designed chopsticks as the game students could code if they wanted at most a B in the class. Considered as the "easy game", Chopsticks uses a board more similar to 1 2 ... 10 than the other games.

How to play
===========

This version of chopsticks is played with n hands and m fingers. Each hand has initially one finger up. Your implementation must be able to handle an arbitrary number of hands and fingers. The default game has three hands, each having five fingers, with one finger up on each hand.

To Move
=======

The example game begins with Figure 1. On the player’s turn, she chooses one of her hands to add the number of fingers to one of the opponent’s hands.

To Win
======

When the player adds enough fingers to exceed the max number of fingers that the hand can hold, then that hand is knocked out of the game. When all hands of a player are knocked out, they lose.

Compulsory Rule Changes
=======================

**Misére Rules:** The player who has all hands knocked out wins. **Wrap-Around Rule:** In this rule, a hand must equal the max number of fingers to be knocked out. Otherwise, the excess number of fingers becomes the new number of fingers on the hand.

Position Representation
=======================

-(P hand\# hand\# hand\# hand\# …) The P represents the player (L or R). Each hand is a number value that shows how many fingers are on that hand.

Future
------

Future versions can add the gui as well as a better way to work the simple graphics so that it doesn't scrunch together when the board is expanded. More compulsory rules can be added as well like hitting your own hand or splitting.
