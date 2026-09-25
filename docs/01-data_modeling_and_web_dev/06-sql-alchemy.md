# SQL Alchemy

In this lesson, we will introduce SQL Alchemy, a library in Python that can enable effective and efficient DB interaction for your app. We will specifically look at:

- How the components of SQL Alchemy and ORM are structured
- What are dialects
- What is a connection pool
- How does the core engine work
- How classes and tables are mapped
- How models are defined
- How data types are handled
- How to define constraints

SQLAlchemy is the most popular open-source library for working with relational databases from Python.

It is one type of ORM library, AKA an Object-Relational Mapping library, which provides an interface for using object-oriented programming(opens in a new tab) to interact with a database.

Other ORM libraries that exist across other languages include popular choices like javascript libraries Sequelize(opens in a new tab) and Bookshelf.js(opens in a new tab) for NodeJS applications, the ruby library ActiveRecord(opens in a new tab), which is used inside Ruby on Rails(opens in a new tab), and CakePHP(opens in a new tab) for applications written on PHP, amongst many other such ORMs.

> ###### Note on ORMs: are they a "best practice"?
>
> Using an ORM to interact with your database is one of many useul approaches for how you can have layers of abstraction in your web application allowing it to interact with a database more easily. Additionally,there are numerous query builder libraries you can use that are somewhere between talking to a database directly (with a database driver library like pyscopg2), and using an ORM. An ORM is considered to be the highest possible level of abstraction you can add to a web application for database management. Query Builder libraries are right there in the middle. There are mixed reactions about whether ORMs are a best practice approach in all cases, such as this opinion on "Why you should avoid ORMs"(opens in a new tab).
>
> SQLAlchemy offers multiple levels of abstraction between the database driver and the ORM, so you can customize the development of your web application. These granular levels of abstraction are one of the reasons that has led to its widespread popularity.

Below a list of some features offered by SQLAlchemy.

- Features function-based query construction: allows SQL clauses to be built via Python functions and expressions.
- Avoid writing raw SQL. It generates SQL and Python code for you to access tables, which leads to less database-related overhead in terms of the volume of code you need to write overall to interact with your models.
- Moreover, you can avoid sending SQL to the database on every call. The SQLAlchemy ORM library features automatic caching, caching collections, and references between objects once initially loaded.

The diagram below can give you insight into where SQL Alchemy and ORM are in the big picture.

![SQLAlchemy diagram](../images/alchorm.png)

### Takeaways

- Without SQLAlchemy, we'd only use a DBAPI to establish connections and execute SQL statements. Simple, but not scalable as complexity grows.
- SQLAlchemy offers several layers of abstraction and convenient tools for interacting with a database.

SQLAlchemy vs psycopg2:

- SQLAlchemy generates SQL statements
- psycopg2 directly sends SQL statements to the database.
- SQLAlchemy depends on psycopg2 or other database drivers to communicate with the database, under the hood.

SQLALchemy lets you traverse through all 3 layers of abstraction to interact with your database. Can stay on the ORM level. Can dive into database operations to run customized SQL code specific to the database, on the Expressions level. Can write raw SQL to execute, when needed, on the Engine level and it can be more simply use psycopg2 in this case.

Here's my opinion on interacting with databases using good design practice.

- Keep your code Pythonic. Work in classes and objects as much as possible.
- Makes switching to a different backend easy in the future.
- Avoid writing raw SQL until absolutely necessary

Next, we'll go over every layer of abstraction in SQLAlchemy and what they offer.

![SQL layers](../images/sqla.png)

## The Dialect

When we're using SQLAlchemy, we can forget generally speaking about the database system that we're using, allowing us to use SQL lite or Postgres or generally switch out the database system whenever we need to.

> The reason why we can do this is because of the dialects

Dialects allow the flavor of SQL that we're using to get abstracted away from us because the dialect's layer controls the quirks and flavor of the specific database system that we're using.

## The Connection Pool

With a connection pool, the opening and closing of connections and which connection you are using when you're executing statements within a session are completely abstracted away from you.

As a result of having a connection pool:

- Connections are easily reused after they are started. This avoids the problem of continually opening and closing connections every time we want to make data changes to our database.
- A connection pool also easily handles dropped connections for us, for example, when we have network issues.
- It also helps us avoid doing very many small calls to the database when we're continually assigning changes to the database, which can be very slow.

