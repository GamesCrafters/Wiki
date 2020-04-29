## End of Semester Write Up - Olvera

### Puzzles Team

Led by: Anthony Ling

Members: Mark Presten, Arturo Olvera

### Contributions

#### CalWeek Video

Anthony, Mark, and I made a [video](https://youtu.be/HRQUtvclvLM) for CalWeek,
explaining how we solve puzzles and how they are different than other
gamescrafters games.

#### Npuzzle

This semester, my main project was implementing Npuzzle. Npuzzle is an NxN
version of [15 puzzle](https://en.wikipedia.org/wiki/15_puzzle), where a 4x4
grid populated by tiles numbered 1-15 and a blank space must be scrambled and
then arranged in ascending order with the blank piece in the bottom right. The
analysis of others has shown that the total possible number of positions for an
NxN grid is N!/2, this means that the largest puzzle we can reasonably store is
3x3.

The implementation built off of Anthony's `PuzzlePlayer` and `GeneralSolver`
and was written in python. The puzzle can currently be played in 3x3 and 2x2
variants on a text based view, but times out with any larger sizes. Further
along into the semester I merged Anthony's `ServerPuzzle` into into Npuzzle, so
that the puzzle can be played on the Gamescrafters server. All my work can be
found on the `npuzzle` branch of the
[`GamesmanPuzzles`](https://github.com/GamesCrafters/GamesmanPuzzles) github
page. 

While the backend of npuzzle is mostly complete, there is still a need for a
front end so that the puzzles can be played with a GUI on the server.
