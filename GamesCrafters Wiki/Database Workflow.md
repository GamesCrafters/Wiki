Database Workflow
=================

    Workflow pseudocode for the Database:


    The database itself is a module class with the following variables:

    MAP<string,file> files - maps strings to open files
    Array<string> preload - Configurable (how do I do this in Java?) List of popular games (w/ options) that should be pre-loaded
    MAP<string,Array<uint16>> loadeddata - Raw data of pre-loaded games
    MAP<string,int> versions - configurable version numbers of game. We may scrap this (see protocol description below)

    Now inside the module class, we have two methods:

    Constructor() <- When run this will load all games in the preload array into memory
    Loading is basically:
    -load file into memory
    -gzip decompress file
    -Copy file contents into loadeddata

    Gotrequest() <- See below for implementation (this is on a per thread basis)




    We have some commands come in (based off protocol draft):

    Generic header for all requests is:

    <core>
    GCNPP  <- unique protocol identifier tag (5 bytes)
    uint8: COMMAND (see below for numbers) - Just some ASCII number
    uint16: MID -> multiplex ID. Unique identifier for outstanding requests (might scrap this)
    <end core>


    client/server protocol version number (sending packet machine's version) -uint16 : can scrap!
    game being played (ASCII) - game title (from gamesman - kDBName)
    game option (uint32) - game options - (getOption())
    uint16 game version - some internal version number. we *might* want to scrap it, but then version compatibility gets nasty

    The uint* is all encoded in ASCII.


    Upon receiving a request, we sanity check (verify GCNPP is present, verify command is valid, verify protocol version number is correct).   Note:  This should be done in the servlet!

    Implementation of getrequest(string httpdata)
    Received when we get a GET_VALUE_OF_MOVE request
    That looks like:
    uint16 length //size of below
    uint64[length] HASH //hashes of positions:

    The response looks like:
    struct res_pos{
       uint16 rawdata-stream (holds remoteness, value, and MEX)
    }[length]

    Again, all structures in ASCII delimited by commas (can wrap res_pos in some kinda brackets)

    implementation:
    -verify that gametitle is correct version (check versions map<gametitle> == gameversion): error if not
    -String fname = gameversion concatenated with gameoption
      i.e. sprintf(fname, "./data/m%s_%d_memdb.dat.gz", kDBName, getOption()) ;
    Check if loadeddata has entry for fname
      If it does:{
         for HASH
          add rawdata-stream which is array[hash] - in network byte order
       }
       else{
         acquire some sort of thread lock <how to do this in java?> - lock needs to be on on a per-file basis
         check if fname is in files map
            if not: open it then add it!
         error if file not found
         sort (ascending) the hashes
         for sortedHASH{
            gzseek(file,sortedHash) <- gzip seek into file w/ decompression window
            add offset (first 2 bits) to raw-data-stream - in network byte order
        }
        release thread lock
      }
    //fire off response somehow (depends how core servlet is implemented)

    And that's pretty much it!
             
    Complications:
    How to make gameman send multiple hashes per request: This is not trivial and may require hacking up the client in  various places.  But not my problem as the server. :p
    -I'm not entirely sure how to do the per-file lock in java. Matt/Victor? Help me!!


    Optimization:
    We may want to have a master thread wait until we get a request
    Requests no longer manage own seeking but put hashes in a sorted request queue
    master thread seeks through and files that in
    This will not be too hard to pull off after writing initial version

    We may have to add redirection support eventually; This is described in the protocol. We worry about that later.
