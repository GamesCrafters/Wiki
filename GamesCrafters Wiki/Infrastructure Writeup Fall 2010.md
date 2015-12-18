Infrastructure Writeup Fall 2010
================================

Overview
--------

My primary goal was to architect the Gamesman API, the foundational infrastructure to allow future GamesCrafters and potentially third-party developers to integrate our solved databases into their games.

Documentation and Code
----------------------

-   [Design doc](http://goo.gl/2RfxU)
-   The code is in development in a public Git repository: <https://github.com/ide/Gamesman-API>

Miscellaneous
-------------

-   Updated nyc.cs to the Fedora 13
-   Connected Apache httpd to Tomcat; games are accessible at <http://nyc.cs.berkeley.edu/gcweb/>
-   General server maintenance: configured [APC](http://pecl.php.net/package/APC), installed [mod\_pagespeed](http://code.google.com/speed/page-speed/docs/module.html), updated [MediaWiki](http://www.mediawiki.org/wiki/Download) to 1.16.0
-   Opened GamesmanWeb to cross-origin requests with [CORS headers](http://www.w3.org/TR/cors/); proof-of-concept that third parties (including GamesCrafters who want to develop a game locally before deploying to the server) can issue XMLHttpRequests

The Future
----------

Time permitting, I would like to complete v1 of the Gamesman API and its implementation to deploy on Google App Engine. It would also be a good idea to look into the robustness of GamesmanJava's QPS rates, and whether we need to put GamesmanJava databases on App Engine and the actual data on Amazon S3.

Web technologies have incredible momentum and will continue to gain traction, both on the server and client. With big memcaches and multiple API instances on App Engine backed by several GamesmanJava/Gamesman+- replicas, we should be able to serve thousands of queries per second. High scalability is important if our target audience is the world, both in terms of third-party developers and people who play our games.

The client-side scene has evolved even more with the sea of changes as HTML5 lands in the browser. The

<canvas>
element is a more natural way to render games, compared to the DOM-based approach we currently use. All of the major browser vendors, including Microsoft, are releasing HTML5-ready browsers with ever-faster JavaScript interpreters, and they're continuing to improve. Coupled with highly concurrent server applications running on platforms like [node.js](http://nodejs.org/), we can provide real-time play between people on different platforms. A few HTML and CSS touch-ups aside, we can send the same code to Safari on an iPad and Firefox on a PC and let them play against each other in real time.

GamesCrafters' next 10 years is going to be exciting.

— James Ide
