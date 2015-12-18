Database
========

Databases are an integral part of Gamesman. They allow for the data retrieved from solving a game to be stored, accessed at a later time, and transferred.

Current Databases
-----------------

There are several databases implemented in Gamesman. They range in functionality and are often tailored for specific purposes.

-   [Bit-Perfect\_DB.md](Bit-Perfect_DB.md "wikilink")
-   [File\_DB.md](File_DB.md "wikilink")
-   [Mem\_DB.md](Mem_DB.md "wikilink")
-   [Two-bit\_DB.md](Two-bit_DB.md "wikilink")
-   [Univ\_DB.md](Univ_DB.md "wikilink")
-   [Collision\_DB.md](Collision_DB.md "wikilink")

Old API
-------

All databases in Gamesman conform to an API specified in db.h.

    typedef struct DB {

        /* for Database authors: */

        /* These 7 functions need to be reduced to the 2 that are specified
           in the DB Class. Like this for ease of implementation/switchover
           a single get and put is really all we need.
           - last words of Scott that are not necessarily true anymore*/

        /* here are the things that ARE true:*/

        /* all these 12 functions may assume the completion of any error-checking
           for their parameters */

        /* for functions that return a BOOLEAN, make it TRUE if the operation succeeds,
           FALSE otherwise
           for functions that return a VALUE, undecided means failure
           for functions that return a REMOTENESS, kBadRemoteness means failure
           for functions that return a MEX, kBadMexValue means failure
           for the write operations to be successful, these functions are required to
           return whatever is IN ITS DB DATA STRUCTURE (ARRAY, ETC.) for comparison */

        /* for a DB to be useful you have to implement at least the value-related functions*/
        /* if gamesman does not see those two available it will exit right away.
           For the other function it will simply return a bad value or do nothing */
        /* if gamesman sees an error during range-checking, it will exit. This happens
           even when, for example, the cannonical sibling of a position is within range,
           but the position itself is not. */

        void        (*free_db)          ();

        VALUE   (*get_value)        (POSITION pos);
        VALUE   (*put_value)        (POSITION pos, VALUE val);
        VALUE   (*original_put_value) (POSITION pos, VALUE val);

        REMOTENESS  (*get_remoteness)   (POSITION pos);
        void    (*put_remoteness)   (POSITION pos, REMOTENESS val);

        BOOLEAN     (*check_visited)    (POSITION pos);
        void    (*mark_visited)     (POSITION pos);
        void        (*unmark_visited)   (POSITION pos);

        MEX     (*get_mex)      (POSITION pos);
        void    (*put_mex)      (POSITION pos, MEX mex);

        BOOLEAN (*save_database)    ();
        BOOLEAN (*load_database)    ();

        // bpdb
        UINT64      (*get_slice_slot)   (UINT64 position, UINT8 index);
        UINT64      (*set_slice_slot)   (UINT64 position, UINT8 index, UINT64 value);
        GMSTATUS    (*add_slot)         (UINT8 size, char *name, BOOLEAN write, BOOLEAN adjust, UINT32 *slotindex);
        GMSTATUS    (*allocate)         ();
        
        void    (*get_bulk)     (POSITION* positions, VALUE* ValueArray, REMOTENESS* remotenessArray, int length); 

    } DB_Table;
