GamesmanWeb\_-\_Interface\_SP09
===============================

Overview
--------

-   I created a new index page that lists the available games and puzzles, which previously was a simple and unpolished table.
-   I improved the visual value history graph to make it more visually appealing and easier to read.
-   I improved the interface of Lights Out by replacing characters with images and implementing random board generation.

All of these have been committed to the main Subversion repository and should be available on nyc.cs.berkeley.edu.

Motivation
----------

A main reason for having a web interface to Gamesman is so that anyone in the world can view and access our work in solving and implementing games and puzzles easily and conveniently, without having to download the Gamesman software and compile it, or solve the games. For example, even when we solve the full-size Connect 4 game, the results would not be very useful without some sort of web interface because the database is too large to transport easily all at once. To reach as many people as possible, we need to have a polished, usable, integrated, and visually appealing interface. Unfortunately, as the web interface is still quite new, many aspects that would improve usability and appearance are missing and in need of improvement. Generally, I tried to fill in some of the missing parts and improve what was lacking to deliver a more polished experience to the user.

New index page
--------------

The previous index page simply presented a table of text with internal information not very relevant to the user. While functional in that this page allowed users to access all of the games and puzzles currently in GamesmanWeb, and presumably helpful for development, it presented information unnecessary and unhelpful to most users and was visually unappealing.

The new index page uses a more visually-oriented layout with large images that represent all of the games and puzzles in GamesmanWeb that have been developed to a playable state, with user-friendly names underneath them. As presenting too many games in one row could easily become too wide, it shows only four games or puzzles to the user at once and allows the user to scroll through the list by clicking on the arrows to either side of it. I put an image overlay of a box with shadows inside it so that the scrolling list of games would appear to be inside a 3D cutout, to improve the appearance of scrolling.

The images that represent the games were largely taken from the games themselves. I changed the game listing code and added an entry to the XML file that lists the games and puzzles so that only only ones marked visible would be, since many of the games are still unplayable.

The new page was made using JavaScript (with jQuery) and CSS. While the scrolling functionality requires JavaScript, it was implemented using the principle of progressive enhancement so the page will display all of the games (although in a plain grid) if JavaScript is disabled.

### Future improvements

-   This four-at-a-time model works because there are only about seven playable games and puzzles. It will not scale well as the number of available games increases. If we were to keep the same scrolling design, we would have to separate the list into categories (different lists for games and puzzles, for example).
-   No more information than just a picture and the game/puzzle's name is presented. It might be helpful to have a link for an explanation of the rules, for example.

Some nitpicky things:

-   The logo is not perfectly centered; the middle of the space between the second and third icon is slightly offset from the centerline of the logo.
-   The containing box image with the shadows was actually placed below (using z-index) the list of games, so the shadows are also under the games. When scrolling, the icon actually covers the shadow instead of the shadow covering the icon (and more noticeably) there is no shadow on the yellow background that appears when hovering over a game.

Visual Value History
--------------------

I implemented a new visual value history graph that plots points on a grid that are connected with lines. The old one simply showed blue dots positioned with CSS in a div, which was hard to read.

I used a JavaScript library (called Flot) to implement the new visual value history graph. It handles most of the drawing, although I had to invert the axis labels so that the 0 would be at the top of the graph and not at the bottom.

When you hover over a point, a tooltip displays the value at that point.

### Future improvements

-   Undo support.
-   The implementation is not very modular (but neither was the old graph). It would be nice to move the functionality into the new framework by James.
-   Only linear scale supported.
-   Support for games will have to be added as they are created.

Lights Out
----------

I added the generation of random boards (implemented by simulating clicking on random points on the board). I also changed the Xs (and later multiplication signs) to images that resemble lights.

Future direction
----------------

I think that a high-priority project for the future could be re-designing the game and puzzle page, since it is used many different times and the current one feels inadequate in several ways (a lot of scattered empty space, options reset when a new game begins, etc.). Eventually, GamesmanWeb should probably be integrated into the main web page at <http://gamescrafters.berkeley.edu>, with the game descriptions, although that will require some thought about how much integration would be desirable. Improvements to individual games would also be helpful.
