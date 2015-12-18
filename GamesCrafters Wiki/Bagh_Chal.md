Bagh\_Chal
==========

The Bagh Chal project is being headed by [Max\_Delgadillo.md](User:MaxD "wikilink") and [Deepa\_Mahajan.md](User:Dmahajan "wikilink"). This page concerns not the C implementation of the game (as most of the New Games pages are), but rather the ongoing look at how this game will be solved, using a brand-new Bagh-Chal-unique solver. I pretty much went ahead and had a massive brainstorm and posting everything I could think of here. Any comments by anyone would be greatly appreciated, and this page will probably be updated on a weekly basis at least.

C Code
------

To get this out of the way: The C code is pretty much Dom's code which Deepa and I went through and cleaned-up. We're still not TOTALLY done (as we might have to change the hash function), but the idea is we'll have a FULLY working version of the standard, 5x5 Bagh Chal game with no variants on CVS by Monday. HOPEFULLY...

In any case, I think we'll HAVE to have the FINAL hash function before we even START doing this, since we're literally going to create this database only ONCE.

As for variants, and such... those will have to come later. Solving is the priority for now.

Disclaimer
----------

First of all, no matter what, this game will NOT work with the current implementation of Gamesman. We intend to use Scott's file-memory-db (in fact, we CAN'T do it without it, since there's no way to load the multi-GB table to memory). Thus, before we even begin to do this, we NEED that database. HOPEFULLY we'll have it by Monday as pinky-promised. :)

That said, before going on about this solver, I have 2 things to ask of my fellow Gamescrafters:

-   When finished (or heck, even when first starting), the database will be WAY too big for Gamescrafters to load into memory. That means, as I said, the game won't even RUN until SOMEONE changes the implementation of Gamesman so that it uses the file-based memory database. So we'd like to ask as a favor to the [Architecture.md](Architecture.md "wikilink") group is ANYONE is willing to do that, and not only someday but as soon as possible.
-   Also, having a GUI to work with would be REALLY nice. Not required, but nice. So we'd also like to ask someone from [Graphics.md](Graphics.md "wikilink") or [Retro.md](Retro.md "wikilink") if they could spend like a week and developing a basic GUI for mbaghchal.c (once we put the most recent version up) to work with? It doesn't even have to be fancy or the final version (since, indeed, we STILL have to go back later and add variants anyway), all we want is a basic GUI with the ability to display the color values. So I'm hoping it shouldn't take TOO long for an experienced TCL/TK user.

Anyway, I'll ask both of these requests next Monday during the meeting.

The Solver Itself
-----------------

