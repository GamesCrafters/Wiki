Original Games
==============

Currently, GamesCrafters only has modules for existing games (a.k.a. games available in places other than GamesCrafters). This page is for people who would be interesting in creating or simply brainstorming on implementing brand new, original games for GamesCrafters. Besides, of course, the joy of inventing a never-before-seen game (as well as the bragging rights if it actually becomes popular), this will also give Gamesman a creative edge over other game-theory software when it goes public.

If this actually gets to be a group of us, we could probably work with the [Game analysis](Game_analysis "wikilink") group in [Architecture](Architecture "wikilink") to try to come up with what truly makes a game "fun". Knowing that would be a nice way to develop games that are both addicting and fun!

Feel free to update this Wiki with any ideas or brainstorms!

"Registers" (or "Max", apparently)
----------------------------------

Creator: [MaxD](User:MaxD "wikilink")

This is the game I talked about during the GamesCrafter's meeting. It's a very simple Computer-Science-type game, with MIPS-like registers as discussed in CS61C. It's still very much in development and any ideas are welcome as well as encouraged.

### The Basics

Esssentially, there are m "registers" with n "bits" each, all initially 0. So, a game with 4 registers, 8 bits each, looks like the following in ASCII:

`00000000`
`00000000`
`00000000`
`00000000`

Now, on your turn, you can do the following:

-   Turn ANY bit from 0 to 1 (but not vice versa).
-   Shift-Left any register (only if there's no overflow). (The original idea was to only shift by 1, although I guess allowing more could be a variant)
-   Bitwise-Add any two registers, and overwrite one of the registers (again, only if no overflow)
-   Bitwise-OR any two registers, and overwrite one of them.

So, after changing Register 1's 4th bit to 1 (from the right), Register 2's 7th bit to 1, ORing the two and saving it to Register 1, and then shifting Register 1 to the left, we'd get the following board:

`10010000`
`01000000`
`00000000`
`00000000`

Once a register hits its maximum value (all 1's), it becomes locked and no other operations can be used with it (although this doesn't have to be true; the initial reason for this was to not allow the cheap thing of just ORing this register to others to win. However, it might add a whole new strategy, so perhaps this will just be a variant). Now, the point of the game is to get all the registers to display their maximum value. The player to do the operation that sets all the registers to 1 wins the game. (A variant could also be that simply maximizing ONE of the registers wins the game. Or, perhaps, any pregiven number of registers).

### Details

-   The way this is set up, this is a non-loopy, impartial game.

<!-- -->

-   The reason I limited the game to those 4 operations (and not including things like AND, XOR, NOT, etc.) was to keep the game loopy: basically, every move leads closer to having the case with all 1's. (As someone pointed out, this isn't quite true; you could OR two 0 registers, or shift a 0 register. But that's an easy fix of not allowing a move that doesn't change the board.)

Now, there are two ways to complicate the game by allowing other things:

-   -   Make the game loopy. Then we can allow pretty much all the register commands in MIPS, like AND, NAND, XOR, NOT, SUB, MULT, setting bits to 0, etc. The problem is that the game might get annoying if someone keeps ANDing all the registers with a 0 register and generally makes it take forever to finish the game (I could even see the A.I. doing this if it wants to draw). Or,
    -   Keep the game non-loopy, but only allow moves which INCREASE the total register amounts. This was pointed out by the class when I first presented the game, and although it complicates things a bit (especially for the player to simply figure out what's legal by just eyeing the board), it WOULD allow us to add operations like AND to the list.

Out of the two, I like the second one, because the first option adds a huge complexity to an otherwise-simple game. So, we'll see. I'll probably implement the second option, although I guess in the end I would probably write it so that ALL the operations can be turned on or off as variants (with limits, of course, you'd want to keep a FEW options on, of course).

-   There's also room for some variants: a "temporary" register, anyone? I'll post these as I come up with them. (And feel free to provide your own!)

<!-- -->

-   Mostly, I want to keep this game simple. The nice thing about this game from a GamesCrafters perspective is that it'd be VERY easy to implement: the hash function is essentially written, since ANY board position is a legal position (ANY bit can be 0 or 1), so the hash index is just basically taking the bits from the board and appending them together. (At least, I THINK this works... if not, the generic has function can probably deal with this anyway.)

<!-- -->

-   Finally, Dan noted that my game is very vulnerable (though not fully - there are ways to avoid it... I think...) to the strategy in Nim of just mirroring whatever the opponent does, as then you're guaranteed to be setting the last bits to 1. This is something that would have to be avoided on player vs. player (or if the solved game relies on it, player vs. cpu) by Player 1 (by doing a fancy thing with Add and/or OR.

Alex Wallisch, however, provided an interesting variant to me that deals with this problem. Instead of defining the register's indexes (in the 4x4 case) as:

`8 4 2 1`
`8 4 2 1`
`8 4 2 1`
`8 4 2 1`

Instead define them something like this:

`64 32 16 8`
`32 16 8  4`
`16 8  4  2`
`8  4  2  1`

This solves the problem in that you can't be mirrored if, say, you set the 1 or the 64 bit to 1. I'd like to hear comments on this, especially since I'm having a hard time visualizing the game being played this way!

### Finishing thoughts

Again, the entire game is still pretty much in planning, so any comments early on are always appreciated. I'll be updating this page as I make more progress on the game.

Finally, feel free to either post comments on this game, or start another section for your own game ideas!
