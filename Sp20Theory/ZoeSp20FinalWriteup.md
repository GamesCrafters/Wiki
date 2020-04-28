###Gamescrafters Sp20 Writeup
-----

This semester I focused on three main areas:

##Counting: 
Expanding the number of counts in our Counting google sheet. I started with known games (Othello) at the beginning of the semester to kick start my brain and have moved through the sheet as best I can. Other members of the theory group have added to the sheet, namely Max with LOA counts, Max and Kevin with Kuba counts, Xinyun with shuttles analysis, and Stella and Xinyun with tic tac two. This sheet serves as a great way to organize the unique knowledge that GamesCrafters have-- we have counted games no one else has!

##Mentoring: 
I mentored Max in his work with LOA, Xinyun and Stella with their work on hashing tic tac two and shift-tac-toe hashing, Max and Kevin counting and hashing Kuba, and discussing effective introductions to the theory team with Lawrence. My hope is they will return and keep the GamesCrafters theory team alive!

##Connect 4: 
I wrote a simplified writeup of the infamous connect four paper and then slowly stepped through an inductive proof as to why the uniqueness of the hashing holds, which can be found [here](https://github.com/GamesCrafters/Wiki/blob/master/Sp20Theory/davidPaper.txt) and [here](https://github.com/GamesCrafters/Wiki/blob/master/Sp20Theory/InductiveProofDavid.pdf) respectively. As I have begun turning this into a hash for Jordan (the current connect four solver team) to actually use, I have started counting the space of the hash function and have determined that it is actually fairly large. Given we represent the coloration order as half of the hash, patterns that are illegal in gameplay are represented. This issue compounds given that there are several height orderings that correspond with each color pattern, meaning there are several invalid states hashed for every invalid coloration ordering. Perhaps this is one of the features that cause David's initial solve to take several days spread across his banks. In a different, but equally dissapointing vein, I worked throughout the semester on continuing the idea of using MEX values to solve connect four but determined that this idea does not hold for this step. Based on the inductive proof for the connect four hash linked above we can actually determine losing MEX values for positions which are in fact not losing positions. While the hashing approach used by David could have more meat to it for future GamesCrafters, I think it is time we put the idea of using MEX to solve connect four to bed. 

##Looking forward:
My goal as I graduate from GamesCrafters is that the theory team continues to learn more and grow stronger. The GamesCrafters Shared Files/Sp20 Theory/Sp20 Counting google sheet holds all of our current counting numbers. I hope moving forward someone is willing to take ownership of the sheet and the group and motivate and aid others to continue counting and exploring. 