First of all, we won't actually be using Gamesman's gSolver method to solve this (it's much more complicated than that). All gSolver will do is be non-NULL so Gamesman doesn't try solving the game and overwriting the database. The idea here is that the file will HAVE to be provided, pre-solved, rather than be solved on the spot (since, let's face it, we wouldn't want EVERY computer to have to go through and create the multi-GB file on their own). Again, the file cannot be loaded into memory, so the Gamesman implementation running it will HAVE to use the file-based database system (read above).

The solver itself, then, will be a completely non-Gamesman based, called-from-outside solver. We'll probably put the code for it in mbaghchal.c and call it with a Game-Specific Menu interface, but we might just have a whole seperate file instead.

Now, the solver itself:

### Philosophy

I'll add the details for Stage 2 games only for now. Stage 1 is a whole other nightmare we'll deal with afterward...

The idea is we have a system like this (pardon the bad ASCII art):

`...`
`^`
`|`
`All positions with 2 Goats`
`^`
`|`
`All positions with 1 Goat`
`^`
`|`
`All positions with 0 Goats`

Basically, dealing with just Stage 2 games for now, we have 21 tiers, and each tier is all the boards with 4 Tigers and N goats, 0 &lt; N &lt; 20 (inclusive). To create these tiers, we'll need an additional function call to the original C code: EnumerateMoves(n), which takes an integer n and returns a list of all the POSITIONs of the appropriate tier. Two notes about this function: one, it's the only additional function required of mbaghchal.c that will be needed by the solver. This means that, if we were to generalize the solver code at some point in the future, we'd need the game developers themselves to include this function if they wanted to use this solver. Secondly, in order to deal with the whole "illegal board positions" thing, we could optionally have this list only return positions which are actually legal (since this is based on the actual GAME being implemented rather than an abstract solver so ideally it knows what positions are legal or not), although it's not required (just makes it slightly faster).

Now, the solver. In general, it will only work on two tiers at a time: tier i and tier i+1. We assume i is fully solved. We also know that, for ANY tier, GenerateMoves() will return a move that leads to a position either in the same tier, or the tier directly below it, and nothing else (a KEY thing to note for this idea to work). So, if i is solved, all we do is call EnumerateMoves(i+1) and get a list of ALL the parents of i, and then we can solve this whole tier using the process of either the basic loopy solver or the zero-memory solver (go through all the list of i+1's children and, for any children that are a LOSE, set the parent to WIN. Then run through the rest and do the whole keeping-track-of-the-children thing).

The algorithm itself doesn't seem THAT hard to grasp (or code, for that matter): the key will be in actually taking the time to RUN the code and solve it. But, we'll worry about that later.

For now, we move to:

Implementation
--------------

### Initial Business

The first thing is a little initialization we run just once, at the beginning:

-   Through a HUGE for-loop, initialize the ENTIRE database (yes, EVERY position) as "undecided". This is so that we can actually have a completely readable database and play a half-solved game. (And this way we can test it on every solving iteration).
-   Next, initialize Tier 0 (that is, the tier of all board positions with 0 Goats) to start with, by just literally running through them all and calling Primitive on it and storing its result in the database. (Although if I'm not mistaken, they're ALL going to be LOSE for Goat and WIN for Tiger anyway.)

### Solve Iteration

Now, the plan is that we're going to build the solver such that we can solve it in steps: that is, after initialization, we solve Tier 1, and then the solver stops running, until we later manually call it with Tier 2. This is to keep it nice and manageable - plus we're going to be running this on my home computer (my good old desktop, with a 2.08 GHz AMD Athlon XP Processor and 1 GB of RAM, which will hopefully do the job well for at least the first few tiers), so it'd be good to be able to take breaks in between tiers. We also are definitely going to implement a sort of status bar telling you exactly how many positions it's done and how many it still needs, and hopefully some estimates of time left too. Also, if we find a clever way of doing it, a way to actually pause the process and then restart at the same place would be nice. Although it's not required, this would also facilate the process of finding a way to actually split up the data if we would have to find that the only way to solve would be the whole parallel solving thing.

Anyway, as for the code itself, the pseudocode is as follows(very, VERY liberal pseudocode):

`SolveTier(int n) {`
`  SOME_LIST_STRUCTURE list = EnumerateMoves(n);`
`  // implement the loopy solver (or alternately, just CALL the loopy solver)`
`  // a possible custom way is as follows:`
`  for all the elements pos in list`
`    pos.chidren = GenerateMoves(pos); // these lists are stored SOMEHOW   `
`  while (this loop still causes change) {`
`    for all the elements pos in list {`
`      for all the elements child in pos.children {`
`        if (database_getValue(DoMove(pos,child)) == LOSE) {`
`          database_set(pos,WIN);`
`          list.remove(pos); // remove from fringe`
`        }`
`        else if (database_getValue(DoMove(pos,child)) == WIN)`
`          pos.remove(child);`
`      }`
`      if (pos.child.size() == 0) {`
`        database_set(pos,LOSE);`
`        list.remove(pos);`
`      }`
`    }`
`  }`
`}`

I THINK that's the basics of the loopy solver, glossing over any ugly details (someone correct me if I'm WAY off). As Dan noted on the newgroup (below), we might just be able to literally call the existing loopy solver itself (discussed later).

### Extra Notes

Five things:

-   It bears repeating: we NEED to have Gamesman changed so that it works with the file-based database before we can even RUN the game on Gamesman. So can someone from [Architecture.md](Architecture.md "wikilink") get on that while we code this?
-   About generalizing: for now we're literally only making this a Bagh Chal solver. Later, we (and I fact, I think I myself might do this next semester) could generalize the code into a step-by-step general solver for ANY big game (Nine Men's Morris, anyone?). That's something we won't worry about this semester, but it's something to look forward to (is solving CHESS in the future of Gamescrafters? With the file-based memory database handling arbitrary-length databases... who knows?)
-   About the Parallel solver: So, in the end, it might turn out my trusty (or actually, not-so-trusty) compy won't be able to solve the bajillion positions on its own. In that case, we'd literally be stuck at a dead-end (or simply a slooooooooow going process) until the parallel solver is implemented. In that case, my and Deepa's job would be pretty much done until the [Architecture.md](Architecture.md "wikilink") team (perhaps with our help, even) implement some sort of parallel solver. But at that point, that would be it for what we could do... so hopefully it won't come to that!
-   About that optimum Goat number: Of course, one of the big reasons we're doing this is to analyze the results and ultimately find out what is the least number of Goats you can have and still win. After reading some of [Game\_analysis.md](Game_analysis.md "wikilink")' page, though, I think they're pretty much going to implement the procedures needed to do this, and the answer would be a function call away. If not, though, the C code to look through and find out wouldn't be TOO hard to do, so I won't focus on it for now.
-   Finally, Dan's note on the newsgroup is addressed here.

