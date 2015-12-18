C Game Wrapper and Gamesman Plus Plus UI
========================================

People
------

1.  Haley Nguyen
2.  Alan Roytman

Problems
--------

1.  Create an user interface, which should look identical to Gamesman's UI, for playing games in Gamesman++.
2.  Do whatever that need to be done to make Gamesman++'s modules (ConsoleShell, solvers, etc.) to work with C games with a minimal amount of changes to C games.

Background understanding
------------------------

1.  *ISolvableGame and IPlayableGame:* These are abstract classes that a game module in Gamesman++ must inherit. The reason for the creation of two distinct abstract game classes (neither inherits the other) is unclear. However, the way we (Alan and I) have understood and organized the declaration of abstract methods is as follow: a playable game is a game a user can interact with, therefore, methods that are needed to interact with the console (ConsoleShell) to print the user interface of the game will be declare in IPlayableGame.h as abstract methods. Similarly, ISolvableGame would contain methods that are needed to solve the game.
2.  *GamesmanRuntime and ConsoleShell:* To run a game, first, we need to create a GamesmanRuntime object, add a DB object to it (DB here is a general name for database object), add a game and a solver to it, and run `go()` (check ConsoleShellMain.cpp for more details). This action will fill dependencies between these modules such that when the solver solves the game sometime and somewhere later, the game's solution will be saved to the database. NOTE: `StandardSolver`'s `solve()` will segfault if the dependencies between the solver, the game, and the database are not filled first. Then, the db, the game, and the solver are passed to a ConsoleShell object, and the user interface is created by calling ConsoleShell's Menus(binaryFileName). `Menus(binaryFileName)` will print out the menu, and game specific menu is there is one. Then, it will parse menu choice and calling the appropriate function when a choice is given.
3.  *Compiler support features:* Gamesman++ has its own compiler support features (somewhere) to make sure certain variables and types are initialized and used correctly. Therefore, abstract (virtual) methods must be initialized to 0 where they are declared, otherwise the compiler (or the support features more likely) will give an error message.

Solution
--------

Following is the list of things we created or modified

1.  *cgame.h and cgame.cpp:* located in the framework folder, these files are the wrapper for C games. The class `cgame` provides methods to query authors' names, text strings and variables needed for for user interface and solver modules. Methods in `cgame` are named similarly but not identical to their C game's counterparts.
2.  *Positions, moves and hashers:* `cgame` uses classes from IntegerGameTools.h for position, moves, and hashers. Please check cgame.cpp and cgame.h for more details. In Gamesman++, each game can potentially have its custom Position, Move and Hasher class. However, these classes will need to inherit IPosition, IMove, and IHasher respectively. These abstract classes serve as an interface for the "real" class with the ConsoleShell. How a move or a position is printed is game-specific and not the move or the position object-specific. The design decision is so that multiple game classes can use the same move class or position class such as IntegerMove or IntegerPosition, but also print the move or position differently.
3.  *Printing moves and reading moves*: Both tasks are accomplished with the help of the function `moveToString(move)`. For printing a move, the move is passed to the function, and a string is returned. For reading user's text input and converting it to move, the text input is compared against the string form of all available moves at the user's current position. If a match is found, the move is used, otherwise, an error message will be announced to the user. With this mechanism, the function `ValidTextInput` in the C games is not needed anymore. In addition, the functions `GetAndPrintPlayersMove(position, move, playerName)`, `PrintMove(move)` and `PrintComputersMove(move, name)` are also not needed.
4.  *Initializing hasher:* cgame's hasher is initialized with the maximum position value which is one less than `gNumberOfPositions`.
5.  *ConsoleShell.cpp and ConsoleShell.h:* this object takes in a solver object, a game object, and a database object whose dependencies have been filled by a GamesmanRuntime object. Most of ConsoleShell's methods that print anything to screen are copied from textui.c of the Gamesman project. Most of those codes are still commented out due to the lack of different database objects, solvers, and other modules. Most of these methods have the same name as their counterparts in Gamesman. One exception is `HitReturnToContinue()` because I felt that the name `HitAnyKeyToContinue()` did not correctly describe the method. The function `BadElse()` is turned into an exception in Gamesman++.
6.  *Player*: This class holds player name, player type (HUMAN or COMPUTER), and whether the player starts first or second.

Result
------

Self-evaluation
---------------

A ( we worked too hard :) )

Lessons learned
---------------

1.  When writing code, don't use special words such as "this", "xor", "bool", "false", "true" even if it is allowed in the programming language you are coding because your code may break the build when it is compiled with codes from another language.
2.  Avoid redefining something that is already defined because this tends to break the build when the code is ported. It is very difficult to find the trick that would make the ported code built in the first place. For example, in mcmass:

`typedef unsigned char bool;`
`#define false FALSE`
`#define true TRUE`

  
Note that, in Gamesman, where this code is found, there is already a type BOOLEAN which is a typedef of unsigned char or a typedef of int depending on the OS. Type BOOLEAN has two values which is TRUE and FALSE. The above code basically defined the type BOOLEAN again with a different name, and has no sensitivity to different OSes. Consequently, when this code is compiled with C++ code of Gamesman++, the compiler gives error because of the redefinition of C++ keyword which are bool, false, and true. In addition, it also complains about the use of unsigned char in the typedef. When these lines of code are removed, and bool is refracted to BOOLEAN, true to TRUE, and false to FALSE, the compiler stops complaining.

<!-- -->

  
Another example of the badness of redefining type would be (this is also from mcmass):

`typedef int Player;`

  
In Gamesman, there is already a struct that is typedef to Player. This Player struct is also ported to the new code for other games to work. mcmass redefines Player while it also includes the code that declares Player that is a struct. It is still unclear how mcmass was able to build in the first place, but since all C games are treated as a generic class in Gamesman++, the build breaks when we tried to compile mcmass. The best way to fix is to refractor the type Player in mcmass.c to something else. While refractoring identifiers is not hard, it is time consuming and tedious. Moreover, fixing code does not really relate to porting code, and having to investigate and fix to remove 20+ lines of error messages per game while trying out some relatively unrelated feature is frustrating and can reduce a programmer's efficiency.

1.  Comment, especially in places where things are out of the norm. This help code readers understand the code better, and can potentially reduce future bugs when the code readers also try to add code to the project. For example, in some games, `gNumberOfPositions` is initialized where it is declared and is never changed. Someone who happens to read several games' code, where this variable is initialized in such a place and never changed can assume that all games would follow the same style. This erroneous assumption, in fact, has introduced a bug cgame.cpp (in Gamesman++). However, this bug was quickly caught because some game's author had written next to where `gNumberOfPositions` is initialized that it would be changed later. This alert the new coder, and the bug was fixed before it causes any major problem.

<!-- -->

1.  When writing a wrapper of games, try it only as many games as you can because an error of wrapper can cause some games to break the build while other games don't. This lesson can also generalize to other practices.

