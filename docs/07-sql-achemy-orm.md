# SQL Alchemy ORM

SQLAlchemy and SQLAlchemy ORM is one of the most popular libraries for building and interacting with models in a Python environment. It's a very well-developed library that offers flexibility and versatility and how we can work with models in our web applications.

In order to successfully maneuver around it and debug feature issues that we may have with our models in our web applications., we'll need to learn concepts like

- The object life cycle
- Sessions
- Inquiry object in SQLAlchemy

## The Object Life Cycle

Within a session, we create **transactions** every time we want to commit work to the database. Proposed changes are not immediately committed to the database and instead, go through stages to allow for undos. The ability to undo is allowed via `db.session.rollback()`

### Stages:

1. **Transient**: an object exists, it was defined....but not attached to a session or database (yet).
1. **Pending**: Some type of action has occurred but we have not yet decided to make it permanent yet. An object was attached to a session. "Undo" becomes available via `db.session.rollback()`. This means we can still clear any work that has been done so far. An object stays in this state until a flush happens!
1. **Flushed**: Translating actions(pending changes) into SQL commands that are ready to be committed. Nothing happens in the actual database yet. The only thing that can do that is 'commit'
1. **Committed**: manually called for all pending changes to persist to the database permanently.


## Flush

A flush takes pending changes and translates them into commands ready to be committed. It occurs; when you call `query` or on `db.session.commit()`.

A commit leads to persisted changes on the database + lets the db.session start with a new transaction.

When a statement has been flushed already, SQLAlchemy knows not to do the work again of translating actions to SQL statements.

The next images is a summary of the explanation exposed in this file:

![Object LifeCycle](../images/objectlc.png
)
