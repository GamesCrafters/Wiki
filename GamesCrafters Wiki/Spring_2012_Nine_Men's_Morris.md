Spring\_2012\_Nine\_Men's\_Morris
=================================

**Goal**

Our Goal was to write a back-end implementation to solve Nine Men's Morris, generalized for three and six Men's Morris as well. This was to be done using David Spies's recently completed parallel solver.

**Project Description**

A lot of the work in the project involved understanding the solver. Much of our code was modeled on the current parallel version of Connect 4. Our game consists of four classes: NineMensMorris, NMMState, NMMHasher, and NMMRecord, each of which directly subclass David's parallel solver code. The primary problems that we faced while completing the project were: 1) Creating a representation of our board and game state such that winning conditions and child states could be easily detected and calculated. Similarly, we needed to create a simple mapping between board representation and game state hash (using the GenHasher), which is critical when using the RangeTree solver. 2) Properly generating the set of all possible moves in the makeMoves method in NineMensMorris. Our move representation needed to take into account the multiple stages

**Future Work**

In future work we could synchronize with the GUI. We could also perform more testing to make sure it works for generalized versions of the game. Due to the constraints imposed on us by dealing with the complexities of the new parallel solver, we were unable to adequately test the game. This should be done next semester.