## The Engine

The 1 of 3 main layers for how you may choose to interact with the database. Is the lowest level layer of interacting with the database, and is much like using the DBAPI directly. Very similar to using psycopg2, managing a connection directly. Moreover,

- The Engine in SQLAlchemy refers to both itself, the Dialect and the Connection Pool, which all work together to interface with our database.
- A connection pool gets automatically created when we create an SQLAlchemy engine.

## SQL Expressions

Instead of sending raw SQL (using the Engine), we can compose python objects to compose SQL expressions, instead. SQL Expressions still involves using and knowing SQL to interact with the database.

## SQLAlchemy ORM (optional)

SQLALchemy ORM is the highest level of abstraction and lets you compose SQL expressions by mapping python classes of objects to tables in the database. It wraps the SQL Expressions and Engine to work together to interact with the database, and, it will be used in this course, so we can know how to use ORM libraries in general.

Moreover, SQLAlchemy is split into two libraries:

- SQLAlchemy Core
- SQLAlchemy ORM (Object Relational Mapping library). SQLALchemy ORM is offered as an optional library, so you don't have to use the ORM in order to use the rest of SQLAlchemy.
  - The ORM uses the Core library inside
  - The ORM lets you map from the database schema to the application's Python objects
  - The ORM persists objects into corresponding database tables

## Summary

The next image summarizes the layer of abstraction of SQLAlchemy:

![SQLAlchemy Layer of Abstraction](../images/sqlalchemy-layers-of-abstraction.png)

## Mapping Between Tables and classes

Let's say that we have a class named Human. The Human class allows us to instantiate an instance of a human being, that has

```python
class Human:
   def __init__(self, first_name, last_name, age):
       self.first_name = first_name
       self.last_name = last_name
       self.age= age

```

We can recall object-oriented programming and instantiating a class is very much like instantiating a collection of objects that could exist.

For example, let's say that we want to create two human beings, named Sarah and Bob. We would do that by creating object instances of the Human class, where we then pass in the attributes that define a single human being.

```python
sarah = new Human("Sarah","Silverman",48)
bob = new Human("Bob","Saget",54)
```

For example, we could have humans Sarah Silverman of age 48 be one instance of a human being, and another instance of a human being be Bob Saget of age 54. Sarah and Bob both differ from each other because they have different attributes of their class Human, but they're both humans.

Similarly, you can think of a table that we create in a database, as a template for future rows to come, or in this case, for future human objects that could exist. That template specifies the types of columns that we would have on a table, which is equivalent to the types of attributes that we would list on a Human class. So if a human can have a first name and last name and age, then in the table, that means that we would specify those as the columns of that table. The columns of the table are essential for all the common attributes that exist across all humans or all records inside of that table.

```sql
CREATE TABLE humans (
   id INTEGER PRIMARY KEY,
   first_name VARCHAR,
   last_name VARCHAR,
   age INTEGER
);

```

In order to create the records for Sarah and Bob, we would simply list Sarah and Bob and their values for every column, as rows within the table. So it's easy to see that the way that we instantiate a class in Python, or in other languages, is very similar to the way that we would instantiate a table in a Relational Database System. The way that we would create instances of that class or objects of that class, which have different attributes and different values for each of those attributes, is a very similar process, to the way that we would create rows within the table, that will have different values for every column.

![Classes and database tables are similar](../images/pysql.png)

A column maps to an attribute on a class. The table schema matches to the class definition of the class as a whole, and rows within a table, match to records or objects that are instances of a class. So the takeaways are, tables mapped to classes, table records mapped to class objects, and table columns mapped to the attributes within that class.

In short:

- Tables maps to classes.
- Tables records maps to objects.
- Tables columns maps to attributes.

## Lesson review

In this lesson, we introduced SQL Alchemy, theoretically as well as in practice. We looked specifically look at:

- How the components of SQL Alchemy and ORM are structure
- What are dialects
- What is a connection pool
- How does the core engine work
- How classes and tables are mapped
- How models are defined
- How data types are handled
- How to define constraints

The next pyramid summarize the SQLAlchemy contents:

![SQLAlchemy layers](../images/sqlalchemy-layers.png)
