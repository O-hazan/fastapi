import databases, sqlalchemy
import os
import psycopg2


## Postgres Database

# DATABASE_URL = 'postgresql://smjzhatreukulg:f0814424648525098f9c827986b6d1c8fe00b1cb3edf2e6cc90b04f1bdf42d3c@ec2-3-219-52-220.compute-1.amazonaws.com:5432/d2ss7j4k7frufr'

DATABASE_URL = 'postgresql://blxsdwppssurjd:a66c484545a15835d10746ad930d8686d304e7a06defff5a5dab0306b230d869@ec2-54-228-32-29.eu-west-1.compute.amazonaws.com:5432/d28hmilckokoaq'
# DATABASE_URL = "postgresql://myuser:123456@localhost:5432/postgres_database" 
# DATABASE_URL = os.environ["DATABASE_URL"]  
# added when trying to connect to Heroku - related to connection from local to postgres docker
# conn = psycopg2.connect(DATABASE_URL, sslmode='require') 


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