Adding new solved games
=======================

Manually solve a game
---------------------

This is kind of a hack, but basically we make a copy of an existing job with the options we want, solve with those options, and copy the database into the solved/ directory.

`cp jobs/Connect3_33.job jobs/Connect5_55.job`
`nano jobs/Connect5_55.job`
`java -cp bin edu.berkeley.gamesman.Gamesman jobs/Connect5_55.job`
`mv -i database33.db solved/connect4_width_5_height_5_pieces_5.db; done`

Note the naming scheme. It must be named in that pattern (connect4 is the game name, so don't change the 4) for the GamesmanJava server to be able to find these databases.

Watch out that you don't run out of memory. 3x9 is about as much as nyc can handle, and it's more optimized than most games we have.

Solve multiple games
--------------------

Here's how to solve four games at once using a for loop and sed to change a single value in the job file:

`for x in {6..9}; do`
`    sed -e 's/`\(game\.height =\)`[0-9]*/\1'"$x"'/' < jobs/Connect3_33.job  > jobs/Temp.job`
`    java -cp bin edu.berkeley.gamesman.Gamesman jobs/Temp.job`
`    mv -i database33.db solved/connect4_width_3_height_${x}_pieces_3.db; done`
`done`
