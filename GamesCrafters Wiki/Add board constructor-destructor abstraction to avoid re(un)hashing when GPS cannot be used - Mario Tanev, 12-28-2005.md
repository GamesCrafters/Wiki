Add board constructor-destructor abstraction to avoid re(un)hashing when GPS cannot be used - Mario Tanev, 12-28-2005
=====================================================================================================================

Currently, when GPS is not used by a game module, all its gameplay functions are completely stateless (Primitive, DoMove, GenerateMoves). For some games board hashing and unhashing is very resource intensive, thus they would benefit from keeping temporary state (while a POSITION is under examination) via a constructor/destructor-like abstraction.

Solvers could simply do something like: if (gInitializePosition != NULL) gInitializePosition(position); ... Primitive(), GenerateMoves(), DoMove() ... if (gFinalizePosition != NULL) gFinalizePosition();

Please provide your comments/objections in this wiki!
