# CRUD

In this lesson, you will learn about the following topics, and also apply each to an actual app that you will be creating:

- Model View Controller
- Handling Input
- Getting user data in Flask
- Using AJAX to send data back to Flask
- Using sessions in controllers

So far, we've built up a lot of the conceptual foundation we'd need to understand how to do real-world web development across the stack. In these next series of lessons from now until the end of this course, we'll pivot to becoming very hands-on, building a fully functional application from start to end.

Following every screencast, an interactive workspace will be provided so you can **follow along in coding** the steps of building out this To-Do application. You'll be building out the same application from now until the end of this course across these next 3 lessons. The starter code is provided above every instance of your workspace, in case you make a mistake somewhere and want to start from a clean slate at any point.

Below, it's share the equivalence between the user actions, the SLQ instructions and the ORM instructions:

- CREATE -> INSERT -> DB.SESSION.ADD(USER1)
- READ -> SELECT -> User.query.all()
- UPDATE -> UPDATE -> user1.foo = 'new value'
- DELETE -> DELETE -> db.session.delete(user1)

In summary, here are the skills we'll master over these next 3 lesson as we build out this application:

- Traversing across all layers of our backend stack, from our backend server in Flask to our database in Postgres, by understanding mappings between user operations, to the ORM, to the SQL executed on a database.
- Developing using the MVC Model-View-Controller pattern, for architecting out our application
- Handling changes to our data schema over time
- Modeling relationships between objects in our web application
- Implementing Search

We'll cover these skills through a hands-on approach by building out our to-do application across these next 3, final lessons of this section!
