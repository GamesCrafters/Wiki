Add board constructor-destructor-save-restore abstraction as substitute for GPS - Mario Tanev, 01-13-2006
=========================================================================================================

Methods: struct {

` /* Initialize the game-state`
`    Any module-defined game-state data structures are allocated here.`
`  */`
` void (*initialize)(POSITION position);`
` `
` /* Initialize the game state to a canonical representation`
`    Any module-defined game-state data structures are allocated here.`
`  */`
` POSITION (*initialize_canonical)(POSITION position);`

` /* Save the game-state`
`    All module-defined game-state data structures are encapsulated and a unique pointer is returned, which is stored in the game-graph stack (solver)`
`  */  `
` void *(*save)();`

` /* Restore the game-state`
`    The solver provides a pointer to the saved state for the game to restore`
`  */`

` void *(*restore)(void *state);`
` `
` /* Finalize the game-state`
`  */`
` void *(*finalize)(void *state);`

}
