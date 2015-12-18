Static Evaluator
================

The static evaluator is a general system for providing heuristic evaluation of a board position. The user specifies a set of parameters- traits, scaling functions, and weighting functions- to produce an instance of a static evaluator, which returns a value between 0 an 1 given a position as input. The evaluator will analyse only the placement of pieces on the board- it has no knowledge of game specific information and thus is completely game independant. This requires that the input be a representation of piece positions on the board. While the static evaluator aims to be as general as possible, it can only support board configurations that reduce to a 2D "grid" representation.
