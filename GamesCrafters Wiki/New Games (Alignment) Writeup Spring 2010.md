New Games (Alignment) Writeup Spring 2010
=========================================

### Goal

Since 2001, GamesCrafters has strongly solved existing games--that is, games whose rules were already set in stone by other people or teams. The goal of this project was to introduce the aspect of design to Gamescrafters by developing a game from square one, representing it programmatically, and then computationally solving it.

### Members & Responsibilities

-   **Brent Batas**:
    -   Acted as team lead
    -   Brainstormed ideas (Alignment, Dominion, Spin Connect 4, Lines of Nine, Bridge the Gap)
    -   Wrote game design document presenting game concepts
    -   Playtested all game ideas
    -   Assisted in programming Java representation of Alignment

<!-- -->

-   **Aloni Cohen**:
    -   Brainstormed game ideas (Totem, Shift Connect 4)
    -   Playtested all game ideas
    -   Programmed Java representation of Alignment
    -   Implemented GamesmanJava

### Overview

The team initially brainstormed game concepts and worked together to determine the viability of each as a potential game. If a game was identified as fundamentally flawed in some way, it was removed from the pool. Each remaining game concept was presented as a pair consisting of a board and a set of rules. Both members, along with various volunteers, playtested the games in order to identify flaws. The iterative testing-and-tweaking process continued for two weeks until the game "Alignment," was deemed to be acceptably polished and became the focus of the team. With the rules henceforth determined, the team proceeded to represent Alignment in Java.

### Problems & Bugs

The main problem the team faced was solving Alignment. The GamesmanJava solver could not yet handle [loopy games](http://nyc.cs.berkeley.edu/wiki/index.php?title=Game_Classification_Project#Loopy_games), and because of the numerous available moves to a player, the solver itself would require a large database.

### Final Product

Game Rules (word document) make a wikipage? or attach the doc? Java ? text representation ? Solver things?

### Future Development

`   Short Term`
`       ?`

`   Long Term`
`       Loopy Solver`
`       GUI`
