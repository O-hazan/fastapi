from pydantic import BaseModel, Field

## Models
class StatList(BaseModel):
    id: str
    age: int
    hight: int
    weight: int 
    # create_at : str

class StatEntry(BaseModel):
    # id: str = Field(..., example="potinejj")
    age  : int = Field(..., example=1)
    hight  : int = Field(..., example=2)
    weight: int = Field(..., example=3)
class StatUpdate(BaseModel):
    id        : str = Field(..., example="Enter your id")
    age: int = Field(..., example="Potine")
    hight : int = Field(..., example="Sambo")
    weight    : int = Field(..., example="M")
    


class UserList(BaseModel):
    id        : str
    username  : str
    password  : str
    first_name: str
    last_name : str
    gender    : str
    create_at : str
    status    : str
class UserEntry(BaseModel):
    username  : str = Field(..., example="potinejj")
    password  : str = Field(..., example="potinejj")
    first_name: str = Field(..., example="Potine")
    last_name : str = Field(..., example="Sambo")
    gender    : str = Field(..., example="M")
class UserUpdate(BaseModel):
    id        : str = Field(..., example="Enter your id")
    first_name: str = Field(..., example="Potine")
    last_name : str = Field(..., example="Sambo")
    gender    : str = Field(..., example="M")
    status    : str = Field(..., example="1")
class StatDelete(BaseModel):
    id: str = Field(..., example="Enter your id")