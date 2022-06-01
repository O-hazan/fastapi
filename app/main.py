import datetime, uuid
from email import message
from distutils.log import error
from os import stat
import app.model as mdStat

from app.pg_db import database, stats
from fastapi import FastAPI, HTTPException  
from typing import List
from passlib.context import CryptContext
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI, Response


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


app = FastAPI(
    docs_url="/api/v2/docs",
    redoc_url="/api/v2/redocs",
    title="Core API",
    description="New Framework of Python",
    version="2.0",
    openapi_url="/api/v2/openapi.json",
    
)
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

# @app.get("/users", response_model=List[mdUser.UserList], tags=["Users"])
# async def find_all_users():
#     query = users.select()
#     return await database.fetch_all(query)

# @app.post("/users", response_model=mdUser.UserList, tags=["Users"])
# async def register_user(user: mdUser.UserEntry):
#     gID   = str(uuid.uuid1())
#     gDate =str(datetime.datetime.now())
#     query = users.insert().values(
#         id = gID,
#         username   = user.username,
#         password   = pwd_context.hash(user.password),
#         first_name = user.first_name,
#         last_name  = user.last_name,
#         gender     = user.gender,
#         create_at  = gDate,
#         status     = "1"
#     ) 

    # await database.execute(query)
    # return {
    #     "id": gID,
    #     **user.dict(),
    #     "create_at":gDate,
    #     "status": "1"
    # }

# @app.get("/users/{userId}", response_model=mdUser.UserList, tags=["Users"])
# async def find_user_by_id(userId: str):
#     query = users.select().where(users.c.id == userId)
#     return await database.fetch_one(query)

# @app.put("/users", response_model=mdUser.UserList, tags=["Users"])
# async def update_user(user: mdUser.UserUpdate):
#     gDate = str(datetime.datetime.now())
#     query = users.update().\
#         where(users.c.id == user.id).\
#         values(
#             first_name = user.first_name,
#             last_name  = user.last_name,
#             gender     = user.gender,
#             status     = user.status,
#             create_at  = gDate,
#         )
#     await database.execute(query)

#     return await find_user_by_id(user.id)

# @app.delete("/users/{userId}", tags=["Users"])
# async def delete_user(user: mdUser.UserDelete):
#     query = users.delete().where(users.c.id == user.id)
#     await database.execute(query)

#     return {
#         "status" : True,
#         "message": "This user has been deleted successfully." 
#     }

# @app.get("/courses", tags=["Courses"])
# def find_all_courses():
#     return "List all courses."

# statsobj = [
#     {"age": 9, "hight": 68, "weight": 9, "id": 1},
#     {"age": 12, "hight": 74, "weight": 13, "id": 2},
#     {"age": 18, "hight": 89, "weight": 16, "id": 3},
#     {"age": 21, "hight": 92, "weight": 199, "id": 5}, 

# ] 

# @app.get("/stats")
# async def get_stat():
#     return stats


@app.get("/stats", response_model=List[mdStat.StatList], tags=["stat"])
async def get_stat():
    query = stats.select()
    return await database.fetch_all(query)

@app.get("/stats/{statId}", response_model=mdStat.StatList, tags=["stat"])
async def find_stat_by_id(statId: str):
    query = stats.select().where(stats.c.id == statId)
    return await database.fetch_one(query)

@app.delete("/stats/{statId}", tags=["stat"])
async def delete_stat(stat: mdStat.StatDelete):
    query = stats.select().where(stats.c.id == stat.id)
    result = await database.execute(query)
    message =[]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Stats with ID {stat.id} not found"
        )
    else:
        query = stats.delete().where(stats.c.id == stat.id)
        await database.execute(query)
        message.append({
        "status" : True,
        "message": "This stat has been deleted successfully." 
    })

    return message[0]
    
@app.post("/stats", response_model=mdStat.StatList, tags=["stat"])
async def add_stat(stat: mdStat.StatEntry):     
    gID   = str(uuid.uuid4().int & (1<<64)-19518405196747027403)
    query = stats.insert().values(
        id     = gID,
        age    = stat.age,
        weight = stat.weight,
        hight  = stat.hight,
    ) 
    

    await database.execute(query)
    return  {
        "id": gID,
        "age": stat.age,
        "weight": stat.weight,
        "hight": stat.hight
    }

        





    
# @app.put("/stats", response_model=mdStat.StatList, tags=["stat"])
# async def update_stat(stat: mdStat.StatUpdate):
#     gDate = str(datetime.datetime.now())
#     query = stats.update().\
#         where(stats.c.id == stat.id).\
#         values(
#             age = stat.age,
#             weight  = stat.weight,
#             hight     = stat.hight,
#             create_at  = gDate,
#         )
#     await database.execute(query)

#     return await find_stat_by_id(stat.id)

    

# @app.post("/stats", response_model=mdStat.StatList, tags=["stat"])
# async def register_stat(stat: mdStat.StatEntry):
#     gID   = str(uuid.uuid1())
#     gDate =str(datetime.datetime.now())
#     query = stats.insert().values(
#         id = gID,
#         age   = stat.age,
#         weight = stat.weight,
#         hight  = stat.hight,
#         create_at  = gDate,
#     ) 

#     await database.execute(query)
#     return {
#         "id": gID,
#         **stat.dict(),
#         "create_at":gDate,
#     }
    
    
    # @app.delete("/users/{userId}", tags=["Users"])
# async def delete_user(user: mdUser.UserDelete):
#     query = users.delete().where(users.c.id == user.id)
#     await database.execute(query)

#     return {
#         "status" : True,
#         "message": "This user has been deleted successfully." 
#     }

#  @app.get("/users", response_model=List[mdUser.UserList], tags=["Users"])
# async def find_all_users():
#     query = users.select()
#     return await database.fetch_all(query)

# app = FastAPI()



    
# class Stat(BaseModel):
#     age: int
#     hight: int
#     weight: int 
   
# stats = [
#     {"age": 9, "hight": 68, "weight": 9, "id": 1},
#     {"age": 12, "hight": 74, "weight": 13, "id": 2},
#     {"age": 18, "hight": 89, "weight": 16, "id": 3},
#     {"age": 21, "hight": 92, "weight": 199, "id": 4}, 

# ] 

# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# @app.get("/stats")
# async def get_stat():
#     return stats
    
# @app.post("/stats1/")
# async def update_stats(stat: Stat):
#     stats.append(stat)
#     return stats 


# @app.post("/deletestats/")
# async def update_stats(stat: Stat):
#     stats.append(stat)
#     return stats 