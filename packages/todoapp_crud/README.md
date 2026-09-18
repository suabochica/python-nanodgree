# TODO CRUD

Start the server with the next command:

```sh
uv run --package todoapp_crud flask --app todoapp_crud.app run
```

## Database Migrations

Initialize Flask-Migrate (first time only):

```sh
uv run --package todoapp_crud flask --app todoapp_crud.app db init
```

Generate a migration after model changes:

```sh
uv run --package todoapp_crud flask --app todoapp_crud.app db migrate -m "description of changes"
```

Apply migrations to the database:

```sh
uv run --package todoapp_crud flask --app todoapp_crud.app db upgrade
```

Rollback the last migration:

```sh
uv run --package todoapp_crud flask --app todoapp_crud.app db downgrade
```
