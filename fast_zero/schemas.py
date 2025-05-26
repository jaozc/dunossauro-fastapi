from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str
    docs_url: str
    redoc_url: str


class HTMLResponse(BaseModel):
    html_content: str
    content_type: str = 'text/html'


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str


class UserPublic(BaseModel):
    id: int
    name: str
    email: EmailStr


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
