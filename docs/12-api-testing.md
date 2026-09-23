# API Testing

As with any code you write, you want to test your API to ensure that requests are processed as you expect, the responses sent are correct, and the operations performed on the database are correct and persist.

In this lesson we'll cover:

- Purpose and Benefits of API Testing
- Testing a Flask Api with Unittest
- Test-Driven Development for APIs

Why Testing?

As with all tests, writing unittests for your API verifies the behavior. For APIs, test should be written:

- To confirm expected request handling behavior
- To confirm success-response structure is correct
- To confirm expected errors are handled appropriately
- To confirm CRUD operations persist

In addition to verifying behavior, having a thorough test suite ensures that when you update your API, you can easily test all previous functionality.

If bugs are discovered while in development, they cost next to nothing to fix and don't have any negative impact on business outcomes or client experience. But if bugs make it to production, their cost can be quite large—they can impact performance, and fixing bugs can take large amounts of time for big, production applications.

The order of operations for app development should always be:

1. Development
2. Unit Testing
3. Quality Assurance
4. Production

Step 2 is essential to ensuring the application is production-ready and time-to-production is used efficiently.

![App Development Timeline](../images/app-dev-timeline.png)


API testing is done to ensure that the API functions as expected and provides accurate and consistent results. APIs (Application Programming Interfaces) are used to enable communication between different software systems or components.

API testing helps to verify the behavior of the API by checking its functionality, reliability, security, and performance. It can also identify issues related to data formatting, response time, and error handling.

By testing the API, developers can detect any issues before the system is deployed to production, thus reducing the risk of downtime or other critical failures. It can also help to improve the overall quality of the software by identifying and resolving issues early in the development process.

## Testing Prep

Before you get started writing your own testing code, we'll review the essential elements of writing a test suite using unittest in Python3. We'll break down the code into it's different components and provide a little more explanation of each.

```py
#Import all dependencies
import unittest
import json
from flaskr import create_app
from models import setup_db
```

Once you've created your test file, the very first thing that you'll need to do is import all of your dependencies. You'll need unittest, json, as well as the create_app method that you created in the init file in the project directory, as well as setup_db from your models so that you can setup your test database.

```py
class ResourceTestCase(unittest.TestCase): 
```

Next, you'll create a class for the test case based off of `unittest.Testcase`. Typically, you'll organize these test cases by resource. So if we're in an application that has users and messages, we will likely have two test classes, UserTestCase and MethodTestCase.

```py
    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "test_db"
        self.database_path = "postgres://{}/{}".format('localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
 
```

Within our setup method we do quite a few things. First, we setup the app using our createAppmethod. Then we setup the test client. Flaskr includes a test client very helpfully, so we can do that using self.app.test_client. We also want to setup a test database so that we don't touch our production database, which we do by setting the self.database_name and `self.database_path`, as well as calling setup_db with `self.app` and `self.database_path`.

```py
    def tearDown(self):
        """Executed after each test"""
        pass
```

Then, we should also create a tearDown method. In this case there's nothing that we need to do to tear it down, but if there are any ports that you opened or anything that you need to do to make sure that it is cleared after each test, this is where you would do that. tearDown runs after each test.

```py
    def test_given_behavior(self):
        """Test _____________"""
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)
```

We'll write tests for each given behavior. For our APIs we want to make sure that we're testing both success and error behavior. Within this method, we'll actually make a request using our test client self.client which has various methods such as .get in this example or .post and .patch Then, we'll save that response and make some assertions. The one you see here, self.assertEqual(res.status_code, 200) is ensuring the status code is 200 or "ok." If you are expecting a given body, you want to make sure that is there as well, and when you're testing your errors you'll want to make sure that the body and the status code are as expected.

```py
# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
```

Finally, to actually allow us to run this test, we need these final two lines. This just makes the tests conventionally executable.

Note that you can practice in you local environment.

## Unit test Flask Key Structures

As we just saw, all of your Flask application tests will follow the same format:

- Define the test case class for the application (or section of the application, for larger applications).
- Define and implement the setUp function. It will be executed before each test and is where you should initialize the app and test client, as well as any other context your tests will need. The Flask library provides a test client for the application, accessed as shown below.
- Define the tearDown method, which is implemented after each test. It will run as long as setUp executes successfully, regardless of test success.
- Define your tests. All should begin with "test_" and include a doc string about the purpose of the test. In defining the tests, you will need to:
  - Get the response by having the client make a request
  - Use self.assertEqual to check the status code and all other relevant operations.
- Run the test suite, by running python test_file_name.py from the command line.

Here's that same code (from the notebook above), for your reference:

```py
class AppNameTestCase(unittest.TestCase):
    """This class represents the ___ test case"""

    def setUp(self):
        """Executed before each test. Define test variables and initialize app."""
        self.client = app.test_client
        pass

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_given_behavior(self):
        """Test _____________ """
        res = self.client().get('/')

        self.assertEqual(res.status_code, 200)

## Make the tests conveniently executable
if __name__ == "__main__":
unittest.main()
```

## Test-Driven Development

Test-Driven Development (or TDD) is a software development paradigm used very commonly in production. It is based on a short, rapid development cycle in which tests are written before the executable code and constantly iterated on.

- Write test for specific application behavior.
- Run the tests and watch them fail.
- Write code to execute the required behavior.
- Test the code and rewrite as necessary to pass the test
- Refactor your code.
- Repeat - write your next test.

Often while pair programming, one partner will write the test and the other will write the executable code, after which the partner will switch. This process is helpful for checking assumptions about behavior and making sure all expected behavior is captured.

## Recap

At this point, you now know how to build an API that:

- Handles multiple kinds of requests
- Can handle a request body
- Can format both successful responses and error responses

And in this lesson, you also learned how to:

- Test your API using Unittest
- Build your API using Test-Driven Development (TDD)

By taking this approach in your future development, you'll be able to produce applications in a way that catches issues prior to putting them in front of the user, and in a way that makes it easier to maintain that quality as the app grows.

Next, we'll be looking at how to make your API usable by others, through writing API documentation. Onwards!