Here's what Dan posted on the newsgroup.

`1. It's easy to create a position that is illegal:`
`(Goats to move)`
`T T T T G`
`G G G G G`
`G G G G G`
`- - - - -`
`- - - - -`
`Tigers could not have *just* moved to get in this position.`

Hmmm... yeah, that looks like it's illegal, alright. However, given the fact that the total number of positions is somewhere in the billions, having a few dozen (ok, a few hundred) positions be illegal is something which I don't think should make THAT much of a difference. :)

`2. Looking at the two levels i and i+1, there are two ways to solve it, as we discussed in the meeting:`
`a. Work bottom up, from the ith level to the i+1th level, using the frontier method, keeping track of the active`
`frontier, etc, like the loopy solver. You'll need GenerateUndoMoves for this.`
`b. Work top-down, from the i+1st level to the ith level, in a zero-memory-solver technique, sweeping through the`
`i+1st level over and over and over until nothing changes. No GenerateUndoMoves needed here.`
`It seems to me if we can get Scott's file-memory-db set up, (a) is much much much much much much better than (b).`
`If you look at the loopy solver, it might be possible to JUST CALL IT! I.e., it might be the case that you can`
`break the loopy solver into stages:`
`(i) walk down, set up parent pointers`
`(ii) define frontier of the primitives`
`(iii) walk up until you can't anymore`
`(iv) anyone visited who has not been labeled is a draw`
`You would cut into this code at (ii.5), right after the frontier is defined (you have frontier already -- level i)`
`and have it process stages (iii) and (iv) for you!!`
`You'd have to write GenerateUndoMoves, no big deal.`
`dan`

Ok, a few notes. First of all, as I noted, we're doing method (a) of course (bottom-up). Secondly, we don't need GenerateUndoMoves OR the initial walk down: the property I stated before (at tier i, you only have possible moves that lead to either i or i-1) makes it so that ALL we need is (i-1) to be solved (which it is) and EnumerateMoves, and we're set. (We COULD do GenerateUndoMoves, but it seems easier to just enumerate them manually and get the list that way). Secondly, this brings up what I said before: we might be able to just use the loopy solver given! We'll have to look into how exactly this will work though... more details to follow.

Last Thoughts
-------------

That's all I can think of for now. I was literally brainstorming all the ideas that were floating around into the Wiki as fast as I could, so I'm sorry if it's all confusing (I'll proofread it and add things later on). Anyway, any comments either here, in the newsgroup/mailing list, or during the meetings, are GREATLY appreciated.

Ah yes, and later notes on more of the C Code (such as the planned variants) and the Stage 1 solver (which complicates things a bit) next time...
