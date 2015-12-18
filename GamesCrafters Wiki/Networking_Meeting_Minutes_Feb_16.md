Networking\_Meeting\_Minutes\_Feb\_16
=====================================

Network Meeting 2/16

Thursday, February 16, 2006

9:04 PM

 

Protocol

-   <span style='font-family:Verdana'>Use of messages</span>
-   <span style='font-family:Verdana'>Serialization
    `    Scheme`</span>

<!-- -->

-   <span style='font-family:Verdana'>Knowledge of
    `     everything being sent`</span>

<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Once we get

`    some sort of client off the ground we can finalize what we need from the`
`    protocol`</span>

</li>
</ul>
 

Text Interface (Client)

-   <span style='font-family:Verdana'>A network
    `    adapter will have to be built underneath the interface`</span>

<!-- -->

-   <span style='font-family:Verdana'>Calls made
    `     into the normal gamesman will passed through to the adapter to make`
    `     socket calls`</span>

-   <span style='font-family:Verdana'>Use library:
    `     libasync?`</span>

<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Send it through

`    a serialization scheme`</span>

</li>
<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Probably done

`    asynchronously`</span>

</li>
-   <span style='font-family:Verdana'>Do not want to
    `     block the GUI`</span>

</ul>
Server

-   <span style='font-family:Verdana'>TCP or UDP?</span>

<!-- -->

-   <span style='font-family:Verdana'>Probably want
    `     the reliability of TCP`</span>

<!-- -->

-   <span style='font-family:Verdana'>Not sending
    `      too many packets`</span>

-   <span style='font-family:Verdana'>Need to get
    `      every packet`</span>

</ul>
<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Java test

`    server could be built`</span>

</li>
-   <span style='font-family:Verdana'>Matt could
    `     create a Stub server for a test`</span>

<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Real server

`    could not be built in java`</span>

</li>
<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Gamesman code

`    would have to plug in`</span>

</li>
<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Server will

`    take a request and then dispatch it in a thread`</span>

</li>
-   <span style='font-family:Verdana'>Data must be
    `     de-serialized to find the header`</span>

<!-- -->

-   <span style='font-family:Verdana'>How much
    `      needs to be de-serialized?`</span>

-   <span style='font-family:Verdana'>You might
    `      just have to hand off some struct`</span>

<!-- -->

-   <span style='font-family:Verdana'>Depends on
    `       what the module guys want`</span>

</ul>
<li style='mso-outline-level:3;margin-top:0;margin-bottom:0;vertical-align:
      middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Library:

`     libasync, sys/socket, samba4?`</span>

</li>
<li style='mso-outline-level:3;margin-top:0;margin-bottom:0;vertical-align:
      middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Run just

`     something like a loop that listens all the time`</span>

</li>
<li style='mso-outline-level:3;margin-top:0;margin-bottom:0;vertical-align:
      middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Does not have

`     to be fancy just has to work`</span>

</li>
<li style='mso-outline-level:3;margin-top:0;margin-bottom:0;vertical-align:
      middle;font-size:10.0pt'>
<span style='font-family:Verdana'>If it’s a

`     certain type send it to a module in a thread`</span>

</li>
<li style='mso-outline-level:3;margin-top:0;margin-bottom:0;vertical-align:
      middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Modules</span>

</li>
-   <span style='font-family:Verdana'>The module
    `      could write back the socket?`</span>

<!-- -->

-   <span style='font-family:Verdana'>If you don’t
    `       write back to the socket then you would not have to know the current`
    `       version of the protocol?`</span>

<li style='mso-outline-level:4;margin-top:0;margin-bottom:0;vertical-align:
       middle;font-size:10.0pt'>
<span style='font-weight:bold;font-family:Verdana'>Find

`      out where is the split between modules is`</span>

</li>
<li style='mso-outline-level:4;margin-top:0;margin-bottom:0;vertical-align:
       middle;font-size:10.0pt'>
