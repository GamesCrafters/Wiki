GamesmanWeb\_-\_Connect\_Four\_SP09
===================================

What I did - Overview
=====================

I designed a new Web framework that allows front-end developers to write UIs with almost no knowledge of the back-end Gamesman engine. Overall, this is one key component that enables Gamesman to move to the Web.

I also implemented a Connect Four client, which aims to be professional-looking and representative of how good the games can look.

Motivation
==========

The Web framework from Fall '08 had laid the groundwork for puzzles, but it suffers from poor modularity and critical race conditions. For example, the Visual Value History widget is a first-class citizen of the framework even though it should be separate - both logically and graphically - from the game and the framework. There is also a concurrency bug in which the framework only remembers the most recent server request; the response to an old request may be mistakenly construed as the response to a newer one. Consider the scenario below:

1.  User makes a move and board state changes to *BoardA*:
    1.  Framework issues a request *ReqA* for the next moves (i.e. all moves that can be performed if the current state is *BoardA*)
    2.  Framework sets *ReqA* as the currently pending request.

2.  User makes another move and board state changes to *BoardB*:
    1.  Similarly, the framework issues a request *ReqB* for the next moves after *BoardB*.
    2.  Framework sets *ReqB* as the currently pending request.

3.  The response *RespA* finally comes back from the server, in response to *ReqA*.
4.  Framework sees *RespA* as the response to *ReqB*, which was remembered as the most recent request.
5.  Now the board state is *ReqB*, but the list of next possible moves is incorrect and the game is now in an inconsistent state.

The new Web framework was written from scratch with inspiration from the former version. The old concurrency bug has been fixed and a more modular approach should allow for plug-ins (e.g. Visual Value History).

Client Web Framework
====================

The client-side JavaScript Web framework is targeted towards front-end developers. The framework abstracts the client-server interface, and leaves only the UI display and event-handling to the front-end programmer, who must specify four things:

-   The HTML/CSS for the game UI
-   Appropriate event handlers to respond to user interactions
    -   Such handlers would e.g. move pieces or call *doMove()*
-   Specify a handler for visualizing an executing move (technically optional)
    -   After the framework receives a *doMove()* invocation and checks the validity of the move in question, it notifies all subscribers to the *executingmove* event. A typical subscriber may be an animation function, which renders the current move.
-   Specify a handler for switching turns.
    -   The framework triggers a *nextvaluesreceived* event whenever it receives a valid response from the server. Most games (but not all e.g. Nine Men's Morris) will choose to switch the currently active team.
    -   This arguably should be handled at the framework level. Currently, the server does not explicitly include the current player as part of the board state, though.

The UI programmer may optionally provide functions to show, hide, and update the value move coloring on the game board.

Future
------

Functions to undo moves or jump to arbitrary board states have not been considered, but these will be needed for the Visual Value History. Also, a separate JavaScript file with utility functions (e.g. playing sound) may be worth creating.

Connect Four
============

I implemented a Connect Four interface, both to determine the requirements for the framework and to have a polished game on the Web. It animates the sliding pieces to provide the look and feel of a real Connect Four board.

Future
------

It would be great to add sound effects when pieces are dropped.
