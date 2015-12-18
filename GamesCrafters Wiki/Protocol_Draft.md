Protocol\_Draft
===============

Below is the BETA Procol draft. Does not cover full thin client Only covers details about database querying and merging

Headline text
-------------

Ideas -download database? we can do this, but too much server load -save/load databases? (memdc.c) : data bases need game version data! (modify memdb + increment version) -throw in redirection of databases -be sure to browse server -sub protocol server -also note theoretically has direct parsing - must spit back rules -must implement cheating stuff -optional password to join -spectating ability!

Headline text
-------------

Protocol description:

Client is responsible for generating legal moves and understanding game client simply lacks solution database; the server does that! client applies board and produces hash -gets hash back, so can directly make board

Headline text
-------------

protocol details:

synopsis: This is the generic level protocol

Headline text
-------------

Core Details: GENERAL: -client issues request with some COMMAND; server responses with same OR different command VERSION HANDLING: client will send packet. server responds with ERROR\_VERSION if version&gt;current version. server sets max version number in own packet server client then must use that number; else error occurs

Headline text
-------------

CORE UNIVERSAL HEADER (all inheret from this) All below is given in order:

&gt;length (uint16): entire packet length not including this byte &gt;GCNPP &lt;- unique protocol identifier tag (5 bytes) &gt;uint8: subprotocol number (0=core; 1=stateless client thing; 2=P2P pure; 3=serverforward P2P) //do we want this? commands are enough &gt;uint8: COMMAND (see below for numbers) &gt;uint8: bit flags (bit 0 = 0?:request:response; others reserved) &gt;uint16: MID -&gt; multiplex ID. Unique identifier for outstanding requests (a bit redundant to tcp/ip but easier to manage) (entire header now 12 bytes) same with request and response

CORE COMMANDS (0x0-0x19): COMMMANDS:

-ERROR (0x0) Last command errored: only valid as response! Parameters:

uint16 errorcode: ERROR\_PROTOVERSIONUNKNOWN //version this high not understood ERROR\_PROTOVERSIONTOOLOW //this should never occur - be sure backwards compatability is present. this is like failing ERROR\_DATABASEVERSIONWRONG //if trying to download databases. using different version ERROR\_GAMEVERSIONWRONG //incorrect version of game position mapping. no reverse compatibility for games (ideas if this is possible?) ERROR\_PACKETBORKED //sent packet was in some way malformed ERROR\_SERVERBORKED //unknown server problem ERROR\_INVALIDPOSITION (Gamesman client) //position sent is not valid ERROR\_INVALIDMOVE (P2P/thin client) //move made is illegal ERROR\_UNKNOWNGAME //not a known game ERROR\_GAMENOTSUPPORTED //game not supported by light client ERROR\_RULEUNKOWN //game rule unknown ERROR\_RULENOTSUPPORTED //rule not supported by light client ERROR\_UNKNOWNCOMMAND //unknown command ERROR\_CLIENTNONEXISTANT //client id non-existant ERROR\_CLIENTTIMEOUT //client timed out (redirector) ERROR\_NOTP2PREDIRECTOR //server cannot p2p redirect ERROR\_ILLEGALID //illegal id ERROR\_NODATABASE //server does not support gamesman clients ERROR\_NOGAMESMAN //server does not support thin clients ERROR\_NEEDPASSWORD //need password for connection ERROR\_REJECTED //reject p2p connection ERROR\_NOTSOLVED //database not solved yet ERROR\_TOOMANYCONNECTIONS //server rejects if too many try to connect to it ERROR\_NOSPECTATORS //cannot spectate this game

-NEGOTIATE PROTOCOL (0x10) - valid for dumb client and direct p2p &gt;request parameters: none &gt;response parameters: none (just inspect all version numbers: respond with error if error!) ERRORS: -PROTOVERSIONTOOLOW -PROTOVERSIONUNKNOWN -ERROR\_SERVERBORKED

-ECHO (0x11) - may be asynch - ping server &gt;request parameters: none &gt;response parameters: none ERRORS: -ERROR\_SERVERBORKED

Headline text
-------------

STATELESS PROTOCOL: This is intended for gamesman clients. Runs as connection between a server providing the database and clients that require it. Stateless though (i.e. HTTP)

