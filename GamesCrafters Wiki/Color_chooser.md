Color\_chooser
==============

About the Project \[edit\] Goal

The goal of this project is to provide an user interface that enable user to set a Rubik's cube state fast and easy.

\[edit \]Overview

`         o Then user manually input the state.`
`         o Key stroke 'a', 's', 'd', 'f', 'j', 'k','l',';' each represent a possible cube corner accordingly.`
`         o Press they key will put the corner to the current corner position, which is flashing.`
`         o Press the same key multiple times will rotate the corner counter clock wise.`
`         o Once the desired corner position is there, press SPACE or BACKSPACE to move the flash to the next or the previous cube corner.`
`         o If 7 out of 8 pieces are chosen, the program will automatically pick the 8th piece for the user and end the color choosing process.`
`         o A new view angel called "corner view" is supported, easy for user to choose corner.`
`   `

\[edit\] View Hierarchy The feature is mostly implemented in CornerChooser.java, also some small changes in Cuboid, PuzzleCanvas, GamesCubeMan. To avoid redundant pieces appear in a cube, many HashMaps are needed to keep track the state. StickerColor stores all colors and manipulates the corner combinations. colorRectangles uses StickerColor to produce the sticker piece. cornermap matches key strokes to corner, and dupcheck stores all chosen corners and avoid redundancy. After a corner is chosen, its index icon will be darken to remind user.

\[edit\] Next Steps/Future Plans

`   * Support cubes in any dimentions`
`         o Cubical (NxNxN), and rectangular(LxWxH)`
`   * Animation `
`         o Paint corner gradually.`
