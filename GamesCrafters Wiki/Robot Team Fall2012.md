Robot Team Fall2012
===================

Overview
--------

Last semester, we built a robot that could play Connect4 but it relied on humans to reset the board, dispense pieces, and calibrate the vision system. Our goal this semester is to design a robot that can play Connect4 perfectly without human intervention.

Members
-------

-   Kyle Lian
-   Ben Izatt
-   Kevin Shih
-   Lily Lin

Hardware
--------

![](Schematic.png.md "Schematic.png.md")

This is our current design for the hardware side of the robot. We have divided the robot up into five main components: Ball Selector (red), Ball Sorter (green), Connect4 Board (blue), Ball Collector (purple), and Elevator System (orange). Each of these components will be controlled by an Arduino (see software section for details). The entire robot with the exception of the elevator system will be sandwiched between two pieces of plexiglass (50mm apart) to provide structural support. We will connect the elevator system with the rest of the robot using PVC pipes.

### Ball Selector

The ball selector consists of an ramp, a ball sensor, and a latch at the end of the ramp. The ball sensor can be implemented as two photo-resistors with one blue LED light at the top of the elevator system. The ball sensor will check 1) whether there is a ball at the top of the elevator and 2) the color of the ball. This data will be used by the Arduino to control the robot.

### Ball Sorter

The ball sorter is made up of 7 latches, 1 for the first level, 2 for the second level, and 4 for the third level. The latches perform a binary sort for 8 positions : 7 board columns + 1 extra column for balls with the wrong color.

### Connect4 Board

The Connect4 board is a rectangular box with eight columns. We plan to give each 40mm ping pong ball 10 mm of clearance, bringing the total width of each column to 50 mm. This puts the dimensions of the board at 400mm wide x 240mm high x 50 mm thick. The bottom of the board will be blocked by a rod connected to a servo. When the game is reset, the rod will swivel to the side allowing the balls to fall into the ball collector. If there is extra time, we plan to put an 8x8 LED array behind the board to display move values and provide a backlight.

### Ball Collector

The ball collector is a ramp that will funnel the balls into the intake of the elevator system. It should be able to handle up to 42 balls at a time. We plan to mount one or two vibration motors underneath the ramp in order to prevent balls from getting stuck. Example of a vibraton motor that could be used for this: 325-100-24mm-vibration-motor-31mm-type.

### Elevator System

The elevator system is located to the left of the board. It takes balls from the ball collector and moves them up to the ball selector using an internal Archimedes screw. The elevator system will be powered by a motor at the bottom oriented in the vertical direction. Right now our plan is to carve out the Archimedes screw from a foam pool noodle and use a PVC pipe as the exterior.

Software
--------

We plan to control our hardware using an ARDUINO MEGA 2560. The Arduino will receive 2 bits of data from the ball selector - whether a ball is present and the color of the ball if it is there. If there is no ball, the Arduino will turn on the elevator system until a ball enters the piece selector. Once a ball arrives at the piece collector, the Arduino will check the color of the ball. If the ball is the correct color, the Arduino will set the ball sorter latches to the proper configuration and open the ball selector latch allowing the ball to fall into the correct column. Otherwise, the Arduino will send the ball into the 8th column where it will fall into the ball collector.

We plan to use Raspberry-Pi to communicate with the nyc server and handle user inputs.

Display Case
------------

![](351soda.png.md "351soda.png.md")

![](351soda2.png.md "351soda2.png.md")

Current Progress
----------------

We have a working prototype of the ball sorter and working code to communicate with the nyc server.
