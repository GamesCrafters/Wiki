GamesmanWeb - Fa09
==================

This semester, I ([James Ide.md](Ide "wikilink")) worked alone on my project.

Overview
========

I rewrote the website backend so that our site data, including member profiles and game descriptions, could reside in a standard database like MySQL instead of being in XML flat files. The motivation for this change was to add more structure to the data. For example, some profiles had "Sophomore" for the year they joined while other said "2nd Year" - now both entries just have "2" in their "Year" columns, and the website can choose how to display the data. It is now considerably easier to issue arbitrary queries (e.g., "show me all members who participated some time in 2009") against the data. Member data has been completely ported.

I also developed an interactive interface for updating member profiles. The JavaScript interface sports active form controls; for example, clicking a text field such as a member's name will slide down a text box in which you can make edits. These edits are "live" in that a page refresh does not occur. It was a fun exercise in experimenting with new UIs. I developed the backend PHP library that generates the code for these live form controls.

Finally, I performed some small maintenance on the site with the playable games. Active games are marked with a green light while inactive games have red ones. I updated the main bootloader page, "game.jsp", to dynamically load dynamic scripts: this means that dynamic JSP pages with Java code (as opposed to static HTML pages) can be loaded on the fly even if their page name is unknown until run-time. This enables the Connect 4 page to actively determine which boards have been solved and display a list to the user. The simple and straightforward UI is [online](http://nyc.cs.berkeley.edu:8080/ui/game.jsp?game=connect4).

Big Picture
===========

My work affects only the website. The enhancements mainly affect the backend code and future GamesCrafters who are in charge of add new member profiles.

Maintenance
===========

My website-refresh project was developed from scratch. The PHP libraries and bootstrapper I wrote are all new. Most of the code is solid. I would say that the "core" code is cleanest, with the application-specific code a little more hacky. In general, there's nothing that will make you want to poke your eyes out (obviously a good measure of code quality), although some of the SQL queries could be optimized. The code base is organized and I have a penchant for reasonably clean code so things should be fine in that department. The website code resides on gamers@ocf.berkeley.edu.

The changes to the site with the playable games have been committed to the SourceForge Subversion repository. They are also live on [<http://nyc.cs.berkeley.edu:8080>](http://nyc.cs.berkeley.edu:8080).

Future
======

Look into changing web server hosts. When OCF re-compiled their PHP binary at the end of November (a half hour before my presentation, according to their configuration page -\_-), they broke the PDO driver that provides PDO (a standard database abstraction layer) access to the MySQL backend. (See [OCF's PHP Configuration](http://gamescrafters.berkeley.edu/phpinfo.php).) I requested that they fix it; they recompiled the binary with some options changed but PDO is still not enabled, and researching the symptoms doesn't yield any fixes. I really don't know how they managed to screw it up.

Inst's web servers are slightly better but still not desirable. For one, they don't provide PDO connectivity to MySQL ([Inst's PHP Configuration](http://inst.eecs.berkeley.edu/~gamers/phpinfo.php)) and also "chmod o+r" needs to be run on every file uploaded to the server due to how Inst has set up their web server.

Building a caching layer would help as well. Using a PHP bytecode cache like [APC](http://pecl.php.net/package/APC) would speed up page-generation time in general. Depending on the time it takes to format ~250 member profiles, it may be worthwhile to start caching member data or generated HTML snippets -- I haven't done any profiling so I'm not sure which should be done.

A future GamesCrafter who wishes to continue the website work should be well-versed in PHP and know basic MySQL. No knowledge of database internals is required.

Work on the playable-game site requires knowledge of JSP. We don't use any advanced features, so I have confidence that a smart programmer who can write clean Java and HTML will be able to learn enough quickly.
