# Introduction to APIs

Let's do a review of the next concepts relative to the API topic:

- APIs - You will learn what APIs are and how do they work. You will also gain insights into the Internet protocols and RESTful APIs.
- Handling HTTP Requests - We will introduce you to HTTP, Flask, and writing and accessing endpoints.
- Routing and API Endpoints - You will learn to use endpoints and payloads (information passed along with the request) to extend the functionality of your API. You will learn to organize API endpoints, handling Cross-Origin Resource Sharing (CORS) requests, parsing different request types, and handling errors.
- Documentation - You will learn to write documentation to enable others to use your API or contribute to your project.
- Testing - You will learn unit testing and test-driven development (TDD). Unit testing will ensure that each function is working as expected and handling errors. TDD will teach you to write tests even before defining the functions in your code.

By the end of the course, you will have hands-on experience on the following technology stack:

- Flask
- Flask-CORS
- SQLAlchemy
- JSONify
- Unittest

Before you start development, you should conceptually understand what you're doing. In this first lesson, you'll gain that foundational knowledge. Here's what we'll go over:

- What are APIs?
- Benefits of APIs
- IP Communication
- RESTful APIs

## What are APIs?

If you look up the term API, you'll probably find a number of definitions—some of which are rather difficult to understand. But the key underlying idea is in the name—Application Programming Interface. An API is an interface. It's something that has been created to help two different systems interact with one another.
A key idea to remember is that API functionality is defined independently of the actual implementation of the provider. Essentially, you don't need to understand the entirety of the application implementation in order to interact with it through the API. This has multiple benefits:

1. It doesn't expose the implementation to those who shouldn't have access to it
1. The API provides a standard way of accessing the application
1. It makes it much easier to understand how to access the application's data

Some frequently used APIs include:

- Google Maps API(opens in a new tab) allows users to access a large amount of data related to maps, routes, and places around the world.
- Stripe API(opens in a new tab) allows users to accept payments, send payouts, and manage businesses online.
- Facebook API(opens in a new tab) allows developers to integrate directly with the Facebook platform.
- Instagram Basic Display API(opens in a new tab) allows users of your app to get basic profile information, photos, and videos in their Instagram accounts.
- Spotify API(opens in a new tab) allows users to access a large amount of data related to music artists, albums, and tracks, directly from the Spotify Data Catalogue.

If you check out any of the above links, you'll find some extensive documentation for the relevant API. Creating good API documentation is an important consideration all to itself, and we'll be discussing it in some detail later in this course.

## How APIs work?

Client-Server Communication

When you got to a bank, the bank teller acts as an intermediary or interface between you and the bank vault. And this is the same type of relationship we see in client-server communication: The user or client makes a request to the API server, which parses the requests, queries the database, formats a response and then sends it back.

Here is the process listed out:

1. Client sends a request to the API server
1. The API server parses that request
1. Assuming the request is formatted correctly, the server queries the database for the information or performs the action in the request
1. The server formats the response and sends it back to the client
1. The client renders the response according to its implementation

### Internet Protocol

Internet Protocol (IP) is the protocol for sending data from one computer to another across the internet. Each computer must have a unique IP address that identifies it from all other computers connected to the internet. It's likely that you've heard the term IP address before, even if you didn't know exactly what it meant.

There are many other internet protocols including:

- Transmission Control Protocol (TCP) which is used for data transmission
- Hypertext Transmission Protocol (HTTP) which is used for transmitting text and hyperlinks
- File Transfer Protocol (FTP) which is used to transfer files between server and client

Our API will transmit data to our client via HTTP so we will primarily focus on that protocol.

## REST API

If you've done some research into developing APIs, you may have come across the term RESTful API(opens in a new tab). REST stands for Representational State Transfer, which is an architectural style introduced by Roy Fielding in 2000(opens in a new tab).

Here's a short summary of the REST principles:

- Uniform Interface: Every rest architecture must have a standardized way of accessing and processing data resources. This includes unique resource identifiers (i.e., unique URLs) and self-descriptive messages in the server response that describe how to process the representation (for instance JSON vs XML) of the data resource.
- Stateless: Every client request is self-contained in that the server doesn't need to store any application data in order to respond to subsequent requests
- Client-Server: There must be both a client and server in the architecture
- Cacheable & Layered System: Caching and layering increases networking efficiency

### Why RESTful are stateless?

It might appear easier to design a server that isn't stateless. There is a reason why RESTful web servers are not allowed to remember anything about the previous requests that the user has sent. In short, stateless servers make your applications scalable.
