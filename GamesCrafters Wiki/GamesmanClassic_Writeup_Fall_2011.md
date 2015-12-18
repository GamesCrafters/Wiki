GamesmanClassic\_Writeup\_Fall\_2011
====================================

Project Overview
----------------

### Goals

There were two primary goals for the project this semester. The first was a major overhaul of the UI/UX of the application, developing a much cleaner experience and application flow. The second was an equally major revision to the underlying API that each game must fulfill to run in the iGamesman system.

### Members/Tasks

-   **Kevin Jorgensen** acted as team lead and was responsible for the redesign of the application's UI and the new definition of the game API.
-   **Ian Ackerman** ported the game Connections from the old system to the new API.
-   **Jordan Salter** ported the game Connect-4 from the old system to the new API.
-   **Luca Weihs** ported the game Othello from the old system to the new API.

Change Description
------------------

### iGamesman Core

-   Created a new Xcode project compatible with Xcode 4 and iOS 5; tidied up odds-and-ends (e.g., the GamesCrafters splash screen is no longer upside-down relative to the default landscape mode).
-   Kevin: describe changes to the core here.

### Connections

-   Transferred over previous Connections code, adapted to the new API.
-   Changed GUI to scale to iPad as well as to landscape view from the previous portrait.

### Connect-4

-   Updated internal data structures (e.g., factored out a GCConnectFourPosition object) and method calls to conform to the new API
-   Updated hard-coded dimensions in layout code, so Connect-4 now scales to iPad

### Othello

Luca: describe the work you did on Othello here.

Problems/Bugs
-------------

### iGamesman Core

Kevin: bugs in core?

### Connections

-   Encircling code not functioning correctly
-   Network API untested

### Connect-4

-   Server play isn't yet supported by the new API and hasn't been tested.

### Othello

Luca: bugs in Othello?

Next Steps/Future Plans
-----------------------

### Connections

-   Look at old GamesmanMobile code-base to see configurations of options for unimplemented options view.
-   Connections internet access capabilities were never confirmed due to not being in database, however the code from GamesmanMobile for it is there.

### Connect-4

-   The current UI design is "board | message". This looks cramped on iPhone now that the game view area is smaller; a graphical status indicator would fit and look better. The status label should be moved below the board on large displays (eg, iPad).
-   The current assets don't scale to iPad and are a bit two-dimensional -- it would be nice to have shiny new graphics.
-   The Connect-4 game package doesn't export options or VVH views.

