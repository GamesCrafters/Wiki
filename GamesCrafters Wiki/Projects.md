Projects
========

For Calday
----------

-   For CalDay, we have to have Sean's pen generate saved games which the GUI should use to genereate a post-game analysis PDF file that gets printed out for them

**Project Proposals/Ideas**
---------------------------

-   [Cal\_Day\_Shifts\_List\_-\_Joey\_Corless,\_2006-04-17.md](Cal_Day_Shifts_List_-_Joey_Corless,_2006-04-17.md "wikilink")
-   [UndoMove\_and\_GenerateUndoMove\_-\_Mario\_Tanev,\_2-6-2005.md](UndoMove_and_GenerateUndoMove_-_Mario_Tanev,_2-6-2005.md "wikilink")
-   [Makefile\_changes\_-\_Evan\_Huang,\_12-14-2005.md](Makefile_changes_-_Evan_Huang,_12-14-2005.md "wikilink")
-   [Uniform\_database\_save-restore\_via\_traversal\_abstraction\_-\_Mario\_Tanev,\_12-20-2005.md](Uniform_database_save-restore_via_traversal_abstraction_-_Mario_Tanev,_12-20-2005.md "wikilink")
-   [Make\_-O0\_the\_default\_optimization\_flag\_-\_Mario\_Tanev,\_12-26-2005.md](Make_-O0_the_default_optimization_flag_-_Mario_Tanev,_12-26-2005.md "wikilink")
-   [Add\_UninitializeGame\_abstraction\_-\_Mario\_Tanev,\_12-26-2005.md](Add_UninitializeGame_abstraction_-_Mario_Tanev,_12-26-2005.md "wikilink")
-   [Add\_board\_constructor-destructor-save-restore\_abstraction\_as\_substitute\_for\_GPS\_-\_Mario\_Tanev,\_01-13-2006.md](Add_board_constructor-destructor-save-restore_abstraction_as_substitute_for_GPS_-_Mario_Tanev,_01-13-2006.md "wikilink")
-   [A\_General\_GUI\_for\_basic\_games\_using\_only\_C\_function\_calls\_-\_Joey\_Corless,\_2-27-2006.md](A_General_GUI_for_basic_games_using_only_C_function_calls_-_Joey_Corless,_2-27-2006.md "wikilink")
-   TODO: Article on Tie vs. Draw

<!-- -->

-   **[Architecture.md](Architecture.md "wikilink")**
    -   [Gamesman++.md](GamesmanPlusPlus "wikilink") {R&D = Robert&David, Max, Casey, Ben, Filip, Evan, Alan}
        -   Requirements: C++, some experience with gamesman
        -   6 components (shells (java), framework (sr), testing, runtime (sr), modules, games & documentation)
        -   Dev mtgs monday @ 5:30pm in 6th floor west alcoves
    -   [Networking.md](Networking.md "wikilink") {Hsiu-fan, Filip, Matt, Ramesh, Ofer}
        -   Deploying server + eharmony
    -   Database {Ofer, Evan, Ken}
        -   MERGE!!! File DB, Zero memory player, Virtual mem {Evan, Ken}
        -   Serving database through mySQL
        -   History and accounts (??)
    -   Analysis + Interestingness {Matt + Omar}
    -   [Static\_Evaluator.md](Static_Evaluator.md "wikilink") {Michael, Brian, Jonathan, Davide}
        -   Way of evaluating a board and returning a value (-1 &lt;-&gt; 1)
        -   File format for static evaluator, learning algorithms
    -   [Autogui.md](Autogui.md "wikilink") (Keaton, Pat, Kevin, Michael, Alex)
    -   WinByUpdating (Alan)
    -   Autosymmetry (Albert)

<!-- -->

-   **[ODeepaBlue.md](ODeepaBlue.md "wikilink")** (Parallelization) {Ofer, Deepa, Max}
    -   hadoop map-reduce!
    -   multi-thread

<!-- -->

