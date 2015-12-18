Tic\_Tac\_Toe
=============

Nalimov Database Interface

Overview
--------

Over this semester, we took an existing online chess interface for a Nalimov Database. Our existing program calls their database, and draws and colors the board appropriately.

The main issue we had in this project was mirroring the k4it existing website. Initially, we could not mimic server calls to their database because of web safety protocols of cross server scripting. To bypass this, we made a server side script that recreates the server call the javascript file tries to make, gets the results, and returns these results back to the javascript file. This was our only major, difficult problem in this project. After solving it, we modified the exisiting code to enable delta remoteness and drew arrows in canvas to display all the information on the board at once.

As of May 3, 2013, chess is not working. The server call was working on my local server, but for some reason, the server call is not working on the gamescrafters' website. This needs to be fixed asap.

Members
-------

Savan Patel

Yuhua Wang

Progress
--------

1) Copied and mirrored online interface from k4it.de. Enabled it to work on our own computers.

2) Implemented delta remoteness when mousing over pieces or the endgame table.

3) Drawn arrows from a piece to everywhere it can move. These arrows are also created based on delta remoteness.

Possible Improvements
---------------------

1) Fix the database call. For some reasons, placing bishops just break the database call. Really weird. Also, the database call is not working on gamescrafters website, but worked fine on local apache server.

2) Create an "AI" so that it automatically makes moves. Most people wanted that at CalDay. (Easy to implement. Just get the first move in the endgame table and play it)

3) Create a key and create options to enable disable arrows.
