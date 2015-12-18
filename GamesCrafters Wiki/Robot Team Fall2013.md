Robot Team Fall2013
===================

Overview
========

Given difficulties with previous semesters' efforts to build a robot that would play on the standard Hasbro Connect 4 board, this iteration created its own representation of the board. This semester was focused on creating a working board that could run independently in a closed system and would only require player input through a keypad or a similar device.

Components
==========

Binary Sorter
-------------

Color Sensor
------------

![alt text.md](Color sensor Spr13.png "alt text.md")

Ball Selector
-------------

Insipired by <https://www.youtube.com/watch?v=t0Ls-x26tWU#t=25s> The ball selector solves the problem of feeding a single ball to the color sensor at a time. The final design uses servos mounted on the side of an inclined track on either side of the color sensor. A horizontal arm with a length slightly less than the width of the track is mounted on each servo. The width of the servo arm material should be under ~1/4" (or a reasonable width to rotate down and separate two adjacent ping pong balls. The two servos rotate asynchronously as shown in the video to select balls. In general both servos begin in the down position (blocking the track). The first servo will lift up to release a ball from the stream and then rotate back down to block the others. Next, after the color has been detected the second servo will rotate up to release the ball and then back down. This process repeats for every move until the correct color ball is found.

The arduino servo library can be used to write the appropriate angle values to the servos:

Prototype demo: <https://docs.google.com/file/d/0B4VrW5BWiw25UjF5VWpFZjNOcUE/edit?usp=sharing>

Board Releaser
--------------

Ramp
----

Ball Bin
--------

Ball Lift
---------