-   **[Maximization.md](Max "wikilink")** {Max, Ofer, Manu, Nishant}
    -   GREAT NEW OPPORTUNITIES FOR NEW STUDENTS
    -   You would take a game that doesn't solve and tierify and SOLVE
    -   [Quarto!.md](Quarto_Tierify "wikilink") (Yanpei, Beno)
    -   [Pentago.md](Pentago_Tierify "wikilink") (Jun Kang)
    -   Maximize Toot-n-Otto + docs (Zach)
    -   Your name here!

<!-- -->

-   **[Retro.md](Retro.md "wikilink")** {Eudean (Foxes, 3Spot), Larry (Connections), Yuly, Simon, Albert}
    -   Finish goldifying 6 games, foxes is almost done.
    -   Tcl/Tk (we'll teach), C (you should know)
    -   Fix things that are broken
    -   OPPORTUNITIES FOR PEOPLE WHO WANT TO LEARN GUIS AND TCL/TK
        -   6mm GUI (Pat, Kevin)
        -   Shift-tac-toe (Diana)
        -   Rubix Checkers (Brian)

<!-- -->

-   **[Graphics.md](Graphics.md "wikilink")** {Sean, David, Davide, Brian}
    -   Some Retro stuff
    -   [SeanPen\_Interface.md](Digital_Pen_Interface "wikilink") (Michael, Sean)
    -   [Auto-analysis.md](Auto-analysis.md "wikilink") to printout
    -   Play human-human-but-solve
    -   [T-shirt\_design.md](T-shirt_design.md "wikilink") committee
    -   [CalDay.md](CalDay.md "wikilink") coordinator {Jerry, Omar, Patricia, Kevin, Daniel, Andrew}

<!-- -->

-   **Nice Games** {BAY = Brian, Alan, Yanpei, Ilya}
    -   GREAT NEW OPPORTUNITIES FOR NEW STUDENTS
    -   -   Actually\* solving games
    -   BIG BUGS / COMPLIANCE
        -   Variants (finish)
        -   MoveToString
        -   ActualNumberOfPositions
        -   GPS
        -   Symmetries
        -   GetOption/SetOptions \[C and GUI\]
        -   Help strings (also documentation)
    -   Particular games
        -   AtariGo -&gt; Go -&gt; Docs (Alexander)

<!-- -->

-   **[Docs.md](Documentation "wikilink")** {Jerry, Kevin, Diana, Philip, Alex, Yanpei, Andrew}
    -   Human docs for website
        -   HUMAN analysis
        -   History for games that don't have it
        -   Typos, font fixes
        -   Website update with photos, biographics, alumni doing now
        -   Every new person needs to send their biography (see web)
        -   100x100 text game images
    -   Wiki reorg
    -   Massive merge of all rules strings
    -   Coding docs for APIs that have no docs
    -   GUI has code authors' photos (C and GUI authors)

Promises for pre-8:30 folks (Docs for everything, pinkie default) don't forget \_\_
-----------------------------------------------------------------------------------

-   **Albert** (Lines of Action works now! | Board size adjustment √, misere √ || Makefile, 1-based variant, other 12 things)
-   **David W and Junkang** (Debugging | Pentago solved untiered || 12 checkoff items, Makefile, 4-in-row variant, print-move tighter, predictions + who-x-is, turn debug off, misere test, different-board-display ||| tierification)
-   **Shah and Jacob** (Hex input handling | Hex solved untiered || 12 checklist, name instead of player1,player2, newline before prediction, variant of larger boards in game-specific menu, a1 lower-left-corner, variants of misere changing number)
-   **Kevin and Patricia** (6mm player-player, stages being debugged, tierifying | Tierified 6mm & 9mm || 6,9 to 9, no square brackets in printmove, dot from achi instead of \_ for printposition, fix PrintMove glitch, /n is not a newline, old authors in kauthors)
-   **Jerry and Daniel** (Abalone bugfree and follows convention cleaned code we think works | Drawn board, Tierified, stretched || remove end, ||| show rank/file indexes right by it, make it look like wikipedia's abalone board)
-   **Zach** (|| xmtootnotto to Xmtootnotto, demo)
-   **Alexander** (Go rules mostly in, thinking about AtariGo | AtariGo maximize-no-pinkie || fix undo 'u' working, lowercase file, tell me whether I'm X or O)
-   **Alvin** (Mancala Tier implemented | Mancala variants (same as before) working!)
-   **Diana** (Goldifying Chung Toi ||| Goldify Shift-tac-toe? To rotate <http://wiki.tcl.tk/8595>)
-   **Aaron and Glenn** (Quickchess working again! | Tierified 3x4,5x6 || variant fix ||| Pawns?)
-   **Yanpei** (Docs, Team lead | Finish docs tierdoc finished, all of max's changes, doc on docs, doc on Quarto!, Canonical/symmetry doc)
-   **Simon** (Doc on Cambio | Tierified 3x3, 4x4, 5x5 | Added variant for initial placement | Fixed getOptions/setOptions)

Promises for post-8:30 folks
----------------------------

-   **Alan & Jon** (Win-by for othello for loop-free solver and play using it || add it to 'ps' output, allowing user to choose to play against a win-by via remoteness or win-by optimization, win-by for iceblocks! ||| have the option that the computer can play to minimize win-bys vs maximize win-bys)
-   **Ofer** (Tutorial, Parallelization, Working solver + level creator, gui wrapper? || waiting for deepa)
-   **Keaton** (rewrite pattern matching code not documented, board decorations, animation ||| make animation look like tcl, applet, undo)
-   **Tim** (load/save, solving % for all games || will show after commit)
-   **Ann & Diana & Jerry** (Docs that blend the game descriptions of XGamesman.new and web page || fraction done, merging of all data from xgameman.new and html, better name, put scollbar on right for left,top,bottom view, XGamesman.new becomes .old, this becomes .new)
-   **David W** (New non-buffer-overrun-reading text API | Help with docs, Xgamesman.new admin facility! ||| Three games goldified)
-   **Matt and Alan** (new xml parsing + table + HKN column sorting + game overview page-&gt;game-&gt;variant, interestingness + play from this one, auto-game-analysis? || sort by num on web hkn, get data from code not from grep, debug flag listing your root directory, allow me to see interestingness + play from here)
-   **Max** (random board start, parallelization | visual value history, undo, ataxx misere || level files? ||| debugger, tier+bpdb)
-   **Brian & Michael** (static evaluator file format xml, scaling & weighting functions, 1210, nim, connect-4, basic demo, given traits and database=&gt;parameterize it, select traits?, arbitrary geometric traits?\*, static evaluator DB -- only where SE is wrong? || print current SE, merge code and check in, make static eval menu cleaner, unhack core so stuff still works || change SE on the fly, make default random if I don't say anything (that way I can play player-vs-unsolved-computer trivially, make sure you merge with keaton's linear unhash function ||| can we find good/perfect partitions of se values?, accuracy checker, edit and delete)
-   **Sean** (redo, progress bar, solving % optional function, load/save help, load/save/redo GUI | CS160 splash, db loading %, move load/save game next to new game)
-   **Ken** (Document Everything! Finish integrating bpdb into gamesman √; Integrate huffman encoding for greater compression. Also, potentially integrate ODeepaBlue.)
-   **Eudean** (dots and boxes goldified!! | animate + something other than circles alone + mark boxes won + GS\_Set/GetOption)
-   **Ramesh and Filip** (finish core server: eharmony, db server, network play, basic chat, cgi-bin testing)
-   **Robert** (Gamesman++ 1,2,...,10?, talk to Eric | prototyping)
-   **David P** (OpenPositions Writup?, Gamesman++ spec ready for framework & runtime)
-   **Deepa** (ODeepaBlue Level files done + docs + tests | integrated + bagh chal?)
-   **Alan & Brian** (maximize?)
-   **Matt** (Finish network db, eharmony client, update gui and text client to play against another player online)
-   **[Evan.md](User:Hevanm "wikilink")** (Finish improving the disk-based filedb/VM system √ ||| Write Docs)
-   **BEST OF THE BEST** : eudean, ramesh, filip, davidp, robert, ofer for staying to the end!

