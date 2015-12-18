Rearrange Solver Writeup Fall 2010
==================================

The goal of the Rearrange Project is to implement the Rearrange Hasher and Solver and to see if there is any gain in efficiency over the Dartboard Hasher with the regular Tier Solver. Both of these hashers are aimed at solving dartboard games.

The idea is that for some dartboard games like TicTacToe, Connections, and Y, we can look at pieces of the player who last moved to determine if the game has ended. In other words, we do not have to look at the other player's pieces when determining primitive value. The Rearrange Hasher and Solver takes advantage of this. It performs a bottom up tier solve but unlike the Dartboard Hasher, iterates through a tier by rearranging first the pieces of the current turn's player before rearranging the pieces of the previous turn's player. That way, we only have to check for primitive value when we rearrange the pieces of the previous turn's player as opposed to for every position. This is accomplished by encoding the current turn's player's pieces as the minor hash, and the other player's pieces as a major hash.
