Client\_side\_modifications
===========================

`   *  Modify main menu to start networked game`
`   * Add resulting sub-menu for setting your name, the server ip, and then entering the lobby`
`   * Adding the “lobby” menu. (q)uit, (h)ost, (r)etract, (l)ist/(u)efresh, (j)oin, (g)etInfo [etc.] {Big suggestion/change here is to create games inside the lobby BBS, for clarity.}`
`   * Add the game creation menu, which should basically be the variation selection menu, but where commiting your changes submits the data packet to the server and registers you.`
`   * Adding the confirm dialogue when a player’s game gets accepted, so they can accept the joiner.`
`     - The joiner, upon selecting to join a game, wait until either the person rejects them (in which case the Joiner goes back to the lobby) or accepts them, in which case the game promptly begins.`
`   * Adding the necessary code to handle the transition into network play, including itializing a network-opponent instead of a computer or human.`
`   * There needs to be the code to handle the GetNetworkPlayerMove() call, which also needs to handle undoing**, resigning, and disconnects. **Big Deal!`
`   * The in-game menu needs to have a resign option, unless aborting takes the role of that.`
`   * The end of game should check to see if this was a network game, and if it was, probably return you back to the lobby.`
`   * I think we need to discuss with Dan and the dB people about how the databases are going to be interfaced in the future into the gamesman client. Now that there are actually choices to be made, it should probably be an ingame menu option. Some of it’s there, I think, but it should probably be consolidated into a Database menu, to deal with loading, storing, saving, formating, etc.`
`   * Once /\ is clear, we’ll need to add our network database option to the UI, both text and hopefully GUI. And don’t forget about the command-line flag too.`
`   * However you set the global gNetworkDatabase flag, during itilization you need to set the function pointers to our netDB functions.`
`   * We need to code the necessary functions for accessing the database, which we’ll then point to in the previous bullet. There’s a few of these functions (value, remoteness, mex, others?) and I/we’ll talk with the dB folk to get a concrete answer on what’ll be needed implemented.`
`     - The lightMemoryPlayer is our model though: that’s a dB that’s not in memory, can’t be modified, but can be read. Remember its name, and pay attention to it. Or rather how it gets used and interfaced with. The module people will mimic the other half of it.`
`         o Someone’ll want to at some point take responsibility, and spend an hour or two tops fixing up the command line doMove call and its companions so that everything useful can be called, and it returns it in a minimalistic format.`
`         o Lastly, I think it would be good and nice to abstract the networking a tiny bit away into a seperate .c file. This way we merely hand out commands and nothing breaks if we change something with the GM-client and server. Also, it would help enforce the idea that dB and p2p access are both the same medium, just different content. Having one establish and used channel would cut down editing as well.`
