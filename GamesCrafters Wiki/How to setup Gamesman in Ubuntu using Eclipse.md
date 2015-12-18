How to setup Gamesman in Ubuntu using Eclipse
=============================================

Introduction
------------

This document explains how to run Gamesman under Ubuntu using Eclipse to manage gamesman CVS repository. Although Ubuntu comes with great software already installed, it does not provide the necessary libraries that a developer needs. The following steps are a guide to install the packages that gamesman need to compile and a easy way to have gamesman CVS under the Eclipse IDE. <u>This guide assumes that you already have Ubuntu installed, that you have a basic understanding of the \*nix environment and most importantly you already have your sourceforge account</u>. Although it is possible to execute every command from a terminal i will provide instructions to install packages using the Synaptic package manager.

Step 1 Installing Eclipse, Compilers and libraries
--------------------------------------------------

From the top panel select System-&gt;Administration-&gt;Synaptic Package Manager

-   Install Eclipse:
    -   Select search and type "Eclipse"
    -   find Eclipse and right click on it and select Mark for installation
-   Install autoconf:
    -   Select search and type "autoconf"
    -   find autoconf and right click on it and select Mark for installation
-   Install gcc:
    -   Select search and type "gcc"
    -   find gcc and right click on it and select Mark for installation
    -   lookout! there will be more than one gcc possibilities, you should choose gcc not followed by any number or you will find yourself in trouble when you will try to compile gamseman
-   Install g++:
    -   Select search and type "g++"
    -   find g++ and right click on it and select Mark for installation
    -   lookout! there will be more than one g++ possibilities, you should choose g++ not followed by any number or you will find yourself in trouble when you will try to compile gamseman
-   Install tcl:
    -   Select search and type "tcl"
    -   find tcl and tcl-dev and right click on it and select Mark for installation (current version tcl8.4, tcl8.4-dev)
-   Install tk:
    -   Select search and type "tk"
    -   find tk and tk-dev and right click on it and select Mark for installation (current version tk8.4, tk8.4-dev)
-   Install zlib:
    -   Select search and type "zlib"
    -   find zlib and zlib-dev and right click on it and select Mark for installation (current version zlib8.4, zlib8.4-dev)

Now you have all the necessary packages.
<b>WARNING (choose g++, not g++3.4 or g++\#NUM otherwise you will get this error at compile time make\[1\]: g++: Command not found , if you get this error you can fix it by installing g++ package or if you have g++3.4 by creating a symbolic link g++ to point to g++3.4, the same apply to gcc) for info on how to create a link type in a terminal $ man ln </b>

Step 2 Create and update ssh key
--------------------------------

From the top panel select Applications-&gt;Accesories-&gt;Terminal
type into the terminal:

    user@machine ~
    $ ssh-keygen -b 1024 -t dsa

ubuntu will prompt:

    Generating public/private dsa key pair.
    Enter file in which to save the key (/home/USERNAME/.ssh/id_dsa):

just press enter. choose a passphrase if you want one.

Now we need to update your new key on sourceforge. Connect to sourceforge and login. Click on "My SF.net" from the top menu
click on the link to “Account Options”
click on “\[Edit SSH Keys for Shell/CVS\]”
from the ubuntu top panel select Places-&gt;Home Folder
a window will open. Select View-&gt;Show Hidden Files
look for the .ssh folder and double click on it. double click on `id_dsa.pub` and a window containing your key will appear. Select and copy the key.
go back to the sourceforge page and paste the key into the form.
<b>WARNING! make sure the copied key is all one one line only or it will not work</b>
Click the update button copy the content of the file ~/.ssh/id\_dsa.pub into the form and make sure it is all in one line
click update button

Step 3 configure CVS in Eclipse
-------------------------------

From the top panel select Applications-&gt;Programming-&gt;Eclipse
After Eclipse starts it will ask you where to put the workspace, just click ok and the workspace will be in your home directory.
Now select Window-&gt;Open Perspective-&gt;Other and choose "cvs repository exploring" click on add cvs repository and a window will pop up.
fill Host: `gamescrafters.cvs.sourceforge.net`
fill Path: `/cvsroot/gamescrafters`
user: `sourceforge USERNAME`
and password: `YOURPASSWORD`
connection type:`ext`
under the CVS Repositories TAB it will appera the gamescrafters repository. Select :ext:USERNAME@gamescrafters.cvs.sourceforge.net:/cvsroot/gamescrafters-&gt;HEAD
now right click on gamseman and select "check out"
TADAM you got the gamesman source! Select Window-&gt;Open Perspective-&gt;Other and choose c/c++ and you will see your gamesman folder under c/c++ Projects TAB

Step 4 compile gamesman
-----------------------

Bring up the terminal window and execute this commands in order

    user@machine ~
    $ cd workspace/gamesman

    user@machine ~/workspace/gamesman
    $ autoconf

    user@machine ~/workspace/gamesman
    $ ./configure

    user@machine ~/workspace/gamesman
    $ make

    user@machine ~/workspace/gamesman
    $ cd bin

    user@machine ~/workspace/gamesman/bin
    $ ./XGamesman.new

now you can play tic tac toe!

References
----------

-   <http://gamescrafters.sourceforge.net/developers/cvs-general.html>

