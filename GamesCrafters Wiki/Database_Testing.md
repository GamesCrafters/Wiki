Database\_Testing
=================

    Testing Database Module

    Known Bugs: 

    IMPORTANT:
    The java gzip library seems broken.  Specifically, the byte alignment breaks down after about 500 reads or so.
    For instance, reading position 2134 returns 722, when it should be 1026 (for tic tac to variation code 3).  Java's library is reading bytes 3,4, when 4,2  should be read.  It should be noted that a 2 follows the 4 in the hex file (that is we are off by 1).
    I do not know why this is happening; I can only conclude that java's library is broken (feel free to audit by code).

    Interestingly, this doesn't manifest itself in seek mode.  I cannot explain this.

    So know that seek mode seems to work but "pre-load" mode has bugs.

    Oh, and I didn't bother modifying the db format.  There really is no point with slice coming soon.

    ALSO IMPORTANT:
    Module exceptions are not handled yet.  I didn't have access to the 'net all day and wasn't sure how other classes should implement them, or which ones are reserved yet.  They'll take 10 min to add, but I need to know
    1) Are the codes class-based or error based?
    2) What code range can I use?


    On to testing:

    TestDb.java exists in the expected location (gamesman\java\test\edu\Berkeley....gamesman\TestDb).
    To compute expected values, I gave on testing gamesman directly.  Rather I ripped the seeking code from memdb and placed it in my own file.

    memdbtest.c may be found in gamesman in gamesman\java\test


    The basic trick to manual testing is expected input/output verification.

    To generate expected output:

    compile memdbtest.c with:
    gcc -o memdbtest -lz memdbtest.c

    Move memdbtest into the gamesman\bin\data directory

    Solve some games (random ones) to generate databases.

    Now in bin\data

    Run:
    ./memdbtest <databasename>

    e.g.
    ./memdbtest mttt_3_memdb.dat.gz


    You will now be prompted to enter positions.
    Type in numbers between 0 and the number of positions for the game.

    for instance typing "1283" <enter>
    Might return 256.

    Do this for as many inputs as you desire.

    To exit, just hit <Ctrl-break>

    Then execute the TestDb module (preferably in eclipse).

    Enter in the absolute path where your gamesman databases are found.  Do NOT terminate with a "/"
    e.g.
    /home/astaley/gamesman/bin/data
    Now enter in the gamename
    e.g.
    ttt
    Finally enter in the variation code:
    e.g.
    3

    Then enter in positions as you did with memdbtest
    When you are done hit "q".

    The output will then be printed out in the same order as the positions entered.
    (that is first output corresponds to first input entered).

    New inputs will then be queried for.

    The multiple input tests the "batch" (handling multiple position queries simultaneously) support of the dbmodule.

    To exit, type q before entering any more positions (note that submitting a request for 0 positions is not legal).


    Warning: note that many debugging print messages are printed.  You only need to concern yourself with the messages starting with length, followed by value #n.

    Mode control:
    By default, the test module tests gamesman in gzip seeking mode.

    To test pre-loading mode, change the following code in TestDb (lines 46-52):

            //Use below 2 lines if preload
    /*
            arg[1] = Integer.toString(1);
            arg[2] = fname;
        */  
            //use below line if not preload
            arg[1] = Integer.toString(0);


    to

            //Use below 2 lines if preload

            arg[1] = Integer.toString(1);
            arg[2] = fname;
            
            //use below line if not preload
        //  arg[1] = Integer.toString(0);


    Again, this mode suffers from the bug described above.

    Be sure to test many databases and a wide range of input.

    The positions that should be tested are:

    0-10, middle positions, numpositions-10, numpositions-1

    Be careful to not test numpositions or higher, because exceptions are not yet implemented (see above note).

    Sorts, anti-sorts and random sorts of arrays should also be tested.



    No automated system exists, as this is only a proof of concept demo.  Testing on 50 inputs or so for several games should be enough.  I do not want to define a formal test plan, as far too many permutations exist.
    If you feel an automated system is extremely important, let me know - and I'll write one in a few hours.


    -Aaron
