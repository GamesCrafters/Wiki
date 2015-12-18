Avro
====

Overview:
---------

This semester I focused on starting work to replace the existing Apache Thrift layer with Avro, as part of the infrastructure overhaul. Other work involved cleaning up and polishing what James and I worked on last semester with "liberating" GamesmanClassic and exposing it to the web.

Avro:
-----

[Avro](http://avro.apache.org/) is a serialization system, similar to Apache Thrift, which is currently used as the RPC layer GamesmanJava/Classic and the GamesmanWeb server. Avro begins with a simple schema which defines the RPC methods as well as the data types transmitted across the system. This schema generates files that are to be used by both the server and client, much like for Thrift.

For more detailed explanation, refer to [Avro's Documentation](http://avro.apache.org/docs/current/)

### Relevance to GamesCrafters

There are several motivations for replacing the existing Thrift layer and Avro are that firstly, Avro natively supports HTTP sockets, which allows us to use Avro to and from our server on Google App Engine. Avro also allows for arbitrary data types to be expressed, giving us more flexibility.

An in-progress version of the Avro schema for the Gamesman system is currently in the repositories. The schema isn't finalized, so the current state of the Avro-replacement-process is still in its infancy. Currently there is a dummy Avro client running on our AppEngine app that queries an Avro server on NYC accepting only basic requests as a proof of concept of this portion of the system.

### Future Work

Much work still needs to be done on this end. After major design decisions regarding the Gamesman API infrastructure is finalized, then work in actively replacing the entirety of Thrift with Avro should be undertaken.

Other Stuff:
------------

GamesmanClassic/Web is currently being update so that remoteness values are returned when GetNextMoveValues and GetMoveValue are called.

A bug that spawned many processes to solve an unsolved variant was fixed.
