Hadoop Tier Solver Writeup Fall 2010
====================================

Motivation
----------

The current GamesmanJava Tier solver is effective at solving many of the games that we have encountered so far. However, it has a few shortcomings that a Hadoop Tier solver would be effective at overcoming. First, the GamesmanJava tier solver does not handle crashes on a particular node very well. Depending on the situation, if a single node crashes during a solve, the solve would have to restart at the last checkpoint on the given tier. On the other hand, Hadoop handles node failures automatically and will be able to redistribute work on the remaining nodes without having to interrupt solves going on in the other nodes. Another short-coming of the current tier solver is that it is not scalable. We are limited by the iCluster right now and if a solve takes up more room than available (such as Atari-Go), then we must add more resources to finish the solve. The best way to gain access to more resources is to use something like the Amazon Cloud to do our solve on, which requires Hadoop compatibility. These benefits will offset the fact that a Hadoop Tier Solver will work slightly slower than the current Gamesman Tier Solver.

Implementation
--------------

To make the current tier solver compatible with Hadoop, we first had to write a master that would take each tier of a game, split them up into segments and feed them to a mapper on a particular node. We iterate through all the tiers this way until we are done. For the mapper, it needs to take a Range passed to it from the Master and solve that range, writing the solved records into a local file. For all but the last tier, this requires the mapper to read from the HDFS database (created in the reducer) to see the values of child positions. When the read and write databases are set up, we can then begin to solve the range by creating a workunit and calling its conquer methods just as GamesmanJava does. Finally, the reducer will take all the separate local solves, merge them into one, and write it all out to HDFS.

Obstacles
---------

There were many challenges to this project. First, we had to understand the Hadoop Map-Reduce API and the mapreduce algorithm behind it. In addition to that, we had to understand how GamesmanJava sets up and executes solves. In fact one of the main confusions and changes made due to our project was to get rid of the GamesmanConf wrapper that included a Hadoop Configuration object since the Hadoop framework did not recognize it as a Hadoop Configuration even though it contained a Hadoop Configuration. Instead, we pass around only a Hadoop Configuration object and serialize a Gamesman Configuration inside that so we can pass around the information we need. Thankfully, with a lot of debugging and help from David, we were able to get past many of these bugs.

Results
-------

Unfortunately, we have not gotten it to run successfuly yet. While the main code for the Hadoop Map-Reduce set up has been completed and debugged, the current databases to support HDFS have not. However, even with this, we have made significant headway into making a stable and scalable solver that will be able to run on the Amazon Cloud. In fact, as soon as the database code is finished, this should be able to solve any game that conforms to the GamesmanJava API.

Next Steps
----------

Clearly, the next step in the project is to get the HDFS databases working. There are a couple of methods that need to be checked for correctness. However, this is extremely hard to debug since Hadoop will not stop until the next tier when it tries to read from the HDFS database so we do not see where exactly the error will be. But after being able to read and write from the database correctly, the Hadoop Tier Solver will be pretty much done.
