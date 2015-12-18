A\_General\_GUI\_for\_basic\_games\_using\_only\_C\_function\_calls\_-\_Joey\_Corless,\_2-27-2006
=================================================================================================

Keaton's current project (if I understand correctly) is to create a powerful, generalized GUI system so that a GUI does not need to be hard-programmed in Tcl for each game, but rather it is converted to a sort of "bytecode" that can then be interpreted by one or more overall GUI systems.

I propose a less ambitious project, which would be more easily implemented but less applicable to complex games. The driving idea is that if a GUI knows the shape of a board, the size of a board, the number of pieces, and how a board is represented, it can display the game graphically using only calls to the already-written C module.

To display pieces, the system would need to be given a standard representation of a board from each module (alternately, for complex games, instead of a predefined "standard" representation, there could be several available boards (e.g. rectangular, hexagonal), or even a standard language for describing a board (e.g. a string of characters, where each '\_' meant a place on the baord and each '|' meant a new row). It could then easily display a blank board and iterate through the board, displaying the pieces.

To display moves, the system would need to be given a list of moves (in their hashed form). For each move, the system would ask the game module for the result of making that move, and would then perform basic pattern recognition to determine what the type of move was made. (E.g. if an X disappeared from one location and an X appeared in another, treat it as a slide; if an X appeared with no corresponding disappearance, it was dropped onto the board; if an X disappeared with no corresponding appearance, it was captured.) The move could then be converted into a standardized form (a piece of data with three fields: the type of move, the piece, and the location).

Once all of the moves are in memory in this standard form, it would simply be a matter of displaying the corresponding arrows/dots. If show value is turned on, the colors for these could be resolved by a C call.

When the player selects a move, the system can animate it using the standardized form (all slide animations can move the piece across the screen, captures can make it fly off the screen, etc.). It then tells the module to make the move (passing it the hashed form, of course), and repeats the process.

There are many more details that need to be worked out, but here's a basic rundown of the advantages/disadvantages of this system over the current one.

Advantages: No need for a separate graphics module for each game, the C code will suffice. Standardized graphics (arrows, animations, etc.) Changes to the GUI system (new animations, options, etc.) only need to be made in one place Immediate graphical satisfaction for newgamers (You finish your game and you immediately see it in graphical action and not just text, to me that'd be pretty cool) Possible addition of many older text games into the graphical system Faster development of games (no lag time between the mechanics being done and the game being added to the graphical system)

Disadvantages: Some procedures (getBoard, getHeight, getWidth) will have to be added to C modules Complex games can't be easily handled Not much room for creativity with the graphics on the part of individual game designers

As to whether it can be implemented effectively? I don't know enough about Tcl/Tk and the interaction between Tcl and C to say. I wrote a very basic prototype in Python (using the wxPython and PyGame libraries for menus and graphics respectively) which works, but I can't interface it with an actual C module yet, only with python modules intended to mimic the interface with a C module. Someone else will have to speak more on this point.Can it be generalized to include more complicated games? I think so. To some extent, once the system is in place, generalization would be trivial (more patterns by which to recognize moves, for example), but more complicated generalizations would be more tough. Arbitrarily-shaped boards, for example, could be implemented with some sort of standard board description format, but these more complex ideas fall more along the lines of Keaton's proposal.

Is it even worthwhile to do? Maybe, maybe not. In the short run, I think if it could be made to work it would be definitely worth it. If nothing else, it would allow us to get older C games with no Tcl modules into the GUI easier. In the long run, I don't know if it'd be worth going this route instead of the more general route of creating a game description format that GUI systems can interpret, except maybe for relatively simple games.

There are a LOT of questions I haven't asked or don't have answers to, and there are a lot of details that still need to be discussed.

If you'd like to see the prototype I wrote in python, you can download it (and the sample games) here:

<http://members.lycos.co.uk/joeycorless/protogui.html>

Unfortunately, the code is really hacked together and pretty ugly, and there's still a few bugs, but it'll give you the basic idea of what I mean. Any comments on whether the idea has any merit, if it's already been tried, etc. would be very appreciated.
