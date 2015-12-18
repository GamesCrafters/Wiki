P2P Module Documentation
========================

The P2P Module accepts three types of requests: moves, end-of-game notifications, and resignation notifications. It sends (respectively) moves, end-of-game acknowledgments, and resignation acknowledgments. In all cases, information is stored exclusively in the headers, and the binary contents of the requests and responses are not used. All requests and responses transmitted must have headers for the source and destination player of the request/response. These are specified in the first table below, although they apply to all requests.

Registration
------------

Before the module will pass moves between two players, a game must exist between the two. The registration module must call the (static) method P2PModule.registerNewGame(p1, p2), where p1 goes first and p2 goes second.

Moves
-----

Clients send moves (i.e. incoming requests) with the following format: Each field name/value is followed by the constant String in gamesman.server.p2p.Const that refers to it.

    Header field             | Header value
    ------------------------ | -----------------
    type                     | SendMove
    Const.TYPE               | Const.SEND_MOVE
    ------------------------ | -----------------
    Move                     | <value of the move as in gamesman>
    Const.MOVE_VALUE         |
    ------------------------ | -----------------
    SrcPlayer                | <player the request originated from>
    Const.SOURCE_PLAYER      | 
    ------------------------ | -----------------
    DestPlayer               | <player the request is headed to>
    Const.DESTINATION_PLAYER |
    ------------------------ | -----------------

The module relays this same message to the destination player.

Game ending protocol
--------------------

When the game ends, the player *after* the finishing player sends a command to the server saying that the game has ended. This request is as follows:

    Header field             | Header value
    ------------------------ | -----------------
    type                     | GameOver
    Const.TYPE               | Const.END_OF_GAME
    ------------------------ | -----------------
    SrcPlayer                | <player the request originated from>
    Const.SOURCE_PLAYER      | 
    ------------------------ | -----------------
    DestPlayer               | <player the request is headed to>
    Const.DESTINATION_PLAYER |
    ------------------------ | -----------------

The other player (that is, the one who made the finishing move) receives a request as follows:

    Header field             | Header value
    ------------------------ | -----------------
    type                     | SendMove
    Const.TYPE               | Const.SEND_MOVE
    ------------------------ | -----------------
    Move                     | null
    Const.MOVE_VALUE         |
    ------------------------ | -----------------
    SrcPlayer                | <player the request originated from>
    Const.SOURCE_PLAYER      | 
    ------------------------ | -----------------
    DestPlayer               | <player the request is headed to>
    Const.DESTINATION_PLAYER |
    ------------------------ | -----------------

Since the player who sent the end-of-game signal must receive a response, the client will receive an acknowledgement from the server that the end of the game completed successfully.

    Header field             | Header value
    ------------------------ | -----------------
    type                     | Ack end
    Const.TYPE               | Const.ACKNOWLEDGE_END
    ------------------------ | -----------------
    SrcPlayer                | <player the request originated from>
    Const.SOURCE_PLAYER      | 
    ------------------------ | -----------------
    DestPlayer               | <player the request is headed to>
    Const.DESTINATION_PLAYER |
    ------------------------ | -----------------

Once all three have gone through the server, the game between the players is unregistered.

Resignation
-----------

The player who resigns sends a resignation request as follows:

    Header field             | Header value
    ------------------------ | -----------------
    type                     | Resign
    Const.TYPE               | Const.SEND_RESIGNATION
    ------------------------ | -----------------
    SrcPlayer                | <player the request originated from>
    Const.SOURCE_PLAYER      | 
    ------------------------ | -----------------
    DestPlayer               | <player the request is headed to>
    Const.DESTINATION_PLAYER |
    ------------------------ | -----------------

The response sent to the other player is of the exact same format.

The response to the player who resigned is as follows:

    Header field             | Header value
    ------------------------ | -----------------
    type                     | Ack resign
    Const.TYPE               | Const.ACKNOWLEDGE_RESIGNATION
    ------------------------ | -----------------
    SrcPlayer                | <player the request originated from>
    Const.SOURCE_PLAYER      | 
    ------------------------ | -----------------
    DestPlayer               | <player the request is headed to>
    Const.DESTINATION_PLAYER |
    ------------------------ | -----------------

Once all three have gone through the server, the game between the players is unregistered.

Errors and warnings
-------------------

To turn on warnings, set the PRINT\_WARNINGS flag in server.p2p.Const to true.

-   The module throws exceptions when a client attempts to send moves for an unregistered game.
-   If a game has not been properly initialized (the second player must send a null request before gameplay can begin), the module will ignore all requests until it receives an initialization request. It will issue a warning each time this occurs.
-   If a game has already been initialized and an initialization request is sent, the module will ignore it and issue a warning.
-   If the player whose turn it isn't attempts to make a move, a warning is issued and the request is ignored.

Testing
-------

A set of sample games can be found in server.p2p.P2PTester.java. This contains 3 games that run simultaneously.
