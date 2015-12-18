Template:CL GamesmanClassic GamePage
====================================

Checklist
=========

From the [C Text Game Checklist.md](C_Text_Game_Checklist.md "wikilink"):

[1.md](#1 "wikilink"). Help strings that change with variant

[2.md](#2 "wikilink"). debug turned off (no printf output), no warnings

[3.md](#3 "wikilink"). GS variants in nice clean menu

[4.md](#4 "wikilink"). NO memory leaks (like calling GenerateMoves and not calling FreeMoveList afterwards)

[5.md](#5 "wikilink"). printPosition handles predictions/whose turn

[6.md](#6 "wikilink"). getoption, setoption, and perfectly packed option list (1-based) LET'S FIX THIS TO BE 0-BASED!!

[7.md](#7 "wikilink"). put it in the Makefile

[8.md](#8 "wikilink"). Clean/Commented Code

[9.md](#9 "wikilink"). implement MoveToString() NEED DOC

[10.md](#10 "wikilink"). Call the common functions from the Game function libraries instead of coding duplicate functions on your own NEED DOC

[11.md](#11 "wikilink"). Docs

[12.md](#12 "wikilink"). Symmetries (optional?) NEED DOC

[13.md](#13 "wikilink"). GPS (optional?) NEED DOC

From the [GUI Game Checklist.md](GUI_Game_Checklist.md "wikilink"):

[14.md](#14 "wikilink"). Remove commented out dead code

[15.md](#15 "wikilink"). Doc your code with comments

[16.md](#16 "wikilink"). Do not change canvas size

[17.md](#17 "wikilink"). Don't hardcode your size parameter (board should be able to grow)

[18.md](#18 "wikilink"). All available animation within reason (including adhering to the 'animation speed' slider)

[19.md](#19 "wikilink"). Conforms to all C game variants

[20.md](#20 "wikilink"). No puts (print statements)

[21.md](#21 "wikilink"). Move strings change when rules change

Checklist Progress
==================

1
-

### Help strings that change with variant

2
-

### Debug turned off (no printf output), no warnings

3
-

### GS variants in nice clean menu

4
-

### NO memory leaks (like calling GenerateMoves and not calling FreeMoveList afterwards)

5
-

### printPosition handles predictions/whose turn

6
-

### getoption, setoption, and perfectly packed option list (1-based) \[LET'S FIX THIS TO BE 0-BASED!!\]

7
-

### Put it in the Makefile

8
-

### Clean/Commented Code

9
-

### Implement MoveToString()

10
--

### Call the common functions from the Game function libraries instead of coding duplicate functions on your own

11
--

### Docs

12
--

### Symmetries (optional?)

13
--

### GPS (optional?)

14
--

### Remove commented out dead code

15
--

### Doc your code with comments

16
--

### Do not change canvas size

17
--

### Don't hardcode your size parameter (board should be able to grow)

18
--

### All available animation within reason (including adhering to the 'animation speed' slider)

19
--

### Conforms to all C game variants

20
--

### No puts (print statements)

21
--

### Move strings change when rules change


