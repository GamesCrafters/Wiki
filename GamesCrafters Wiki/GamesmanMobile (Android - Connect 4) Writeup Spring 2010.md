GamesmanMobile (Android - Connect 4) Writeup Spring 2010
========================================================

The Project and Its Members
---------------------------

Google Android GamesmanMobile Application

- Alex Degtiar - Gayane Vardoyan - Royce Cheng-Yue

### Goals

Our goals this semester included making the GamesmanMobile application independent of the current games. Currently, our Connect 4 is somewhat closely related to certain methods (such as undo / redo and game methods). However, these methods should be general and accessible from other games. As a result, one of the main goals is to have a main GameActivity class that provides general methods to make web calls, a framework for specific games to use, and features that could be used across all games. In terms of features, we are providing perfect computers for users to play against. To further comment on this feature, we are hoping to provide a time delay between each of the computer moves to ensure that the game progresses at a reasonable rate (this feature is especially useful in computer vs. computer). As a result, we have human vs. human, computer vs. human, human vs. computer, and computer vs. computer as our options for each game. We are also implementing an undo/redo feature for all games. In this way, users can choose different paths in a course of a game. This undo and redo feature also leaks into the VVH, providing a basis to change the game "live".

### Members and Responsibilities

All of the members concentrated on individual parts in the application. Whenever we needed help, we asked each other for help.

Here is the breakdown:

Alex worked on creating an abstract GameActivity library class that essentially controls the entire application. When a game requires a general function, it will call upon this GameActivity class. In this way, the methods for making each game is independent of the specific game. Features that we implement will also be accessible across all games.

Gayane worked on providing perfect computers to the games. She worked on computer vs. human AI and she is currently working on computer vs. computer AI. Computer vs. human AI is currently working and computer vs. computer is currently in progress. For the computer vs. computer part, she is planning to implement a time delay to reasonably see each individual move (in a computer vs. computer setting, the board will instantaneously be filled).

Royce worked on the undo / redo features of the Connect 4 game. Although it is currently only working for Connect 4, he will try to make it part of the library so that each game can add in the undo / redo feature. This undo / redo feature is added on the bottom menu of the Connect 4 game. To make it easier for the user, he implemented a slider that quickly jumps to a specific move based on the relative level within the slider and a forward and backward button for marginal move changes.

Apart from our individual responsibilities, we helped other Android groups when they required help. We also helped them understand our code to call our methods (such as the move value methods).

General Code Structure
----------------------

### GameActivity

This abstract class is the overarching class in our application. It contains general game methods and additional features that we provide. By providing a general abstract class, an individual game is able to extend GameActivity and access these general methods and features.

### GUIGameBoard

This class abstracts out the GUI features of the game board. Originally, our GUI elements were incorporated inside the game. Now, the GUIGameBoard offers an extraction of these elements to make the actual game independent of the GUI.

### HorizontalSlider

This class provides the essence of the undo/redo horizontal slider in a specific game. In essence, this is an extension of the progress bar and provides the feature that a relative move number corresponds to the relative location of the progress bar.

### MoveValue

This class generalizes the methods required to access move values from the GamesCrafters server. Each game would call upon methods from MoveValue to receive responses from the server.

Final Product
-------------

For our final product, we have a working Google Android GamesmanMobile application. The application provides dynamic board size changes, perfect computer opponents, and an undo and redo buttons and slider. Another group (Angie/Jennifer) are implementing a VVH into the final product. Hopefully, we are able to integrate the other games (Connections/Y) into the main application soon.

Ideas for Future Development
----------------------------

### Future goals

- Integrating all the games into the main application - Cleaning up code - Generalize specific game methods (more abstraction from individual game)

Documentation by Royce
