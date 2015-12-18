Add UninitializeGame abstraction - Mario Tanev, 12-26-2005
==========================================================

Some games utilize SafeMalloc in InitializeGame and they obviously don't free the allocated memory when the game ends. Thus I propose a gUninitializeGame abstraction (since we can't force games to implement one), which will be called when a game is finished solving/playing.
