GamesmanJava Writeup
====================

So here's the status of GamesmanJava:

**Core** is in pretty good shape. Everything builds and the class hierarchy is somewhat sane. **Packaging** needs some work. It would be nice if we could send everything off in a single .jar file and it have everything work. As of right now, if you build it from source everything is fairly intuitive. Here's a vague layout of the repository:

-   bin/
    -   Built binaries. A clean checkout should be empty.
-   build.xml
    -   Ant buildscript. Needs some love - we use Eclipse for the build system but ant is more useful for headless builds
-   doc
    -   Javadoc. Rebuild it as you need to; it's just there as a convenient location to access the files (so you have a reasonably up-to-date copy with every checkout)
-   externals
    -   org.json
        -   JSON parser/builder used to communicate with GamesmanWeb
-   gamesman-java.conf
    -   Main configuration file used with Wesley and Jin-su's configuration stuff
-   gamesman-java.jardesc
    -   File Eclipse uses to build a .jar file
-   jobs
    -   Legacy jobs that should be imported to the configuration module
-   junk
    -   Staging area for testing/misc code
-   jython\_lib
    -   Jython library files
-   lib
    -   Useful jar files. These must be on the classpath for various things to run. Replace with updated versions as needed.
-   src
    -   The source tree

