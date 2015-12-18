GamesmanFramework
=================

Introduction
------------

The Gamesman Framework (GF) would contain all of the libraries necessary for extending Gamesman. Any time one wants to make a module, solver, or otherwise write against an extensibility point in Gamesman, this is where they would start. All base classes and interfaces go here, and it is through the GF that we will be able to specify what it means to be a part of the Gamesman system. The goal in this piece of the system is not to rewrite Gamesman’s functionality, but rather to provide the tools necessary to plug Gamesman’s functionality into the GR.

API Proposals
-------------

It's now time to start fleshing out the API for the Framework, which will allow us to start developing the rest of [Gamesman++.md](GamesmanPlusPlus "wikilink")! Here are some initial thoughts...

### Gamesman++ Primitives

These are the lowest-level parts of the Gamesman Framework. Gamesman applications are composed of these parts, strung together by the Gamesman Runtime.

#### Solvers

#### Modules

##### Positions

##### Moves

#### States
