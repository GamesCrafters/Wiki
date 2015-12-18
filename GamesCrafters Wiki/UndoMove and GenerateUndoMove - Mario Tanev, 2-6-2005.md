UndoMove and GenerateUndoMove - Mario Tanev, 2-6-2005
=====================================================

Since the current loopy solver is very space-inefficient, I don't think it's such a hassle to require loopy games to write UndoMove (which GPS requires as well) and GenerateUndoMoves.

Thus the algorithm can still work down in an iterative fashion, adding all leaves to the initial frontier, and marking all nodes (positions) it has encountered as visited, but NOT creating lists of incoming edges as it does now.

The frontier percolation mechanism would be the same as it is now, with the exception that reverse incoming edges would be generated via GenerateUndoMoves. If by any chance GenerateUndoMoves generates a move to a position that is not actually in the game graph, it would be ignored as it has not been marked visited. The only requirement for GenerateUndoMoves would be to generate only moves to hashable positions (which is perfectly possible for combinatorially-perfect hashes; it wouldn't be as simple, perhaps, for absolutely perfect hashes, but if a person actually wrote one, I am sure they could figure out how to do it). By 'hashable' I mean that the hash function would generate a unique hash within the range of gNumberOfPositions.

Since a position only examines its parents when it has a known value, undo move generation would occur only once per position. Thus the overall computation would be equivalent to traversing the abstract game-graph twice.

Any thoughts?

--Mario

Excellent!!

This is a really great idea, Mario. Do you want to volunteer to add it to our system as another 'solver' and then test it against the current loopy solver?

My only concern is that GenerateUndoMoves \*must\* always generate a superset of the possible parents. If it missed just one actual parent, the entire tree could be corrupted...

Then, the next step would be to take your algorithm and adapt it to use Scott's new db system so that the db could be in memory or in a file.

Next, we figure out how to take JJ's algorithm to parallel-ize the solver and apply it to your algorthm...

--dan

On Saturday 04 February 2006 15:44, ZIMMER, BRIAN wrote: &gt; What about games where pieces are taken (ie Tile Chess =p) ?

Generally most loopy games have capture, thus there are positions where there a many possible undo moves to generate. That indeed makes it harder to implement by the game module. However since it is very likely that most of them lead to a valid (i.e. reachable from the initial position via some path) parent, the corresponding downward move would have been computed too in GenerateMoves at some point. Thus, generally, computationally things should add up and there shouldn't be efficiency lost.

That said, I think Tile Chess is different in that regard, because if I remember correctly, it currently constructs a particular board as the initial board rather than allow the players to place the pieces first. That might eliminate a lot of positions from the game graph, but it would be very difficult to tell that from a particular position below the root. Same reasoning applies to any "initial position" or "restricted placement" games (such as chess).

I intended "require implementation" to be implicitly supplemented by "if the game is to be solved with space efficiency".

&gt; Would I have &gt; to keep an array of what pieces were taken from which spot to be able to &gt; undo the move?

No, you can't do that. You would need to generate all possible undo moves.

&gt; Also, since our board is relative, and is constantly &gt; resizing, it would be somewhat difficult to extrapolate back to a larger &gt; board size..

Well the game cannot grow nor shrink by more than unity, so it's not completely arbitrary - there is a finite amount of undo moves.

&gt; perhaps the move would tell us which direction we would need &gt; to expand the board back... I'm guessing that its possible, but it seems &gt; like its not trivial and we would be wasting resources keeping track of &gt; what happened and extrapolating how to undo things. Don't know for sure &gt; tho, what do you think?

You wouldn't be wasting resources keeping track of anything, as you shouldn't be keeping track of anything other than the initial position. There are various optimizations (like if the game started without a knight, you shouldn't have an "undo capture the knight"), but overall I can see how Tile Chess could generate a lot of invalid undo moves. This means there could be a significant computation overhead over the downward traversal.

In the end, maybe this will end up being slower than the current space-hogging method on machines with enough RAM.

But in such endeavors we always do work that in the end may need to be discarded, because unless we make a thorough mathematical analysis of the game, we never know. Take Quarto for example, it's around 3000 lines of code right now, 1000 of which are not used anymore, and countless of functions which have been so heavily modified that only CVS could tell how many there were, but who cares.

So it would be up to the game module's implementors to decide whether to do that.

&gt; &gt; ~Brian

-Mario