Legal ERRORS: ERROR\_PROTOVERSIONUNKNOWN //version this high not understood ERROR\_PROTOVERSIONTOOLOW //this should never occur - be sure backwards compatability is present. this is like failing ERROR\_GAMEVERSIONWRONG //incorrect version of game position mapping. no reverse compatibility for games (ideas if this is possible?) ERROR\_PACKETBORKED //sent packet was in some way malformed ERROR\_SERVERBORKED //unknown server problem ERROR\_INVALIDPOSITION (Gamesman client) //position sent is not valid ERROR\_UNKNOWNGAME //not a known game ERROR\_GAMENOTSUPPORTED //game not supported by light client ERROR\_RULEUNKOWN //game rule unknown ERROR\_RULENOTSUPPORTED //rule not supported by light client ERROR\_NODATABASE //server does not support gamesman clients ERROR\_NOGAMESMAN //server does not support thin clients ERROR\_NOTSOLVED //database not solved yet

header: &gt;client/server protocol version number (sending packet machine's version) -uint16 &gt;game being played (uint16). must assign numbers to games. internal server hash &gt;game option (uint32) - game options &gt;uint16 game version

Headline text
-------------

STATELESS PROTOCOL COMMANDS (0X60-0X8F)

-GET\_GAME\_ID (0x60) - implemented to notify server that we want to utilize a game will set game number. //this required before any call! //server should free memory after perhaps 20 min of no interaction on this game (or use some queue) Request parameters: uint8 length char kdbname\[length\] //datbase name

-REDIRECT\_CLIENT (0x65) - response only -Redirect client to another server if game or game version not supported -Responds this way to any unknown request -only intended if entire database is on another server parameters: uint8 length char servername\[length\] (e.g. po.cs.berkeley.edu:port)

-GET\_VALUE\_OF\_MOVE - 0x70 &gt;request parameters: uint16 length //size of below uint64\[length\] HASH //hashes of positions: WARNING: This is the canonical (see symetry) position. Client must wrap! &gt;response parameters: uint16 length struct res\_pos{

`  uint32 remoteness //32 bit always seemed too large. reduce?`
`  uint8 MEX/Value (low 2 bits are value. upper 6 are MEX)`
`  uint8 redirectindex; //mostly since I had to fill up space. 1 indexed! other values should be 0    redirect for this position`
`  uint16 winby; //reserved for now. In case winby ever is implemented, it goes here`

}\[length\] uint8 redirect\_length; //256 redirect servers \*should\* be enough. anymore would fry client. like we'd have that many moves struct redirect\_info{

`  uint8 length;`
`  char servername[length] (see REDIRECT_CLIENT)`

} \[redirect\_length\] &lt;- 1 indexed!

(client is responsible to ensure that redirects don't go in a loop (from faulty server configurations))

Headline text
-------------

THIN\_CLIENT\_SUBLAYER (0x8 range) <not yet designed. worry about this later. it is part of stateless protocol>

Headline text
-------------

PEER TO PEER COMMANDS (0X20-0X5F) General Errors: ERROR\_PROTOVERSIONUNKNOWN //version this high not understood ERROR\_PROTOVERSIONTOOLOW //this should never occur - be sure backwards compatability is present. this is like failing ERROR\_GAMEVERSIONWRONG //incorrect version of game position mapping. no reverse compatibility for games (ideas if this is possible?) ERROR\_PACKETBORKED //sent packet was in some way malformed ERROR\_INVALIDMOVE (P2P/thin client) //move made is illegal ERROR\_UNKNOWNGAME //not a known game ERROR\_RULEUNKOWN //game rule unknown ERROR\_CLIENTNONEXISTANT //client id non-existant ERROR\_CLIENTTIMEOUT //client timed out (redirector) ERROR\_NOTP2PREDIRECTOR //server cannot p2p redirect ERROR\_ILLEGALID //illegal id ERROR\_NODATABASE //server does not support gamesman clients ERROR\_NOGAMESMAN //server does not support thin clients ERROR\_NEEDPASSWORD //need password for connection ERROR\_REJECTED //reject p2p connection

-BROWSE\_INFO - 0x20 (server probably has this info cached) request params: none response params: uint16 maxprotoversion //max version of protocol this guy is using (0 if forwarding) uint16 gameversion //version of game positions handling (must be exact) uint32 gameoption //game options (options) uint16 gameflags (bit0?IGofirst:UGofirst, bit1?passworded:no\_password, bit2?:allow\_specs:no\_specs,

`      bit3?allow_value_moves:no_value_moves, bit4?allow_prediction:no_prediction)`

uint8 gnamelength char gamename\[gnamelength\] uint16 extra\_data\_length uint8 extra\_data\[extra\_data\_length\] //any extra data about specific game

-REQUEST\_CONNECTION - 0x25 //the brunt of it all. attempt to open a connection between peers //does not apply to spectating. only starting a game request\_params: uint16 protoversion //version of protocol this guy is using uint16 gameversion //version of game positions handling (must be exact) uint8 password\_length //0 if no password char password\[password\_length\]; uint8 my\_name\_length //connector's name char my\_name\[my\_name\_length\]; response params: (if no error, connection has been established) uint8 my\_name\_length //hoster's name char my\_name\[my\_name\_length\];

-DROP\_CONNECTION -0x26 //no params: just a request to terminate game

-SEND\_MOVE - 0x30 //send a move request parameters: -uint64 curposition (note: current position is needed if spectators are present; otherwise remove this) -uint32 MOVE response parameters: NONE

-MESSAGE - 0x31: //Send message to specific player request parameters: uint16 length; char message\[length\] //note: server autoconcatonates (name: ) to this!

Headline text
-------------

FORWARDING SUBCOMMANDS - REFERS TO ALL ACTIVITY OCCURING ON SERVER TO CONNECT P2P PLAYERS Error messages are pretty much what is seen above.

Range: 0x90-0xB9 -All mesages have (inhereted from core) header of: -uint32 id; //unique identifier assigned by server

-CONNECT\_TO\_SERVER (0x90) description: connect to a p2p redirector Request Parameters: -uint16 serverprotoversion //version of protocol server is using -uint8 name\_length -char\[name\_length\] name;

Response Parameters: -uint8 name\_length //accepted name (needed for uniqueness) -char\[name\_length\] name; (id is now set) -short name\_length -char\[name\_length\] name; ERRORS: (primary) -ERROR\_NOTP2PREDIRECTOR

(These should generally be called directly after connection is established) -GET\_OPEN\_GAME\_LIST (0x91) //get a list of open games from the server request params: none Response Parameters uint32 num\_games; struct game\_info{

`  uint8 gname_length;`
`  char gamename[gname_length];`

}\[num\_games\]

