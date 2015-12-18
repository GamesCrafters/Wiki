Sliding Game Interface
======================

**Project Overview:**

**Goal:** Over the course of the semester we set out to learn the fundamentals of JavaScript and Canvas using online tutorials and through building a SlidyInterface. This interface was to be used in games in which pieces slide across the board, as opposed to being dropped on a place. The game would feed the function valid moves of the piece clicked and the player can select an arrow pointing to a valid move. Once selected, the piece would slide across the screen to the selected move.

**Members:** Madeeha Ghori Jason Duval

**Code Overview:** Version 1.0 of the code is very simple. The idea was to make a very light interface that requires very little knowledge of the specific game and its rules. Therefore, there are only a few functions present:

  
1) drawValidMoves: this is the only function actually called by the game.

  
a. ctx: the canvas your game is drawn on. This is where the arrows, etc. will be drawn as

well.

  
  
b. moves: an array of x, y positions that represent the different valid moves.

  
i. An example of use:

var xNode = boardX + (selectedPiece%5)\*pieceWidth;

var yNode = boardY Math.floor(selectedPiece/5)\*pieceHeight;

var moves = new Array( );

rMove00 = 371;

//Arbitrary values to be given by backend

rMove01 = 59;

//Arbitrary values to be given by backend

moves\[0\] = new Array ( rMove00, rMove01);

rMove10 = 238;

//Arbitrary values to be given by backend

rMove11 = 263;

//Arbitrary values to be given by backend

moves\[1\]= new Array (rMove10, rMove11);

drawValidMoves(interfacecxt, moves, xNode, yNode, pieceWidth);

xNode and yNode are the approximate x and y position of the current piece that has been selected. The given x, y coordinates are currently arbitrary since there currently is no backend in the html demo file. In a completed game, this would take in the x,y coordinates of the valid moves for the selected piece and the arrows will be drawn directly to them.

2) canvasPolyArrow: draw an arrow from the selected piece at fromx, fromy to the valid move at, tox, toy.

  
a. The size of the arrow is decided by importing the width of the piece and then mathematically determining the width of the arrow, the length of the arrow (using Pythagorean theorem), the height of the arrow and length of its sides and base. This also calculates the angle from the piece to the move and a complimentary angle.

<!-- -->

  
  
b. The function then determines the direction of the arrow using the change in x and y coordinates and determines which arrow should be used. One is made for each of 8 directions: N, S, E, W, NE, NW, SE, SW.

c. Using calls to jCanvas, the arrow is drawn and filled with a determined color (defaulted to yellow) using the drawLine method in jCanvas

**Approach:** In order to build this interface, the fundamentals of HTML5 were needed to be learned first. The beginning of the semester was dedicated to taking online tutorials such as CodeAcademy and Mozilla’s Mozilla Developer Network tutorial on Canvas. Once these concepts were introduced, we set out to build the interface. Using the Javascript code of an existing game of Baghchal, we studied both how the canvas is used and how separate JavaScript scripts are called into the .html file. We began writing the code for SlidyInterface.js and wrote a new test.html to emulate the Baghchal code and call our new interface.

In order to write this code without much experience, we began by drawing shapes; first with squares on the valid moves, then circles and finally arrows from the beginning point to the desired move, each using more advanced canvas applications.

In the meta.html file, when a piece was clicked, it would generate valid moves for the piece to slide to by calling our functions in the clicking function. Once we received the piece selected and the valid moves, arrows were to be drawn to these places. The player would then click an arrow and the piece would slide (not drop) to the spot. In the game of Baghchal, we made sure to only show arrows for the tigers during the first phase of the game, and then for both goats and tigers in the second phase of the game.

**Problems and Difficulties**

Throughout the coding process, we ran into several speed bumps, most apparent in the canvas drawing. However the most frequent difficulty that rose was in running the .html file in a browser. Many times a slight change was made using correct syntax, JavaScript would skip certain lines of code and not edit the canvas as we wrote it to. Using console.log calls helped discover that often times the draw function would simply not be called, and other times it would work just fine.

In drawing on the canvas, we struggled between adding to the existing canvas (importing the context from the .html file) and drawing a new canvas on top of the existing one. When we attempted the former, the chosen strokeStyle, or color, of the arrows would change the colors of the board as well. For example, in the baghchal code, the board would turn to green when the green arrows were drawn. We noticed that we could make a new canvas that would draw on top of the existing and attempted that. When this was attempted, a canvas width and height were required; the logical step would be to make these the dimensions of the window. When this was applied, the game extended past the window and placed arrows lower than the actual board. This issue baffled the two of us and after several attempts to debug, we returned to the former format in which we changed the arrows to match the board color.

We redid the entire project using calls to jCanvas and using a similar file in the Gamescrafters Github written in tcl. We also determined that the best place to call the function in the .html file was within a call to “downFunction” which is how pieces are selected when clicked on. This allowed us to click a piece and then draw its valid moves. Arrows were redone using the directional format, which took a lot of math and translating from tcl to JavaScript. The only way to make the pieces slide when clicked on though was to change the entire meta.html file we used as a skeleton using all jQuery and jCanvas calls.

**Next Steps**

  
1. Experiment with the placing of arrows. Since the arrows take in EXACT x, y pixel coordinates, there should be a way to make them point to the abstract board location. This would take some time in learning how valid moves are given to games from the backend as well as figuring out

the abstraction of pixels to the board’s coordinates.

  
2. Color the arrows based on the value of the move, which can be done in the .js file (each

canvasPolyArrow is written with a variable “strokeStyle: ‘<color>’” )

  
3. See if we can actually animate the sliding motion of the pieces without knowing too much about the board.

  
a. Using jQuery/jCanvas calls through the entire .html file.

b. Using click events on the arrows to send the pieces sliding across the board.

c. Changing the color of the arrow as the cursor hovers over it. Would also use an event with jCanvas

d. Showing all valid moves for all pieces at one time instead of having to click a piece to see that piece’s individual valid moves.

4. Start using the SlidyInterface in other games.


