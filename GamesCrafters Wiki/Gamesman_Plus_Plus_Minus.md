Gamesman\_Plus\_Plus\_Minus
===========================

Gamesman++- is the work I have been doing to port Gamesman+- to C++, with the intent of making it incredibly easy to create new games, hashers, and solvers.

Because an entire port is nearly impossible, the way I am doing this port at the moment is to convert all Gamesman code to C++, leaving utilities (string, hashtable, ArrayList) all in C, which can be replaced by STL classes if the user desires (std::string, std::tr1::unordered\_map, std::list and std::vector).

About
=====

I know that people attempted a [Gamesman++.md](Gamesman_Plus_Plus "wikilink") port a last semester (Spring '08). But I feel that it was overcomplicated, both in its design and in that it did not seem to make game implementation simple.

Now there's also a [Gamesman+-.md](Gamesman_Plus_Minus "wikilink") port. I like several design decisions that Gamesman+- made to generalize Dartboard games. However, some of these break down slightly when dealing with games/puzzles that require custom board types (for example, not square), and it fixes several of the problems that original gamesman has. In fact my main complaint about Gamesman+- is that it tries too hard to be C++, and also depends too much on hashtables for properties that could just as easily be compiled into the code. It makes heavy use of function pointers, which may as well be virtual functions which allow for

There is now a third codebase, [Gamesman\_Java.md](Gamesman_Java.md "wikilink"). I think the hope is that [Gamesman+-.md](Gamesman+-.md "wikilink") will be as compatible as possible with the Java system. However I also realize that it may be trickier than it sounds. Also, I'm not sure about the performance difference, but if GamesmanJava avoids creating a Board object for each move, or if it is JIT compiled, performance while solving may actually be comparable between the two.

SVN
===

The tree is available at <https://gamescrafters.svn.sourceforge.net/svnroot/gamescrafters/branches/Gamesman++->

Viewable online at <http://gamescrafters.svn.sourceforge.net/viewvc/gamescrafters/branches/Gamesman++-/src/>

To check out a repository with TortoiseSVN or Eclipse, this process should be self-explanatory. For command line users (Mac or Linux), run "svn co URL foldername" --if you leave foldername blank it will check it out into the last piece of the URL (Gamesman++- in this case).

Progress
========

The Game structure to be a class with multiple functions that can be overridden. I have altered the game types (in the Core/Types folder) to be virtual subclasses of Game which allow for multiple inheritance. For those not familiar with C++, the idea is that you can extend multiple game types, some of which may implement a few of the required functions.

For example, Rubik's cube extends Game\_Puzzle and Game\_Hashable, because it is a puzzle and implements its own custom hasher. LightsOut extends Game\_Puzzle and Game\_Dartboard, but does not require a special hasher because it is a normal dartboard game.

However, almost everything else in the system (Hasher, Database, Solver, Player, BoardDefinition) is still using C-style classes, so they are able to inherit from parent classes by adding the parent as the first element of the structure.

Porting considerations
======================

Game\* and function pointers
----------------------------

Problem: A couple functions do not have a Game\* argument, so they cannot access options or call other methods inside Game. I'm specifically talking about the couple of functions that are set as function pointers or stored into GamesmanObject.

While it might be possible to put a member function pointer into the GamesmanObject dictionary, casting a function pointer to a void\* is technically disallowed by both the C and C++ standards, so this would require malloc'ing a funciton pointer.

Possible solutions:

1.  Include Game pointer inside of BoardDefinition (perhaps we should do this anyway)
2.  Move Game's GamesmanObject dictionary into BoardDefinition... since the Game itself is never used except to call functions
3.  Merge BoardDefinition into Game (i.e. as part of the base class)
4.  Ensure that Game\* is passed to all functions (this includes Board::toString and Hasher functions)

Game variants?
--------------

I can't find a "correct" way to specify game variants.

Possible solutions:

1.  Make an options dictionary--this can either be part of BoardDefinition as mentioned above, or it can be part of Game's dictionary.
2.  use width/height -- this is probably a bad way to do this.
3.  Create separate subclasses of Game for each option???
4.  Create separate instances of Game for each option, and pass the Game\* into each one. However, this is exponential with respect to the number of options (I will need 16 copies of TCross for only 4 boolean options!)

BoardDefinition
---------------

BoardDefinition is restrictive. What if a given position in a board has more than 255 possible values? True, that game could define its own conversion functions... But why not change it to a plain void\* and leave serialization ("Board\_data\_toString") and displaying ("toString" function pointer inside BoardDefinition) up to the Game class itself?

Although merging it with game is one option, I like some things about the way the current system works--I just feel that it makes too many assumptions about the types of games (think about what made the Python solver so easy to write games for).

Personally, a possible solution for this is to make BoardDefinition as it is written now an implementation of a more generic BoardDefinition class, that is taylored specifically to dartboard games. While this does require the use of virtual functions inside of BoardDefinition (and therefore calling function pointers), I think it is worth the performance hit. Indeed, if performance is critical it may be possible to pinpoint the places where it matters and have them call the correct function directly.

Anyway, BoardDefinition is not going to fundamentally change any time soon because so much code depends on things being the way they are, and I don't yet have a specific reason that it needs to be changed--games are still able to define custom board definitions, just they have to worry about structuring it into a byte array rather than a type of their own choosing.

Alternatively, BoardDefiinition could cooperate with Game--but that should not break existing code.

Hasher vs. Game
---------------

Problem: Hasher as a separate class makes sense for certain Game types, but not for every game.

It makes sense to allow multiple hashers per game, but perhaps this is acceptable as a compile-time constant. The way I would implement multiple hashers per game is to make the game itself be an abstract base class, leaving the hash(), unhash() and maxHash() functions undefined. Then you can subclass the game for whatever types of hasher you want.

In this way, it may also make sense to define hashers as parents using multiple inheritance -- that is, if you are defining a Dartboard game, and you want to use the generic hash with it, you could make your game extend both dartboard game as well as generic hash.

However, this is an unnecessary change for the most part, so right now there is a wrapper Hasher class that handles the interactions between Hasher and Game, so you can either implement a separate hasher, or implement the functions in the Game class directly.

Helping
=======

I'm sorry that I haven't let anyone know about this project--it's something I came up with last weekend (Feb 14) and it's still in a very experimental state, especially with respect to if it will help simplify the Gamesman+- system and the ease of creating games. It should work just as well as normal Gamesman+-, and indeed most of the code, except for the new games, could be trivially ported back to standard C. However, I likely missed some things in the porting process.

I would love if people could dive into the code (if they so please) and try to implement games or things... but I know that it's a bit tricky to get used to Gamesman+- style. Still I would like to know what sorts of things trip you up so they can be better documented and fixed (code is supposed to be easy to read, just like the sense of awe and beauty you get while looking at Python code).

Please email me at patrick.horn@gmail.com with any suggestions. Perhaps there should be a mailing list for Gamesman+-
