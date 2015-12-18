Solving Progress Bar
====================

Ideas
-----

### A

-   create new thread to solve game (thread::create)
-   game can solve in the background
-   main tcl thread must communicate with C somehow to get progress (push or poll)
-   make sure return value of DetermineValue is still obtained by tcl

### B

-   from C run a tcl script to update the GUI while solving
-   tcl may be "frozen" and not update ??

