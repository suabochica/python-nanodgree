# Python Nano Degree

- [ ] TO DO: Add program index

## Install Python on Ubuntu

### ⚠️ The Golden Rule: Always Use a Virtual Environment

Modern Ubuntu versions will block you with an "externally managed environment" error if you attempt to run pip install globally. To safely install project libraries (like Django, NumPy, or Requests), always create an isolated environment first.

Navigate to your project directory:

```bash
cd ~/my_project
```

Create the environment (naming it .venv):

```bash
python3 -m venv .venv
```

Activate it

```bash
source .venv/bin/activate
```

Your terminal prompt will now show (.venv) at the beginning

Safely install your packages inside the environment:

```bash
pip install requests
```

When you are finished working, simply type deactivate to exit.

## Install Postgres on Ubuntu

### Step 1: Add the Official PostgreSQL Repository

Ubuntu includes a dedicated helper script in its postgresql-common package that automatically imports the repository signing keys and sets up the official stable repository for you.

```sh
# Update your local package index
sudo apt update

# Install the repository automation tool
sudo apt install -y postgresql-common

# Run the official setup script to add the PGDG repository
sudo /usr/share/postgresql-common/pgdg/apt.postgresql.org.sh
```

### Step 2: Install PostgreSQL

Once the repository is added, update your package list again and install the core database server along with the `contrib` package (which provides crucial extra utilities like cryptographic functions and specialized data types).

```sh
sudo apt update
sudo apt install -y postgresql postgresql-contrib
```

Use code with caution.(Note: If you specifically need an older release, you can append the version number, like sudo apt install postgresql-16).

### Step 3: Enable and Verify the Service

Ensure that the database engine has started correctly and is configured to launch automatically whenever your server boots up.

```sh
# Enable PostgreSQL to launch on boot
sudo systemctl enable postgresql

# Start the service
sudo systemctl start postgresql

# Verify it is active and running
sudo systemctl status postgresql
```

### Step 4: Secure the Default Administrative Role

PostgreSQL utilizes a "role" system for authentication. By default, it creates a system user account called postgres.

To secure your installation, log into the local prompt and assign a strong password to this master administrative role:

Open the PostgreSQL prompt as the postgres user:

```sh
sudo -u postgres psql
```

Set a secure password for the root database user:

```sql
ALTER USER postgres WITH PASSWORD 'your_secure_password_here';
```

Type `\q` and press `Enter` to exit the prompt.

## Working with uv workspaces

A uv workspace lets you manage multiple interconnected Python packages inside a single repository using a shared lockfile and virtual environment.

?Inspired by Rust’s Cargo, workspaces allow you to group multiple apps or libraries together.

- _Single Lockfile_: All packages share one `uv.lock` file to keep dependency versions consistent.
- _Single Virtual Environment_: Commands use one shared .venv at the workspace root instead of separate environments for each sub-project.
- _Local Sources_: Packages can depend on each other locally without needing manual rebuilds.

)Most users on r/FastAPI agree that placing sub-packages inside a packages folder is the standard and most idiomatic layout.

## Basic Setup

To set up a workspace, create a root `pyproject.toml` file that defines your workspace members using globs:

```toml
[tool.uv.workspace]

members = [
    "packages/*"
]
```

```toml
[tool.uv.sources]
my-local-lib = { workspace = true }

```

## Common Commands

- `uv sync`: Syncs dependencies for the entire workspace or the package in your current directory.
- `uv run --package <name> <command>`: Runs a command targeting a specific workspace member.
- `uv lock`: Generates or updates the unified lockfile for all members.

## Standard `src` Layout

Each workspace member should follow the standard `src` layout:

```
package_name/
├── pyproject.toml
└── src/
    └── package_name/   ← importable package
        ├── __init__.py
        └── app.py
```

- `src/` prevents accidentally importing from the working directory during development.
- The inner `package_name/` directory is the actual importable module.

This is the convention expected by `uv_build` and most modern Python build backends.