-GET\_SPECABLE\_GAME\_LIST (0x91) //get a list of games to spectate from the server request params: none Response Parameters uint32 num\_games; struct game\_info{

`  uint32 gamecode; //unique id of game instance running (server might just cache last position for specs. no playing though)`
`  uint8 gname_length;`
`  char gamename[gname_length];`

}\[num\_games\]

-GET\_CLIENT\_LIST (0x95) //get a list of clients from the server //only ones in lobby, waiting for connection, and accepting specs request params: none response params: uint32 num\_players; struct player\_info{

`   uint32 gamein;`
`   uint8 state (logged off, lobby, waiting, accepting specs, no_accept)`
`       uint8 name_length;`
`       char player_name[name_length];`

}\[num\_players\]

-GAME\_CHANGED (0x97) //notification to clients in lobby that a game changed struct game\_info{

`  uint32 gamecode; //unique id of game instance running (server might just cache last position for specs. no playing though)`
`  uint8 gname_length;`
`  char gamename[gname_length];`

} uint8 game\_state; (0=terminated; 1=open to connect; 2=filled, specable, 3=filled, no spec)

-PLAYER\_ACTION (0x98) //notification to clients in lobby about some player action (enter lobby, server, etc) struct player\_info{

`   uint32 gamein;`
`   uint8 state (logged off, lobby, waiting, accepting specs, no_accept)`
`       uint8 name_length;`
`       char player_name[name_length];`

}

-GLOBAL\_MESSAGE - 0x9A: //Send global message to game (will go to all spectators if forwarding) or server\_lobby request parameters: uint32 gamenum; //message a certain game uint16 length; char message\[length\] //note: server autoconcatonates (name: ) to this!

-LOG\_OUT - 0x9F //log off server no parameters

-INITIALIZE\_GAME - 0xA0 //one player goes into "ready mode" request: uint16 gameversion //version of game positions handling by client uint32 gameoption //game options (options) uint16 gameflags (bit0?IGofirst:UGofirst, bit1?passworded:no\_password, bit2?:allow\_specs:no\_specs,

`      bit3?allow_value_moves:no_value_moves, bit4?allow_prediction:no_prediction)`

uint8 gnamelength char gamename\[gnamelength\] uint16 extra\_data\_length uint8 extra\_data\[extra\_data\_length\] //any extra data about specific game response: uint32 gamenum; //unique identifier of game

-REQUEST\_SPECTATE -0xA1 //request access to spectate a game. can be denied //no negotion: client must make sure that versions match from browsing! request: uint32 gamenum response: uint64 position //last transported position uint32 toplay //player who needs to make the next move

Headline text
-------------

missing notes: -do we care about spectators? I can terminate that bit if we don't -no password lock out of spectators. do we care?
