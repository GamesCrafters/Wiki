Quick\_Chess
============

QUICKCHESS:

Adam A, Aaron L.

Rules:

Game Board Configuration: 1) The size of the board is 5x6 and does not change 2) The initial board looks like this:

------------------------------------------------------------------------

|R |B |K |Q |N |

------------------------------------------------------------------------

|P |P |P |P |P |

------------------------------------------------------------------------

| | | | | |

------------------------------------------------------------------------

| | | | | |

------------------------------------------------------------------------

|p |p |p |p |p |

------------------------------------------------------------------------

|r |b |k |q |n |

------------------------------------------------------------------------

Piece Key/Movement Capabilities: R = Black Rook, r = White Rook =&gt; Rooks can move Forward, Backward, Right or Left

`                       any number of squares.`

B = Black Bishop, b = White Bishop =&gt; Bishops can move diagonally in any direction K = Black King, k = White King =&gt; Kings can move in any direction but only one square Q = Black Queen, q = White Queen =&gt; Queens can choose the path of a bishop or rook, ie

`                       straight or diagonally any number of squares                            `

N = Black Knight, n = White Knight =&gt; The knight has a fixed number of steps per move

`                       and can only capture a piece on its 3rd step(last).`
`                       It jumps in an L shape two forward/back/sideways `
`                       then one to the left or right. It always ends its move `
`                       on a different color square.`

P = Black Pawn, p = White Pawn =&gt; Pawns have two types of movement, normal movement and capture movement. In normal movement the pawn can move forward one square on any given turn. In capture movement an opponents piece must be diagonally one space forward from your pawn. If this is the case the pawn can move diagonally forward one square to capture the opponents piece. Also if a pawn reaches the end of the board, it can transform itself into any of your already captured pieces.

Object of the Game:

`   The object of Quick Chess much like real chess is to capture your opponents King. Once this is done the game is over and the person who captured the King wins.   `

Data Structures:

`   The chess board will be maintained as a double array of characters using the mapping above.  We will use the general hash to key the board.  A move for a given board will be a pair of points on the board.`
