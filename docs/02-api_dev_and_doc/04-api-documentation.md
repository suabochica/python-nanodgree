# API Documentation

Now that you've learned the ins and outs of creating a RESTful API, you'll learn about how to make your API accessible and usable for other developers. In this lesson we will cover:

- Good vs. Bad API Documentation
- Practice writing API Documentation
- Project Documentation

Finally, you'll complete some preparation for your final project in which you'll use all your skills to demonstrate your ability as an API developer.

## Google Maps API

Not only is the data supported by the Google Maps API huge, but the API itself is also massive. There are different APIs and SDKs (Software Development Kits) depending on the data you are looking to access and also how you are looking to access the data.

Our API is significantly smaller than Google Maps, and the documentation will be able to be contained in a README, however, it is good practice to think about how your documentation might be organized as your project grows.

## REST Countries

It is useful to look at existing documentation to get a feel for the level of documentation provided. Sometimes a name is descriptive enough, and other times a longer description is necessary. In addition, while some APIs may only show the format of a request, others provide an example in place of or in addition to the format, while others will also provide example responses.

## Stripe API

Stripe is a great example of documentation because they are used for payment processing, where it is essential to hit the exact endpoints and understand how to process data.

A few items to note about the Stripe API:

- Is a RESTful API
- Has resource-oriented URLs
- Returns JSON encoded responses
- Uses standard HTTP response code, authentication, and verbs
- Provides the base URL

The Stripe API is broken up into different sections that are shown along the left. Similar to Stripe, it is important for your own documentation to include specific error codes and messages for developers that will use your API. Another nice thing that Stripe does is provide a sample request via Curl, so that interested developers can copy and paste the command directly into a terminal to test the API. Lastly, they provide a detailed response object so that you can see what the response body would look like without running any code.

## Good API Documentation

Good API documentation allows any developer considering the API to quickly understand the purpose of the API, the data it works with, and how to send requests and parse the responses. Some documentation, particularly for large projects, even host samples you can run within the documentation to see the API in action. For the purposes of this course, you don't need to implement interactivity, but you will provide examples that can be run by someone viewing your documentation.

Here's a recap (for your reference) of the components that are typically included in good API documentation:

- Introduction
- Getting Started
    - Base URL
    - API Keys /Authentication (if applicable)
- Errors
    - Response codes
    - Messages
    - Error types
- Resource endpoint library
    - Organized by resource
    - Include each endpoint
    - Sample request
    - Arguments including data types
    - Response object including status codes and data types

## Structure

All good, well-documented projects have a README.md file that should clearly explain the project and how to get started with it to any developers who may want to use or contribute to the project. Depending on your personal style preferences and project type, the structure and exact contents will differ, but the structure below is a good starting place.

- Project Title
    - Description of project and motivation
    - Screenshots (if applicable), with captions
    - Code Style if you are following particular style guides
- Getting Started
    - Prerequisites & Installation, including code samples for how to download all pre-requisites
    - Local Development, including how to set up the local development environment and run the project locally
    - Tests and how to run them
- API Reference. If the API documentation is not very long, it can be included in the README
- Deployment (if applicable)
- Authors
- Acknowledgements

## Recap

In this lesson, we learned how to make our API accessible and usable for other developers. We covered:

- Good vs. Bad API Documentation
- Practice writing API Documentation
- Project Documentation

Next up you will put your API documentation skills into practice in the project!
