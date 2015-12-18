Solvers Writeup Spring 2010
===========================

About the Project
-----------------

### Goal

The focus of the Solvers Team for this semester is to provide the back-end support for the two dartboard games (The Game of Y and Connections) that Gamescrafters are working on. This involves strongly solving the two games and having the data of the solved game available.

### Members

-   **David Spies**:
    -   Solvers Team Lead

<!-- -->

-   **Rohit Poddar**:

<!-- -->

-   **Sri Thatipamala**:

<!-- -->

-   **Thomas Lam**:
    -   Coded the hash and unhash functions on the generic hasher that would work for any dartboard game involving pieces of two different types(colors)

<!-- -->

-   **Yang Wen**:

<!-- -->

-   **Yian Shang**:

### Code Overview

-   **MMHaser**:
    -   The hasher is a generalized version of the hasher used to solve Connect 4. The generalization allows for similar efficiency techniques to be applied in the solving of the Game of Y and Connections. See [Solver journey‎.md](Solver_journey‎.md "wikilink") and [Fast Rearranger.md](Fast_Rearranger.md "wikilink") for more information about the original hasher. The current hasher differs in that it hashes the board in two phase, first hashing in respect to the primary pieces and then the secondary. Currently the hasher supports the hashing of the game board into a number and unhashing that back to the board. It also supports the data structure required to implement the efficient algorithms of stepping and piece rearrangement.

### Problems / Difficulties

### Next Steps

-   Implement stepping and piece rearrangement for the MMHasher

