Add\_board\_constructor-destructor\_abstraction\_to\_avoid\_re(un)hashing\_when\_GPS\_cannot\_be\_used\_-\_Mario\_Tanev,\_12-28-2005
====================================================================================================================================

Currently, when GPS is not used by a game module, all its gameplay functions are completely stateless (Primitive, DoMove, GenerateMoves). For some games board hashing and unhashing is very resource intensive, thus they would benefit from keeping temporary state (while a POSITION is under examination) via a constructor/destructor-like abstraction.

Solvers could simply do something like: if (gInitializePosition != NULL) gInitializePosition(position); ... Primitive(), GenerateMoves(), DoMove() ... if (gFinalizePosition != NULL) gFinalizePosition();

Please provide your comments/objections in this wiki!
