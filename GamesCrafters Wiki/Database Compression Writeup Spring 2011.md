Database Compression Writeup Spring 2011
========================================

### Team Members

Caroline Modic James Muerle

### Overview

Significantly compress how much space our databases take up.

### Process

Since the biggest solved games we currently have (Connect-4 and The Game of Y) are tier-based games, we decided to focus our compression on games that have tiers. By doing this, a clear strategy came around to simply eliminate tiers. If the client requested a value for a position on an eliminated tier the database does two things. It first checks if that tier is a primitive, if so it just called the game's primitive value function on it and returns the correct value. Otherwise, it looks up all the values for that positions children and calculates the current position's value exactly how it is originally calculated by the solver.

### Current Use

David has taken our code and implemented it on any game taking up significance space on the server. We have found that it is better to eliminate more tiers towards the end of the game. In the last few tiers there are a lot of illegal positions being stored so you eliminate a lot of space, for relatively few actual positions being eliminated where you would need to calculate inside the database. Furthermore as long as several tiers aren't eliminated in a row there is no noticeable change in speed so we have been able to make significant reductions to database sizes. For example, the 7x6 version of Connect 4 has been reduced from 1.6 terabytes to around 300 gigabytes.

### Future Projects

In the future Gamescrafters should look into ways of expanding our method to be used with other types of games, particularly loopy ones. Furthermore, people currently need to analyze by hand how much cutting each tier effects time and size, and there could be some effort to calculate better strategies to determine which tiers to ideally remove, how many tiers can often be removed before it slows down in a typical game, or even write a program to create databases with different tiers cut and time them in retrieving positions.
