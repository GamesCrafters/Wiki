GCWeb API Documentation
=======================

This page serves to document all of the GCWeb API calls that are currently available.

RESTful API
-----------

GCWeb uses a RESTful API to query the various backends (GamesmanClassic, GamesmanJava) for solved game data.

All API requests have a common base URI: <font size="+1">

    http://nyc.cs.berkeley.edu:8080/gcweb/service/gamesman/puzzles/

</font>

There are two API requests that can be made for each game.

#### Position Value

<font size="+1">

    http://nyc.cs.berkeley.edu:8080/gcweb/service/gamesman/puzzles/<GAME_NAME>/getMoveValue;<GAME_PARAMETERS>;board=<BOARD>

</font>

#### Move Values

<font size="+1">

    http://nyc.cs.berkeley.edu:8080/gcweb/service/gamesman/puzzles/<GAME_NAME>/getNextMoveValues;<GAME_PARAMETERS>;board=<BOARD>

</font>

<font size="+1">`GAME_NAME`</font> is a unique identifier for each game that indicates which game's data is being requested (see below for specific values).

<font size="+1">`GAME_PARAMETERS`</font> is a (potentially empty) set of semicolon-separated key-value pairs for games that have multiple variations, used to specify which variation of the game is being queried (typically these values are width/height and the like). Again, see below for the values each game supports.
