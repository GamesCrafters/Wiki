Augmented\_Reality\_Gamesman:\_Connect\_4
=========================================

Members: Elizabeth Izatt

Project Description:

-   Prototype of a real-time augmented reality system for overlay of Gamescrafters interface on camera feed of an unmodified commercial Connect 4 board.

Demonstration Video:

-   <to add>

Usage:

-   Connect to internet and camera, and start Python app. Arrange camera and board so that board is within the rectangle drawn on the camera feed.
-   When the board is found, standard Gamescrafters interface (guide circles above the board in red, yellow, and green) will overlay.
-   If getting bad results, take a picture of the board with webcam software and manually create templates (red, black, and empty) to replace the ones found in the templates subfolder.

Features:

-   UI-guided finding of game board
-   Automated k-means clustering based location of board pieces
-   Automated template-matching for identification of piece color.
-   Server access and overlay generation.

Dependencies:

-   Python OpenCV

To Do:

-   Delta remoteness on colors.
-   Averaging piece location over several frames (more robust measurement).
-   UI for tuning board selection size (or preferably automated system for finding board)

