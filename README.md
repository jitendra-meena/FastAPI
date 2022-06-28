# FastAPI

FastAPI is a modern, high-performance web framework for building APIs with Python based on standard type hints. It has the following key features: Fast to run: It offers very high performance, on par with NodeJS and Go, thanks to Starlette and pydantic

<!-- # DataBase-Scaling
Scaling in DBMS is the ability to expand the capacity of a database system in order to support larger amounts or requests and/or store more data without sacrificing performance -->


# Basic Setup

1. Create your virtual environment
2. Create a project directry
3. git clone remote url

# Install Dependencies
  ```bash
  pip install -r requirements.txt

  Dependencies:
    python ≥ 3.5
    fastapi
    pydantic
    fastapi-sqlalchemy
    alembic
    psycopg2
    uvicorn
  ```


# Pydantic
pydantic enforces type hints at runtime, and provides user friendly errors when data is invalid. We can define how data should be in pure python and validate it easily with pydantic.

# ASGI specification
ASGI (Asynchronous Server Gateway Interface) is a spiritual successor to WSGI, intended to provide a standard interface between async-capable Python web servers, frameworks, and applications.

# Uvicorn server
Uvicorn is a lightning-fast ASGI server, built on uvloop and httptools.

# Alembic
Alembic is a lightweight database migration tool for usage with the SQLAlchemy Database Toolkit for Python



# DATABASES = 
    Create an environment file and name it .env.
    Inside the .env file, do the following:
    
  ```bash
    DATABASE_URI = 'postgresql://postgres:<password>@localhost/<name_of_the_datbase>'
  ```
 


# Migrate Database
  It will create a folder called alembic. Inside the folder, go to the env.py file and do the following:
  ```bash
  alembic init alembic
  ```
  
  Run the following code to enable migration:

  ```bash
  alembic upgrade head

  alembic revision --autogenerate -m "New Migration"

  ```

# Run Server:
```bash
>>To kickstart the app, use:
```

```bash
uvicorn main:app --reload

```

# Jitendra Meena Copyright ©2022