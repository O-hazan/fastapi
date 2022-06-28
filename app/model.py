from pydantic import BaseModel, Field

## Models
class StatList(BaseModel):
    id: str
    age: int
    hight: int
    weight: int  
class StatEntry(BaseModel):
    age  : int = Field(..., example=1)
    hight  : int = Field(..., example=2)
    weight: int = Field(..., example=3)
class StatDelete(BaseModel):
    id: str = Field(..., example="Enter your id")
class StatUpdate(BaseModel):
    id        : str = Field(..., example="Enter your id")
    age: int = Field(..., example="Potine")
    hight : int = Field(..., example="Sambo")
    weight    : int = Field(..., example="M")
    


# class UserList(BaseModel):
#     id        : str
#     username  : str
#     password  : str
#     first_name: str
#     last_name : str
#     gender    : str
#     create_at : str
#     status    : str
# class UserEntry(BaseModel):
#     username  : str = Field(..., example="potinejj")
#     password  : str = Field(..., example="potinejj")
#     first_name: str = Field(..., example="Potine")
#     last_name : str = Field(..., example="Sambo")
#     gender    : str = Field(..., example="M")
# class UserUpdate(BaseModel):
#     id        : str = Field(..., example="Enter your id")
#     first_name: str = Field(..., example="Potine")
#     last_name : str = Field(..., example="Sambo")
#     gender    : str = Field(..., example="M")
#     status    : str = Field(..., example="1")

class Gallery(BaseModel):
    id: str
    path: str
    desc: str

class GalleryEntry(BaseModel):
    path  : str = Field(..., example=1)
    desc  : str = Field(..., example=2)
class GalleryDelete(BaseModel):
    id: str = Field(..., example="Enter your id")

class MessageEntry(BaseModel):
    title  : str = Field(..., example=1)
    sender  : str = Field(..., example=2)
    message  : str = Field(..., example=2)
class Message(BaseModel):
    id: str
    title: str
    sender: str
    message: str 
class MessageDelete(BaseModel):
    id: str = Field(..., example="Enter your id")
    
class NewsEntry(BaseModel):
    content  : str = Field(..., example=1)

class News(BaseModel):
    id: str
    content: str

class NewsDelete(BaseModel):
    id: str = Field(..., example="Enter your id")