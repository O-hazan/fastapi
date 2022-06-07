import databases, sqlalchemy
import os

## Postgres Database
DATABASE_URL = os.environ["DATABASE_URL"]
#DATABASE_URL = "postgresql://myuser:123456@localhost:5432/postgres_database"
# postgresql://usertest:usertest222@127.0.0.1:5432/dbtest

database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "py_users",
    metadata,
    sqlalchemy.Column("id"        , sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("username"  , sqlalchemy.String),
    sqlalchemy.Column("password"  , sqlalchemy.String),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name" , sqlalchemy.String),
    sqlalchemy.Column("gender1"    , sqlalchemy.CHAR  ), 
    sqlalchemy.Column("create_at" , sqlalchemy.String),
    sqlalchemy.Column("status"    , sqlalchemy.CHAR  ),
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



engine = sqlalchemy.create_engine(
    DATABASE_URL
)
metadata.create_all(engine)