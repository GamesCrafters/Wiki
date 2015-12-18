Image Input for Rubik's Cube
============================

Team Member 1: Swapnil Ralhan

Team Member 2: Veer Bawa

Our project intends to create new methods of input for solving the Rubik's cube, as an alternative to the existing direct color input method. The new input will be a photo taken of the sides of the Rubik's cube (with plans to expand functionality to take video as input), similar to the CubeCheater App ([1](http://www.youtube.com/watch?v=HNwx0nbgm7M)) on the iPhone. The image-recognition algorithm takes a picture of the rubik's cube and then runs it through a few steps to find the colored stickers:

1. Camera noise is reduced, using a Guassian blur to smooth out the image a little. (http://en.wikipedia.org/wiki/Gaussian\_blur)

2. A Sobel Operator is used to do edge-detection on the image (http://en.wikipedia.org/wiki/Sobel\_operator)

3. Contiguous regions of color within the cube (the squares) are isolated, using blob detection (http://en.wikipedia.org/wiki/Blob\_detection)

4. All the blobs are scored according to how close they are to squares in a rubik's cube "grid" and the 9 highest scoring blobs are detected.

All research and coding was done collaboratively by both partners. The Code is still in the process of being written. Since this project is a two-semester project, the first phase primarily involved researching, planning, and writing a working version of the code. Improving the quality and readability of the code is an aspect that will take focus in the second half of the project (next semester).

`   Plans for the future involve adding functionality to handle video inputs, and customizing code for platforms like the iPhone and the Android (where this would be most useful).  Plans also include adding an overlay over the camera image to center the picture and make the algorithm's work easier.`
