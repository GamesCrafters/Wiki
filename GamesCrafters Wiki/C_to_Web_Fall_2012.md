C\_to\_Web\_Fall\_2012
======================

Two attempts were made to connect GamesmanClassic to the web.
-------------------------------------------------------------

Result: There is now a server serving some of the games at nyc.cs.berkeley.edu:8081.

Attempt One: Export
-------------------

Originally, the design was to implement a new export format in GamesmanClassic, then add a backend to GamesmanJava to read that export format.

### The export format is as follows:

-   A header of 64 bit, little endian integer values:
    -   The number of bytes in the remoteness field
    -   The number of bytes in the mex value field
    -   The number of bytes in the hash field
    -   The number of moves in each 'line'
-   A series of 'lines', each of which is the same size, containing:
    -   A byte recording win, lose, tie, or undecided as a character ('W', 'L', 'T', 'U').
    -   Remoteness, a little endian integer of the size indicated in the header.
    -   Mex value, a little endian integer of the size indicated in the header
    -   An array of moves with a number of entries equal to the number of moves entry in the header
        -   Each of which is a hash (a little endian integer of size indicated in the header).

The export functionality is located in export.c, and can be accessed from the analysis menu as well as the commandline option --export. The code is based on the ascii print function in analysis.c. Unfortunately, the team found that there was no suitable interface in GamesmanJava to extend to add the desired functionality, so a new Java server called GamesmanLightServer was implemented. A serious limitation was that board strings weren't extracted from GamesmanClassic, and new functions to unhash the board positions would have to be written either in the GamesmanLightServer or in the frontend. Another limitation is that it requires the use of a non-tier solver. Near the end of that implementation, the idea to write spawn GamesmanClassic as a subprocess and interact with it through pipes was proposed.

Attempt Two: Subprocesses
-------------------------

A small experimental implementation was written in Ruby, which made clear that the final implementation would need to focus on asynchronous communication with subprocesses. Since node.js provides an asynchronous interface for subprocess interaction, as well as mature http and json support, it was chosen for the real implementation.

### An interaction shell was added to GamesmanClassic.

### Capabilities

-   Query for various fields in the game.
-   Generate json responses corresponding to the web API (although it doesn't parse the request URL's).

Its implementation is located in interact.c, and can be accessed using the command line option --interact. It uses =&gt;&gt; as its prompt, has a line limitation of 511 characters, and does error checking (including shutting down correctly if it's input or pipe breaks). However, the c process will return incorrect results (or crash) if started using a tier solver. An important detail is that it flushes its output on newlines, which makes interacting with it through pipes easy. Note that the interaction shell is entirely text based, there is no binary interaction.

### Commands

#### The following commands take no arguments:

-   shutdown: Stops the process.
-   exit: Stops the process.
-   quit: Stops the process.
-   start: returns the hash of the starting position as a base-10 unsigned integer

#### The following commands take a position/hash encoded as a base-10 unsigned integer (denoted by <pos>):

-   value <pos>: takes a position and returns the value letter ('W', 'L', 'T', or 'U') of that position.
-   choices <pos>: takes a position and returns a json-format list of integers of the positions resulting from moves.
-   moves <pos>: takes a position and returns a json-format list of moves encoded as position. Guaranteed to be in the same order of the result of the choices command.
-   named\_moves <pos>: takes a position and returns a json formated list of strings representing the moves. Requires MoveToString to be implemented. Guaranteed to be in the same order as the result of the choices command.
-   board <pos>: takes a position and returns a board string if PositionToString is implemented, otherwise returns not implemented.
-   remoteness <pos>: returns the remoteness of a position.
-   mex <pos>: returns the mex value of a position, or not implemented if there is no mex value for this game.

#### The following commands take other argument sequences:

-   result <pos> <move>: takes a position and a move in the format returned by the moves command, and returns the resulting position from performing the move.
-   move\_value\_response <board string>: takes a board string, and returns a json-response as per the GCWeb API (getMoveValue), if the game is properly implemented. If the game is not properly implemented, may return junk data (or crash).
-   next\_move\_values\_response <board string>: takes a board string, and returns a json-response as per the GCWeb API (getNextMoveValues), if the game is properly implemented. If the game is not properly implemented, may return junk data (or crash).

### The interaction shell has some error handling:

-   There should be no buffer-overflows or similar errors in the interaction shell itself.
-   The input size of a line is limited to 511 characters.
-   Lines which are too long, commands called with the wrong number of arguments, and unknown commands will all result in a response of the form error =&gt;&gt; <msg>

### A node.js server was created which starts the subprocesses.

Processes are started using --interact --notiers. This should always result in correct behavior.

#### The server can either:

-   Start all games in the GamesmanClassic bin directory (must start with the letter m).
-   Start all games listed in the response to a url (currently not tested, but likely to be correct).
-   Start up games when it recieves a request for them (the current default).

The server can forward requests for game matching a list to the GamesmanJava. (tested, but currently disabled)

#### Limitations:

-   The forwarding works by making an http request over the internet.
-   The games are hard coded in a global.

The server does all of its work asynchronously, pushing requests onto queues which are then processes by the subprocesses. Preliminary work for supporting multiple subprocesses per game, and starting and stopping processes based on resource requirements has been done, but the server currently makes not use of this. The server currently records if a subprocess has shut down incorrectly, the refuses to start the process the game again if it does. The server currently ensures that it always sends out a valid JSON response (even if it proxies to the GamesmanJava server).

### MoveToString, StringToPosition, and PositionToString were implemented for some games.

A generic implementation of StringToPosition and PositionToString was implemented in mlib.h

#### Working games:

-   1210
-   1ton
-   baghchal
-   rubik
-   sim
-   swans
-   ttt

#### Not working games:

-   369mm
-   3spot
-   Lgame (some progress)
-   abalone
-   achi
-   ago
-   asalto
-   ataxx
-   blocking
-   cambio
-   change
-   cmass
-   con
-   ctoi
-   dao
-   dinododgem (some progress)
-   dnb
-   dodgem
-   fandan
-   foxes
-   gobblet
-   graph
-   hex
-   horse
-   hshogi
-   iceblocks
-   igo
-   joust
-   kono (can this game even be solved?)
-   lewth
-   lite3
-   loa
-   mancala
-   nim
-   nuttt
-   ooe
-   othello (mostly implemented)
-   pylos
-   qland
-   quarto
-   quickchess
-   qx
-   rInfin2
-   rcheckers
-   rubix
-   seega
-   slideN
-   snake
-   squaredance
-   stt (everything appears to be implemented, but there's some bug)
-   tactix
-   tilechess
-   tootnotto
-   tore
-   ttc
-   tttier
-   win4
-   winkers
-   wuzhi
-   xigua

### Current limitations:

-   Not all game have MoveToString, StringToPosition, and PositionToString implemented or need the tier solver.
-   Cannot query tier solver
-   Currently no support for variants / options (although preliminary support for multiple subprocesses per game has been done).

