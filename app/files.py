from typing import Union

from fastapi import FastAPI, status, Form,File, UploadFile
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: Union[str, None] = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(UserBase):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)
    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut,status_code=status.HTTP_201_CREATED)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved

@app.post("/login/")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username}

"""
File Uploade and get file name details

"""

# @app.post("/files/")
# async def create_file(file: bytes = File()):
#     return {"file_size": len(file)}

@app.post("/files/")
async def create_file(
    file: bytes = File(), fileb: UploadFile = File(), token: str = Form()):
    return {
        "file_size": len(file),
        "token": token,
        "fileb_content_type": fileb.content_type,
    }

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    """
    you can uploadfile:

    - **name**: each file must have a name
    - **description**: you can get res.
    
    """
    return {"filename": file.filename}    