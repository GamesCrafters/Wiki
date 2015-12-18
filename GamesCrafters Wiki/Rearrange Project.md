Rearrange Project
=================

I.Rearrange Hasher

VARIABLES TYPE DESCRIPTION

xHash DartboardHash X major hash

oHash DartboardHash O major hash

length int Board Size

xChar char char of the piece that goes first

oChar char char of the piece that goes second

board char\[\] array of chars(from {xChar,oChar,' '}) representing the board

OX boolean OX = true =&gt; X's turn

`                   OX = false => O's turn`

METHODS INPUTS DESCRIPTION

setnums \# of ' ', xChars, oChars sets board to position of hash = 0 based on inputs

unhash hash value (long) sets board to position based on hash value and \# of ' ', xChars, oChars

hash position(char\[\]) ERROR if mismatch with \# of ' ', xChars, oChars

`                       copies position to internal board`
`                                               returns hash value of board`
`                               `

setNumsAndHash position(char\[\]) setNums then hash

next changed iterator changes internal board and hash to match next hash value

`                                               records which indexes on the board was changed in iterator`
`                               `

getCharArray copyTo(char\[\]) copies board to copyTo

getChildren char, char, childArray sets childArray to array of children's hash values Optimization: Iterate through board once only. Iterate through the major array. If the current major array value is 1 do nothing. If the current major array value is 0 and if the corresponding minor array value is 1, add 1 to num1s. Otherwise store originalminorhashvalue \* (i-1-\#1s)/(i-1)+newMajor\*(minorarraaylength - 1 choose num1s in minor hash) in childArray.
