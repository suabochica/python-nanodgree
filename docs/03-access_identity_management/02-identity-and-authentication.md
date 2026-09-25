# Identitiy and Authenticaiton

Identity and authentication are essentially asking the question: who is making a request to the digital systems? In this lesson, we will explore different techniques to identify and authenticate, such as usernames and passwords, or multi-factor authentication.

## Authentication in the Digital World

Let's look at a brief overview of the concepts we'll be covering. If you don't understand all of the details given in this video at this stage, don't worry—we're going to go over all of this in much greater detail throughout the lesson!

In a simplified fashion where there are only the frontend and the API server, a user will interact with the frontend and sending a request to the API server. Then a process will verify the identity. Once the identity is verified, a response will be returned.

In this lesson, we will discuss the following topics related to authentication:

- Common authentication method
- Alternative authentication methods
- Third-party auth systems
- Implementing Auth0
- JSON web token (JWT) - data structure and validation
- Local storage
- Sending tokens

## Username and Passwords

The most common authenticating technique is using a username and password pair.

Once a user submits the username and password pair, this information is sent to the API server. Then a request is made to the database using the unique username to pull that user's information including the ground truth password or the representation of the ground truth password.

Then the representation of the password is brought into the API server, where we can compare the two passwords. If the password entered by the user matches the ground truth password stored in the database, we can pass a 200 response to the frontend, allowing that login. If they don't match, we can reject the attempt with a 401 HTTP status code.

![Password Match](../../images/password-matching.png)

### HTTP Status Codes

Two status codes which are important throughout this course are:

- 401 Unauthorized

The client must pass authentication before access to this resource is granted. The server cannot validate the identity of the requested party.

- 403 Forbidden

The client does not have permission to access the resource. Unlike 401, the server knows who is making the request, but that requesting party has no authorization to access the resource.

### Brief intro to Password Problems

There are some issues with passwords are outside of our control as developers. Many issues come from user behavior that we cannot directly influence, such as:

- Users forget their passwords
- Users use simple passwords
- Users use common passwords
- Users repeat passwords
- Users share passwords

In contrast, some issues are within our control as developers:

- Passwords can be compromised
- Developers can incorrectly check
- Developers can cut corners

## Single Sign-On