<span style='font-family:Verdana'>What kind of

`      interface are we going to use`</span>

</li>
<li style='mso-outline-level:4;margin-top:0;margin-bottom:0;vertical-align:
       middle;font-size:10.0pt'>
<span style='font-family:Verdana'>How would two

`      player work?`</span>

</li>
</ul>
<li style='mso-outline-level:3;margin-top:0;margin-bottom:0;vertical-align:
      middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Every request

`     could be stateless and then passed to the module who closes it or we can`
`     close it ourselves`</span>

</li>
-   <span style='font-family:Verdana'>Module could
    `      say I got nothing for you`</span>

-   <span style='font-family:Verdana'>It could also
    `      say that its got a player`</span>

<!-- -->

-   <span style='font-family:Verdana'>Might pick a
    `       random port to create the stateful connection `</span>

-   <span style='font-family:Verdana'>The response
    `       to the client might be to create a stateful request at a certain port`</span>

<li style='mso-outline-level:4;margin-top:0;margin-bottom:0;vertical-align:
       middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Server could

`      be the one that handles the listening`</span>

</li>
-   <span style='font-family:Verdana'>Module could
    `       ask the server to open certain ports and hand it back to the module`</span>

</ul>
</ul>
<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Alternatively

`    using a application server`</span>

</li>
-   <span style='font-family:Verdana'>Jboss (J2EE)
    `     but for C`</span>

-   <span style='font-family:Verdana'>It will be
    `     quick to get off the ground`</span>

<!-- -->

-   <span style='font-family:Verdana'>Not terribly
    `      robust`</span>

<li style='mso-outline-level:3;margin-top:0;margin-bottom:0;vertical-align:
      middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Apache Mods

`     might be able to handle what we want`</span>

</li>
-   <span style='font-family:Verdana'>The have
    `      stuff like to plug in to Perl interpreter and PHP interpreter`
    `      (application server like)`</span>

-   <span style='font-family:Verdana'>Might be a
    `      mod to be able to spin a system executable or put a process or a apache`
    `      API?`</span>

</ul>
<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Gamesman Does </span><span
     style='font-weight:bold;font-family:Verdana'>NOT </span><span
     style='font-family:Verdana'>live on the server</span>

</li>
-   <span style='font-family:Verdana'>Only parts of
    `     gamesman that we need`</span>

-   <span style='font-family:Verdana'>Most of the
    `     stuff will be handled on the gamesman client except for thin client`</span>

<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Client

`    Registration `</span>

</li>
-   <span style='font-family:Verdana'>Have to do
    `     certain things that might be the responsibility of the server`</span>

<!-- -->

-   <span style='font-family:Verdana'>Register
    `      could be stateless`</span>

<!-- -->

-   <span style='font-family:Verdana'>Would we
    `       need stateful?`</span>

-   <span style='font-family:Verdana'>Stateless
    `       has to be done with pull requests (client only gets data when asks for`
    `       it)`</span>

</ul>
</ul>
<li style='mso-outline-level:2;margin-top:0;margin-bottom:0;vertical-align:
     middle;font-size:10.0pt'>
<span style='font-family:Verdana'>Gameplay</span>

</li>
-   <span style='font-family:Verdana'>Might want to
    `     do P2P statefully`</span>

<!-- -->

-   <span style='font-family:Verdana'>This way you
    `      can just send a move to the client`</span>

-   <span style='font-family:Verdana'>Otherwise the
    `      client would have to poll the server to see if moves have been made`</span>

</ul>
</ul>
Future Steps/Things to Think About

-   <span style='font-family:Verdana'>Once the Stub
    `    Server is created`</span>

<!-- -->

-   <span style='font-family:Verdana'>We can think
    `     about what we need`</span>

<!-- -->

-   <span style='font-family:Verdana'>Functionality</span>
-   <span style='font-family:Verdana'>Keep adding
    `      to the modules and the server`</span>

</ul>
</ul>
 
