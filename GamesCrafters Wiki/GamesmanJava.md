GamesmanJava
============

The **Gamesman-Java** Project
-----------------------------

*Experimental port of parts of the Gamesman core to Java, with a focus on Hadoop manycore solving*

### Mission

The Gamesman-Java project exists as a rapid-development testbed for new features. The C codebase is tough to try new features in because of the static nature of C (Swapping out parts requires a good bit of work unrelated to the actual coding - setting up function pointer tables, writing Makefiles, writing "constructors", et. al.) In Java, changes are as simple as subclassing and replacing the functionality desired. Additionally, the Hadoop project allows us to quickly move code from the local machine to a cluster with little headache. Most code written is completely usable without worrying about locking, interprocess communication, or other multiprocessing headaches.

### Current Status

`* Preliminary Hadoop solver completed`
`* Remote database working`
`* Java port of many core Gamesman concepts complete`
`* Local multi-threaded solving for testing working`

### To-Do

`* Track down some correctness bugs`
`* Rewrite remote database code (ugly and needlessly complex)`
`* Develop cross-system database`
`* Solve connect-4 6x7!`
