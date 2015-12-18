Robot\_Team\_Writeup\_Spring\_2012
==================================

Overview
--------

This semester, the robot team (mostly veterans from last year) started on a new robot concept using the same theoretical framework, implemented with a robust commercial, 2 degrees of freedom robotic arm. Ultimately a first prototype and proof of concepts for all components were provided. Polishing and fine tuning to allow for autonomous function and robust function is necessary in the future.

Software
--------

The primary software (server contact, running the robot, and playing the game itself) is written in Java. The visual analysis work is written in Labview (and has not been editing since Spring of 2011).

### Members

-   **Ben Izatt**
    -   Java framework
        -   Robot Communication and control
        -   Server contact and string interpretation
        -   Robot gameplay program supporting PvP, PvC, CvP, CvC (all combinations of robot v player with either starting first)

<!-- -->

-   **Albert Wang**
    -   Vision

<!-- -->

-   **Kevin Shih**
    -   Vision

### Software Tasks

-   **Communicating with Server**
    -   **Objectives**
        -   Retrieve list of possible moves from server
        -   Pick the best possible move from the list
    -   **Results**
        -   Built off framework of Python code from previous year.
        -   Takes a board string, adds it to URL, converts " " to "%20", sends to server
        -   String parsing is less elegant in Java -- lots of creative use of substring. Assumes server response format will not be changed.

<!-- -->

-   **Communicating with Arduino**
    -   **Objectives**
        -   Best way to control the gripper.
        -   Theory is sound, has not yet been implemented

<!-- -->

-   **Board Vision**
    -   **Objectives**
        -   Maintain an internal "state" of the board in the code
        -   Convert state into board to communicate to the server
    -   **Results**
        -   Use last semester's software written by Jimmy Wu.
        -   Add depth data from Kinect to get more robust results.

### Future

-   Tie together components under Java control (gripper, vision).
-   Fine tune arm motion, explore Pierre's algorithms and program to make this more elegant and simple.
-   Explore better methods of string interpretation in Java.

Hardware
--------

FROM HERE ON IS JUST LAST YEAR's CONTENT! For hardware, we mostly focused on the various design possibilities. We started out by looking at existing connect 4 and other game-playing robots, and from there listed the our possible design options. After 2 different phases of prototyping, we settled on our final design.

### Members

-   **Kyle Lian**
-   **Linsey Hansen**

### Design

![A\_placeholder.md](FinalDesign.png "A_placeholder.md")

-   **Strengths:**
    -   Simple to implement
    -   Only requires 3 motors
    -   Allows the robot to use both colors without human interference (aside from reloading dispensers)
-   **Weaknesses:**
    -   Keeping the slab on the tracks might be tricky

### Components

#### Piece Placement

We will use a piece of wood and/or poster board with a ramp routed into it. This board will move back and forth on wheels along a rail so that the bottom of the ramp is aligned with the appropriate slot for a move. In order to make a move, a piece then just needs to be dropped down onto the top of the board, where it will roll down the ramp and into the proper slot. This will be controlled with 1 stepper motor.

#### Piece Dispenser

There will be two piece dispensers, one for each color. Each dispenser will be controlled by one motor, and we will either have a horizontal dispenser with a gumball-machine like mechanism and a spring, or a vertical dispenser with a spherical gumball-machine like mechanism.

#### Viewing the Board

We are still debating whether we will be using a webcam or sensors. A webcam will be more difficult to properly implement software-wise, and sensors will cost more and be more difficult to properly implement hardware wise.

#### User Interaction

In order to begin a game, the user will need to choose their color based on some control box. If we add in different play styles, such as robot vs robot or having the robot finish an in-progress game, these will also be added to the box. There will be a red light and a blue light on the box, so that when red wins, the red light lights up, and when blue wins, the blue light lights up, if it is a tie, both lights will light up. In theory we could also just implement this as a program on a computer in the event that the robot will be connected to a computer anyways.

Goals for Next Semester
-----------------------

-   Get vision working
    -   We still need to decide between sensors and a webcam depending on the software team's input
-   Build the actual robot
    -   We will probably use at least 2 iterations
-   Enable Human vs. Robot Play
-   Enable Robot vs. Robot Play
-   Go from Human to Robot Play

