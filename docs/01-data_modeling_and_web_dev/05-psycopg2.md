# psycopg2

## String Interpolation

We can use string interpolation to compose a SQL query using python strings. Two methods for doing so include:

- Using `%s`, passing in a tuple as the 2nd argument in `cursor.execute()`
- Using named string parameters `%(foo)s`, passing in a dictionary instead.

Check the next snippet to illustrate the previous definitions:

```python
import psycopg2

connection = psycopg2.connect('dbname=example')

cursor = connection.cursor()

cursor.execute('DROP TABLE IF EXISTS table2;')

cursor.execute('''
  CREATE TABLE table2 (
    id INTEGER PRIMARY KEY,
    completed BOOLEAN NOT NULL DEFAULT False
  );
''')

cursor.execute('INSERT INTO table2 (id, completed) VALUES (%s, %s);', (1, True))

SQL = 'INSERT INTO table2 (id, completed) VALUES (%(id)s, %(completed)s);'

data = {
  'id': 2,
  'completed': False
}
cursor.execute(SQL, data)

connection.commit()

connection.close()
cursor.close()
```

## Fetch Data

psycopg2 has the next methods to fetching results in our database; `fetchone()`, `fetchmany(1)` and `fetchall()`. The next snippet illustrate the use cases for these commands.

```python
cursor.execute('SELECT * from table2;')
result = cursor.fetchall()
print(result)

cursor.execute("INSERT INTO table2 (id, description) VALUES (%s,%s);' (3,True)")

cursor.execute('SELECT * from table2;')
---
result2 = cursor.fetchone()
print('fetchone ' , result2)
---
result = cursor.fetchmany(2)
print('fetchmany ' , result2)
---
result3 = cursor.fetchone()
print('fetchone ' , result3)
```

## Commands

```txt
## conn = pyscopg2.connect(...)
## cursor = conn.cursor()

## cursor.execute(SQL command string)
## cursor.commit()
## cursor.rollback()

## cursor.fatchall()
## cursor.fetchman(3)
## cursor.fetchone()
## cursor.close()
## conn.close()

```

## Conclusion

Writing SQL directly is a fairly clunky way of doing web development. It's usefull to learn some higher-level libraries that let us interact with a database, using Python classes and expressions. Let's get to learn one of the most powerful Python libraries for interacting with databases: SQLAlchemy.
Steps for getting a database-backed web application up and running

Here is an overview of the list of tasks we'll need to do for a given web app to run with a database.

1. **Create a database**. Using createdb in Postgres.

2. **Establish a connection to the database**. We can connect to a Postgres server from a Python web server using pyscopg2 with psycopg2.connect().

3. **Define and create your data schema**. Execute CREATE TABLE commands to create the tables and define the schema (attributes, data types, etc) that will define what data gets housed for our web app.

4. **Seed the database with initial data.** (Optional) Give the database some initial data, e.g. test data for doing local development.

5. **Create routes and views.** Create routes in our server that will serve pages (views) to the client. Write up our HTML, CSS, and Javascript in our views. Then finally, to get our web app running,

6. **Run the server.** Get the web server running.

7. **Deploy the server to the web.** That is, generally, how we would build a web application backed by a database.
