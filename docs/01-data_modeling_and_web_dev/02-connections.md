# Connections

TCP/IP is connection-based, meaning all communications between parties are arranged over a connection. A connection is established before any data transmission begins.

Over TCP/IP, we'll always need to establish a connection between clients and servers in order to enable communications. Moreover, it deliveries over the connection are error-checked: if packets arrive damaged or lost, then they are resent (known as retransmission).
Connecting starts a session. Ending the connection ends the session. In a database session, many transactions can occur during a given session. Each transaction does work to commit changes to the database (updating, inserting, or deleting records).

## Aside: the UDP Protocol

The internet also offers the UDP protocol. UDP stands for User Datagram Protocol. UDP is much simpler than TCP: hosts on the network send data (in units called datagrams) without any connections needing to be established.

## TCP vs UDP

If TCP is like building roads between houses before sending packages between them, then UDP is much like sending over a carrier pigeon from house to house in order to deliver messages: you don't have much control over the pigeon once it flies away -- will the pigeon will fly the right direction, drop your package into the dirt, or encounter attacking bald-eagle during flight. On the other hand, USD has less overhead than TCP / building a highway.

When speed is more important than reliability, especially when applications need to stream very small amounts of information quickly (smaller packages of information mean fewer issues with reliability), then UDP is preferred. A lot of real-time streaming applications, (e.g. live TV streaming, Voice over IP (VoIP)) prefer UDP over TCP. Since UDP does not need to retransmit lost datagrams, nor does it do any connection setup, there are fewer delays over UDP than TCP. TCP's continuous connection is more reliable but has more latency.
