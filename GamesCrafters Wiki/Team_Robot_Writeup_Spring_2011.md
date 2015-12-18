Team\_Robot\_Writeup\_Spring\_2011
==================================

Overview
--------

For this semester, our goals were to have the robot essentially able to play the game for a Cal Day demonstration.

Software
--------

### Members

-   **Ben Izatt**
    -   Added to the existing Python code to be able to play game/choose settings
    -   Wrote code to communicate with LabVIEW through Python
    -   Added easy/medium/brutal/torture modes
    -   Voiced the robot

<!-- -->

-   **Jimmy Wu**
    -   Wrote LabVIEW code for robot vision
    -   Polished robot for vision
    -   Helped to structure software

### Software Tasks

-   **Robot Vision**
    -   **Objectives**
        -   Take an image of the board with a webcam and convert it to a board string
        -   Pass the resulting string to Python
    -   **Results**
        -   Obtained the necessary NI vision libraries and found the right functions
        -   Wrote code for reading in the corners of the board and the pieces
        -   Used the corners to perform a simple linear transformation and converted results to a string
        -   Wrote the results into a .txt file for the Python code to read (no concurrency problems due to robustness on Python end)

<!-- -->

-   **Communicating with Arduino**
    -   **Objectives**
        -   Deliver the best possible move to the Arduino
        -   Have serial communication working
    -   **Results**
        -   Altered Mark's Python-Arduino library using Standard IO (did not work due to Linux/Windows changes at first)
        -   Fixed a bug with starting up the Arduino and having it drop values due to it resetting each time a port is opened

<!-- -->

-   **Difficulty Settings/Voices**
    -   **Objectives**
        -   Have the robot interact with the player using information such as remoteness/win-lose value
        -   Change whether the computer has givebacks, plays perfectly, or drags the game out and wins
    -   **Results**
        -   Voices were done by Ben with a microphone in quiet room
        -   Originally went with GLaDOS voice from Portal, changed due to irrelevance to Connect 4
        -   Successfully communicated the right messages to taunt the player
        -   Difficulty settings worked in the end
        -   Ultimately, the flow of the code was a large loop reading in input from the LabVIEW code, talking to the server for the right move, telling the Arduino the right move, updating its internal board, then waiting for LabVIEW to give it the next valid board.

### Future

-   Our overall goal was to make sure that the software never crashed and only had minor errors that could be fixed without restarting the code. One issue that still crashes the code is when the server goes down, so we could add robustness to avoid crashing in this case as well.
-   Have vision working even more reliably, especially near the end of the game where there are more pieces to categorize; perhaps find a new algorithm for image processing

Interfacing
-----------

### Members

-   **Albert Wang**

Hardware
--------

### Members

-   **Kyle Lian**
-   **Linsey Hansen**

