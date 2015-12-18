Bit-Perfect DB
==============

The purpose of the **Bit-perfect Database Project** is to devise and implement, as efficiently as possible, a file format for storing enumerated game values. The current system for handling the storage of fully enumerated games is memDB. We seek to replace memDB because of its inability to compress empty gaps in the game values array. These gaps exist since for most of Gamesman games only a combinatorial perfect hash function exists, which means many buckets are never hashed to and are thus 16 bits of empty space each in memDB's representation.

Game Values Background
----------------------

Game values in Gamesman are stored in arrays whose lengthed are fixed based on the game. For the purposes of this general explanation, we can assume that the game values are stored in array entries 16 bits wide; these will be called records. Each record contains a fixed amount of room to store several game values for the board that hashes to this particular record. The following are some examples: value (win, lose, tie), grundy number, and remoteness.

Problems to Solve
-----------------

There are two immediately visible problems with the current implementation. The first is that records often do not allocate an appropriate amount of room to store values such as grundy number and remoteness. In these cases, Gamesman is said to simply crash. The second is that records that are not hashed to simply exist as empty records that take up the full number of bits a used record would. On average, more than 97% of records are unused which poses a serious problem--97% of our data files are currently filled with blank data.

Solution
--------

[Dan Garcia](Dan_Garcia "wikilink") has devised a system to solve the latter problem. He proposes that the first bit of every record should be used to designate whether the record is being used; 0 if it is, 1 if it is not. In cases where a 0 is the first bit, the next n-1 bits, where n is the size of the record in bits, are used to represent the game values for the record. In the event that a gap must be represented, a 1 is used as the first bit; this indicates that the standard record format will not be used. Any number of 1s can follow this initial 1. The number of 1s including the first 1 will represent the number of bits used to represent the size of the gap between utilized records. The following is an example of the counting system:

10\_ 1-2 (Range of gaps representable)

`  100 1`
`  101 2`

110\_ \_ 3-6

`  11000 3`
`  11001 4`
`  11010 5`
`  11011 6`

1110\_ \_ \_ 7-14

`  11100000 7`
`  11100001 8`
`  11100010 9`
`  11100011 10`
`  11100100 11`
`  11100101 12`
`  11100110 13`
`  11100111 14`

Page in progress...
