import datetime, uuid
from email import message
from distutils.log import error
# from os import gallery

from os import stat
import app.model as mdStat
from app.pg_db import database, galleries
from app.pg_db import database, news

# import app.model as mdGallery

from app.pg_db import database, stats
from app.pg_db import database, messages

from typing import List
from passlib.context import CryptContext
from typing import Optional
from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from fastapi import Response, HTTPException
from fastapi.responses import FileResponse
import os
from random import randint

import shutil


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

IMAGEDIR = "app/files/"


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

# @app.on_event("startup")
# async def startup():
#     await database.connect()
    
@app.on_event("startup")
async def startup():
    if not database.is_connected:
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


# Not working Need to try and fix it

# @app.post("/video")
# async def upload_video(file: UploadFile = File(...)):
#     with open(f'{file.filename}', "wb") as buffer:
#         shutil.copyfileobj(file.file, buffer) 
#     return {"file_name": file.filename}

# @app.post("/image")
# async def upload_image(file: List[UploadFile] = File(...)):
#     for img in file:
#         with open(f'{img.filename}', "wb") as buffer:
#             shutil.copyfileobj(img.file, buffer) 
#         return {"file_name": 'good'}
    
    
   
    # WORKS!!!!
@app.post("/files/") 
async def create_file(file: bytes = File()):
    return {"file_name": len(file)}




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
   
   
   
   
   
   
 # lksjdasjdljkhadjsdas

@app.post("/images/")
async def create_upload_file(file: UploadFile = File(...)):

    file.filename = f"{file.filename}"
    contents = await file.read()  # <-- Important!

    # example of how you can save the file
    with open(f"{IMAGEDIR}{file.filename}", "wb") as f:
        f.write(contents)

    return {"filename": file.filename}


@app.get("/images/{imageId}")
async def read_random_file():

    # get a random file from the image directory
    files = os.listdir(IMAGEDIR)
    random_index = randint(0, len(files) - 1)

    path = f"{IMAGEDIR}{files[random_index]}"
    
    # notice you can use FileResponse now because it expects a path
    return FileResponse(path)
   
   
   
@app.get("/gallery", response_model=List[mdStat.Gallery], tags=["gallery"])
async def get_gallery():
    query = galleries.select()
    return await database.fetch_all(query)
 
@app.delete("/gallery/{galleryId}", tags=["gallery"])
async def delete_gallery(gallery: mdStat.GalleryDelete):
    query = galleries.select().where(galleries.c.id == gallery.id)
    result = await database.execute(query)
    message =[]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Image with ID {gallery.id} not found"
        )
    else:
        query = galleries.delete().where(galleries.c.id == gallery.id)
        await database.execute(query)
        message.append({
        "status" : True,
        "message": "This image has been deleted successfully." 
    })

    return message[0]

    
@app.post("/gallery", response_model=mdStat.Gallery, tags=["gallery"])
async def add_gallery(gallery: mdStat.GalleryEntry):     
    gID   = str(uuid.uuid4().int & (1<<64)-19518405196747027403)
    query = galleries.insert().values(
        id     = gID,
        path    = gallery.path,
        desc = gallery.desc,
    ) 
    
    await database.execute(query)
    return  {
        "id": gID,
        "path": gallery.path,
        "desc": gallery.desc,
    }
    
    
    # This is a start 
@app.get("/message", response_model=List[mdStat.Message], tags=["message"])
async def get_message():
    query = messages.select()
    return await database.fetch_all(query)
 
@app.delete("/message/{messageId}", tags=["message"])
async def delete_message(message: mdStat.MessageDelete):
    query = messages.select().where(messages.c.id == message.id)
    result = await database.execute(query)
    message1 =[]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"Image with ID {message.id} not found"
        )
    else:
        query = messages.delete().where(messages.c.id == message.id)
        await database.execute(query)
        message1.append({
        "status" : True,
        "message": "This message has been deleted successfully." 
    })

    return message1[0]

    
@app.post("/message", response_model=mdStat.Message, tags=["message"])
async def add_message(message: mdStat.MessageEntry):     
    gID   = str(uuid.uuid4().int & (1<<64)-19518405196747027403)
    query = messages.insert().values(
        id     = gID,
        title    = message.title,
        sender = message.sender,
        message = message.message,
    ) 
    
    await database.execute(query)
    return  {
        "id": gID,
        "title": message.title,
        "sender": message.sender,
        "message": message.message,

    }  


@app.get("/feed", response_model=List[mdStat.News], tags=["feed"])
async def get_news():
    query = news.select()
    return await database.fetch_all(query)
 
@app.delete("/feed/{feedId}", tags=["feed"])
async def delete_news(feed: mdStat.NewsDelete):
    query = news.select().where(news.c.id == feed.id)
    result = await database.execute(query)
    message1 =[]
    if not result:
        raise HTTPException(
            status_code=404, detail=f"news with ID {news.id} not found"
        )
    else:
        query = news.delete().where(news.c.id == feed.id)
        await database.execute(query)
        message1.append({
        "status" : True,
        "message": "This news has been deleted successfully." 
    })
    return message1[0]
  
@app.post("/feed", response_model=mdStat.News, tags=["feed"])
async def add_news(feed: mdStat.NewsEntry):     
    gID   = str(uuid.uuid4().int & (1<<64)-19518405196747027403)
    query = news.insert().values(
        id     = gID,
        content    = feed.content,
    ) 
    await database.execute(query)
    return  {
        "id": gID,
        "content": feed.content,
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