Tile\_Chess
===========

Rules
-----

Tile Chess is played on an "infinite board". The pieces are exactly the same as regular chess, in which both players have 8 pawns, 2 rooks, 2 bishops, 2 knights, a queen and a king. The game has two phases: Phase 1 is the piece placement stage, in which players take turns putting their pieces down. There can be no "islands", meaning that no pieces may be in isolation from others. Every piece must be adjacent to another piece either by an edge or by a corner. Once both players have placed all of their pieces down, phase 2 begins. Phase 2 plays very much like normal chess, with just a few exceptions. Pawns may move forward and backward. In addition, your own piece may jump over other pieces on your own side. In normal chess, a bishop may not, for example, go over a pawn that is on the same side. Of course, each move that is made must result in a legal board, so no pieces can be left in isolation. For example, in the following board, the Bishop (denoted by "B") may not move anywhere, since doing so would either leave the king on its own team in isolation or the opposing player's king in isolation:

|                                              |
|----------------------------------------------|
|     +---+---+---+---+---+                    
       4 |   |   |   |   |   |                 
         +---+---+---+---+---+                 
       3 |   | K |   |   |   |                 
         +---+---+---+---+---+                 
       2 |   |   | B | k |   |                 
         +---+---+---+---+---+                 
       1 |   |   |   |   |   |                 
         +---+---+---+---+---+                 
           a   b   c   d   e                   
     It is Computer's turn (black/lowercase).  |

These are the most notable differences between Tile Chess and regular chess. The gameplay and strategy, however, is radically different between the two games.

Data Structures
---------------

We keep a "placement" array, which is an array of 1's and 0's. A "1" implies that a piece belongs in that spot, and a "0" implies that there is no piece in that spot. We also keep a "piece" array, which works in conjunction with the placement array to map which piece goes where on the board. For example, in the board above, the piece array would be: "KBk".

Hash
----

As of right now, we only allow 3 pieces to be on the board at an given time. Our hashing/unhashing works as follows: We generate all possible legal boards with 3 pieces, and for each legal board that is generated, a number is assigned to it and kept in a separate array. Thus, one of the arrays is packed very tightly, while the other array is a little bit more sparse, but still not too bad. We also implemented a pieces hash, in which something like "KBk" maps to a number (this had to be hard-coded). In the hash, we keep track of whose turn it is (it's impossible to calculate whose turn it is based on just a given board). We then combine all 3 of these elements (placement hash, pieces hash, and current player's turn) into a single number, and designate such a number to be a valid POSITION.

Project Members
---------------

Alan Roytman

Brian Zimmer
