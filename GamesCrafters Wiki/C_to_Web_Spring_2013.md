C\_to\_Web\_Spring\_2013
========================

Server Ported to Python
-----------------------

### Rationale

-   Only requires Python standard library (fewer dependencies).
-   Allows "multithreading."
-   Makes the server more accessible to members (node.js is not know by everyone).
-   Better error handling.

### New Features

-   Processes allowed to live through timeout.
-   Timeout vs. Crash is now reported correctly.
-   Support for per game extensions.
-   Support for query parsing for options / variants.

Added Games
-----------

-   Achi
-   369mm
-   Othello
-   Lgame
-   quickchess

Reusable Parsing Functions
--------------------------

### Hack to Add Games Faster

Some games use the encode a board string with pos=<number> in their board string. This allows the StringToPosition function to search for this key and return it as a POSITION.

### Tiered Games

Tiered game support was added by encoding the tier into the board string. For example, "rkq QKR;turn=2;tier=85" for the quickchess starting position. This value is retrieved in interact.c, and used to set the correct tier before using a board string.
