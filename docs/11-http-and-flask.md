# HTTP and Flask

This section will lay the foundation for the rest of the course. You'll learn more about the HTTP protocol and how to implement an API using the Flask microframework. Here's what we'll cover:

- HTTP Basics
  - Methods
  - Requests
  - Responses
  - Status Codes
- Flask Microframework Intro
  - Creating your first basic endpoints
  - Testing the response using Curl

In this lesson the new technologies you'll use are: Flask and Curl

## HTTP

Hypertext Transfer Protocol (HTTP) is a protocol that provides a standardized way for computers to communicate with each other. It has been the foundation for data communication over the internet since 1990 and is integral to understanding how client-server communication functions.

### Features

- Connectionless: When a request is sent, the client opens the connection; once a response is received, the client closes the connection. The client and server only maintain a connection during the response and request. Future responses are made on a new connection.
- Stateless: There is no dependency between successive requests.
- Not Sessionless: Utilizing headers and cookies, sessions can be created to allow each HTTP request to share the same context.
- Media Independent: Any type of data can be sent over HTTP as long as both the client and server know how to handle the data format. In our case, we'll use JSON.

### Elements

- Universal Resource Identifiers (URIs): An example URI is <http://www.example.com/tasks/term=homework>. It has certain components:
  - Scheme: specifies the protocol used to access the resource, HTTP or HTTPS. In our example http.
  - Host: specifies the host that holds the resources. In our example <www.example.com>.
  - Path: specifies the specific resource being requested. In our example, /tasks.
  - Query: an optional component, the query string provides information the resource can use for some purpose such as a search parameter. In our example, /term=homework.

> ### Side Note: URI vs URL
>
> You may be unsure what the difference is between a URI (Universal Resource Identifier) and a URL (Universal Resource Locator). These terms tend to get confused a lot, and are even frequently used interchangeably—but there is a distinction.
> The term URI can refer to any identifier for a resource—for example, it could be either the name of a resource or the address of a resource (since both the name and address are identifiers of that resource). In contrast, URL only refers to the location of a resource—in other words, it only ever refers to an address.
> So, "URI" could refer to a name or an address, while "URL" only refers to an address. Thus, URLs are a specific type of URI that is used to locate a resource on the internet when a client makes a request to a server.
> And if you really want to dive into the topic, here are some further readings (with examples and Venn diagrams):
>
> - StackExchange: What is the difference between a URI and a URL?(opens in a new tab
> - StackOverflow: What is the difference between a URI, a URL, and a URN?(opens in a new tab
> - RFC 3986(opens in a new tab), published by the Internet Engineering Taskforce(opens in a new tab) (this one is rather hefty and more of an official reference than a reader-friendly explanation)

## HTTP Requests

HTTP requests are sent from the client to the server to initiate some operation. In addition to the URL, HTTP requests have other elements to specify the requested resource.

### Elements

- Method: Defines the operation to be performed
- Path: The URL of the resource to be fetched, excluding the scheme and host
- HTTP Version
- Headers: optional information, such as Accept-Language
- Body: optional information, usually for methods such as POST and PATCH, which contain the resource being sent to the server

### HTTP Request Methods

Different request methods indicate different operations to be performed. It's essential to attend to this to correctly format your requests and properly structure an API.

- GET: ONLY retrieves information for the requested resource of the given URI
- POST: Send data to the server to create a new resource.
- PUT: Replaces all of the representation of the target resource with the request data
- PATCH: Partially modifies the representation of the target resource with the request data
- DELETE: Removes all of the representation of the resource specified by the URI
- OPTIONS: Sends the communication options for the requested resource

## HTTP Responses

After the request has been received by the server and processed, the server returns an HTTP response message to the client. The response informs the client of the outcome of the requested operation.

### Elements

- Status Code & Status Message
- HTTP Version
- Headers: similar to the request headers, provides information about the response and resource representation. Some common headers include:
  - Date
  - Content-Type: the media type of the body of the request
- Body: optional data containing the requested resource

### Status Codes

As an API developer, it's important to send the correct status code. As a developer using an API, the status codes—particularly the error codes—are important for understanding what caused an error and how to proceed.
Codes fall into five categories:

- 1xx Informational
- 2xx Success
- 3xx Redirection
- 4xx Client Error
- 5xx Server Error

## Flask

Flask(opens in a new tab) is the tool we'll use to create our API server.

It is a "micro" framework, which means that its core functionality is kept simple, but that there are numerous extensions to allow developers to add other functionality (such as authentication and database support).

In this section we will cover:

- Creating a basic Flask application
- Writing a basic endpoint
- Checking the response using Curl.

### Curl

Curl is a library and command-line tool that completes IP transfers of data using URLs. One quick way to test your API while your API server is running is to run a curl command in another terminal window.

The "curl" command is a powerful tool that allows you to send HTTP requests and receive HTTP responses from a server.
Curl Syntax

```sh
curl -X POST http://www.example.com/tasks/
```

The above is a sample curl request. Every request starts off with the command curl and needs to include a URL. Other parts you see added in are options that you can use to build your request. In the example the -X shortform option (also --request) specifies the request method.

### CURL Options

You can find more options by entering the following command in the terminal.

```sh
curl --help
```

Some frequently used options are:

- -X or --request COMMAND
- -d or --data DATA
- -F or --form CONTENT
- -u or --user USER[:PASSWORD]
- -H or --header LINE

You may already have curl available on your local machine. Open up a terminal and check by running:

```sh
curl --version
```

If you do not have it installed, you can see the instructions here(opens in a new tab) for your OS.
