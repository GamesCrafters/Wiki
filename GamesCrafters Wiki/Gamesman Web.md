Gamesman Web
============

*Gamesman Web* is an effort to introduce client software for Gamesman using Web technologies such as HTTP and JavaScript. The project is split into two main tiers: the server, which provides bindings to the Gamesman engine; and the client, which renders game interfaces with HTML/CSS and enables user interaction with JavaScript.

Rationale
---------

Our long term goal is to be able to phase out Tcl/Tk as the presentation layer and instead move to JavaScript/AJAX. This will allow for richer games (alpha blending) and the ability to work on nearly every computer. We will be targeting WebKit (Safari rendering engine) and eventually integrate WebKit into the Gamesman client itself. The benefit of this is that, theoretically, game interfaces need to be written just once to run both locally and in a Web browser.

Server Architecture
-------------------

The server handles client requests regarding game data; i.e., the AI opponent's moves and move analysis information (win, tie, loss). If possible, the server should provide a RESTful interface. REST is a series of principles that ask for a stateless interface: one that is independent of user sessions. This facilitates both server and client development, including sub-processes such as caching.

The server exposes several of the functions of Gamesman. Most notably, remote clients will be able to query for an AI opponent's move, move history analysis, etc.

Client Development
------------------

The client code is designed to run in Web browsers that support HTML, CSS, SVG, PNG, and JavaScript. These technologies will comprise the user interface to provide a rich game-playing experience. An added bonus is that new skins can be easily and quickly produced by rewriting the CSS code and providing new images. To include Web Gamesman in the local executable version of Gamesman, a Web rendering engine can be embedded in the client software.

The game logic (rules) will be programmed in the client JavaScript code.

Client-Server Communication
---------------------------

The XMLHttpRequest API (a key component of AJAX) allows JavaScript to make HTTP requests to the server without refreshing a Web page. With AJAX, Web Gamesman can achieve a level of responsiveness close to that of the current Tcl/Tk interface. When the user triggers some action, the client will send an HTTP request to the server and listen for a response. During this listening period, which is anticipated to be brief, a small loading indicator may appear. Once the server response has been received, the client will parse the data and update the interface as deemed appropriate.

Tier Diagram
------------

The server tier is composed of the AI and API sections, while the Networking and Frontend sections make up the client tier.

![](gamesman-web-tiers.png.md "gamesman-web-tiers.png.md")
