GamesMan\_Java\_-\_UIModule\_Writeup\_SP09\_(by\_Wesley\_Hart\_&\_Jin-Su\_Oh)
=============================================================================

(Working on it)

Overview
========

Because GamesmanJava lacked any user interaction, we made a simple object-oriented text user interface. It's object-oriented in that it involves different modules like a solve module, database module, etc. that all inherit from a UIModule class. Using Java reflection, coders just have to write functions in these modules that begin with "u\_" and the interface will automatically allow users to use these functions. Essentially, we split up the work by having Wesley work on the abstract classes like UIModule and GamesmanShell and Jin-Su working on the module classes.

The interface is controlled by a main class named GamesmanShell that passes user commands to whatever the current module is, with each module operating based on inherited methods from UIModule. A module is basically a collection of user-callable methods and any data important to its operation.

The enire user interface also relies heavily on GamesmanJava's Configuration objects. Configuration objects store a collection of GamesmanJava information for a specific game, such as a solver type, database type, where a database file is located, which module should be defaulted to, and so on. The interface provides a way of loading and modifying these Configuration objects and using them to access databases and solve games.

GamesmanShell
=============

The main entrance point to GamesmanJava System.

Testing
-------

Picking up
----------

UIModule
========

Mother of all User Modules that have been implemented and will be implemented.

Testing
-------

Picking up
----------

ConfigurationModule
===================

This is an interface that allows the users to create, load, save and edit the configuration file. Configuration file holds multiple configurations that are differentiated by a configuration's title. When a new configuration is created, it is appended at the end of the existing list of configurations.

Testing
-------

We have been testing it by trying many different input combinations into the functions and manually checking the configuration file.

Picking Up
----------

Creating a new configuration can be more friendly to users.

Database Module
===============

This is an interface that allows the users to open, close, see, and edit the solved Database for a game. As of now there are four functions implemented : open, close, see, and edit. The database comes from what uri the configuration specifies.

Testing
-------

The functions implemented so far have been tested thoroughly and can be assumed to be fully working. Testings were done just by manually comparing what should be there and what the function showed.

Picking Up
----------

These four functions implemented are very primitive functions and another person can start coding more robust functions. i.e. converting the entire database into human-readable form and put it somewhere so that a person can easily open it up and see it. It would also be nice if you can clean up some nearly useless methods I put in there to make the module working, like, u\_initializeConfiguration and isParsableBoolean functions.

Solver Module
=============

This is an interface that allows the users to make GamesmanJava System to do any work that involves solving a game. Currently there is only one function that solves the game. Specification of solving come from the configuration.

Testing
-------

Not tested because the code just calls another function in a different class.

Picking Up
----------

Not sure what more can be done with solving.
