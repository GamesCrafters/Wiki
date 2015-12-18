Make -O0 the default optimization flag - Mario Tanev, 12-26-2005
================================================================

Currently gamesman is compiled using O3 optimization flag, alongside debug which is not appropriate. We should either create a mechanism upon which to compile everything -O0 -g when we need debugging, or make that the default.
