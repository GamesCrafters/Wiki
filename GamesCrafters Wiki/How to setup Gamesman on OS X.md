How to setup Gamesman on OS X
=============================

Compiling and Running GamesmanClassic on OS X (Lion)
----------------------------------------------------

Type the following set of commands in order to compile and run Gamesman.

    sudo port install tcl tk  # don't have MacPorts?  get it from macports.org
    svn co https://gamescrafters.svn.sourceforge.net/svnroot/gamescrafters/GamesmanClassic/ GamesmanClassic
    cd GamesmanClassic/trunk
    sed -e 's/-mpowerpc//g' -i.bak configure.ac
    autoconf
    ./configure --with-tcl=/opt/local/lib/tclConfig.sh --with-tk=/opt/local/lib/tkConfig.sh
    make
