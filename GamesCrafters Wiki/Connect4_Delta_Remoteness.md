Connect4\_Delta\_Remoteness
===========================

Project Member
--------------

Leland Au, Tom Lai

Overview
--------

We have modified the green and red color in the delta remoteness as discussed before. We have also added transparency level to the green and red to reflect the remoteness of the individual winning or losing move. The winning moves are separated to four groups according to their remoteness (1. the fastest 2. the second fastest 3. the third fastest 4. the rest) and given different transparency level accordingly as discussed. The losing moves are also separated to four groups (1. the fastest move to lose 2. the second fastest move to lose 3. the third fastest move to lose 4. the rest) and given transparency accordingly.

How is the transparency level applied
-------------------------------------

The transparency level in the shade below the block is applied by displaying different pre rendered images. The transparency level in the block is applied by creating different classes of objects which will render into images of different transparency according to the description of that class in ui/game/styles/connect4.css
