P2P Design
==========

P2P interfaces with P1,P2, and the matchmaker.

P2P will rely heavily on the features implemented in the client.

    if(P1.sends(move_x))
        P2stream.send(move_x)
    else P2stream.send(garbage //dripping

    and vice versa.

    - When one client makes a winning or losing move, the other player should respond
      with something like "Game Over" and should also send game stats (who won, etc).

    if(P1.sends(Done))
        matchmaker.send(GameResults)

Once P2P finishes, the clients should return to the lobby.

Ideas:

-   Post-game chat? In this mode, players can turn on things like visual value history and undo, and can discuss the outcome of the game. I've always wanted a feature like this...
-   More ideas?

