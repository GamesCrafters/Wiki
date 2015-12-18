Connect4 Quit Buttons- GUI changes Spring 2011
==============================================

Process
=======

I read and understood the android code base given to me, while picking up the Android API to implement a few changes regarding game functionality and Connect 4 game play interface.

Code Updated/Final Product
==========================

I've added the following classes:

-   Package com.gamescrafters.Gamesmanmobile:

QuitDialog() : Allow program to quit when pressing either back button or quit button (which I added to the GUI)

-   Package com.gamescrafters.Connect4:
-   Class ColumnTouchListener: handles touching events of the game, including touching, sliding, and clicking. This class has several

methods, each handle an event specifically.

-   New feature added: Changed the code so that the game updates in real-time the current targeted column by displaying a semi-transparent piece on the column as the user slide his finger across the screen. This is done by overwriting previous methods with new and more efficient code.

Future Development
==================

-   It is important to improve the GUI of the game. Game play could be polished further with art and/or animation changes.

