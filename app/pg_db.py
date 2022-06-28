import databases, sqlalchemy
import os
import psycopg2


## Postgres Database
# DATABASE_URL = 'postgresql://nlipxarhtxeupm:78a61e9596b97351abaad96528a80bc228e7413d28aef8c7dccc377f0997879c@ec2-34-242-84-130.eu-west-1.compute.amazonaws.com:5432/de2nkfj8f5c9r8'
DATABASE_URL = os.environ["DATABASE_URL"]
# added when trying to connect to Heroku

# conn = psycopg2.connect(DATABASE_URL, sslmode='require') 
# DATABASE_URL = "postgresql://myuser:123456@localhost:5432/postgres_database"
# postgresql://usertest:usertest222@127.0.0.1:5432/dbtest

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

# users = sqlalchemy.Table(
#     "py_users",
#     metadata,
#     sqlalchemy.Column("id"        , sqlalchemy.String, primary_key=True),
#     sqlalchemy.Column("username"  , sqlalchemy.String),
#     sqlalchemy.Column("password"  , sqlalchemy.String),
#     sqlalchemy.Column("first_name", sqlalchemy.String),
#     sqlalchemy.Column("last_name" , sqlalchemy.String),
#     sqlalchemy.Column("gender1"    , sqlalchemy.CHAR  ), 
#     sqlalchemy.Column("create_at" , sqlalchemy.String),
#     sqlalchemy.Column("status"    , sqlalchemy.CHAR  ),
# )

galleries = sqlalchemy.Table(
    "gallery",
    metadata,
    sqlalchemy.Column("id"    , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("path"   , sqlalchemy.String),
    sqlalchemy.Column("desc", sqlalchemy.String),
)

messages = sqlalchemy.Table(
    "message",
    metadata,
    sqlalchemy.Column("id"    , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("title"   , sqlalchemy.String),
    sqlalchemy.Column("sender", sqlalchemy.String),
    sqlalchemy.Column("message", sqlalchemy.String),

)


# stats = sqlalchemy.Table(
#     "stats",
#     metadata,
#     sqlalchemy.Column("id"    , sqlalchemy.String, primary_key=True),
#     sqlalchemy.Column("age"   , sqlalchemy.Integer),
#     sqlalchemy.Column("weight", sqlalchemy.Integer),
#     sqlalchemy.Column("hight" , sqlalchemy.Integer),
# )

stats = sqlalchemy.Table(
    "stat",
    metadata,
    sqlalchemy.Column("id"    , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("age"   , sqlalchemy.Integer),
    sqlalchemy.Column("weight", sqlalchemy.Integer),
    sqlalchemy.Column("hight" , sqlalchemy.Integer),
    # sqlalchemy.Column("created_at" , sqlalchemy.String),

)


news = sqlalchemy.Table(
    "feed",
    metadata,
    sqlalchemy.Column("id"    , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("content"   , sqlalchemy.String),
)

engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)