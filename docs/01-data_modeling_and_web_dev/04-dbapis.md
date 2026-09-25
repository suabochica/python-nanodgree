Takeaways
---

We will sometimes want to interact with our database and use its results in a specific programming language. E.g. to build web applications or data pipelines in a specific language (Ruby, Python, Javascript, etc.). That's where DBAPIs come in.

A database API:

- provides a standard interface for one programming language (like Python) to talk to a relational database server.
- Is a low-level library for writing SQL statements that connect to a database
- Is also known as database adapters
- Different DBAPIs exist for every server framework or language + database system
- Database adapters define a standard for using a database (with SQL) and using the results of database queries as input data in the given language.

Turn a selected `SELECT * from some_table;` list of rows into an array of objects in JavaScript for say a NodeJS adapter; or a list of tuples in Python for a Python adapter.

Examples across languages and server frameworks:

- For Ruby (e.g. for Sinatra, Ruby on Rails): pg(opens in a new tab)
- For NodeJS: node-postgres(opens in a new tab)
- For Python (e.g. for Flask, Django): pyscopg2(opens in a new tab)

psycopg2 is the focus of this course since we are using a Python stack.
