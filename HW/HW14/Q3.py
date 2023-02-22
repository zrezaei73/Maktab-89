import datetime
from pydantic import BaseModel, Field, validator, validate_email
from datetime import datetime


app = FastAPI()
users = []
class User(BaseModel):
    username: str
    password: str = Field(min_length=8)
    email: EmailStr = Field(regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$')
    date_joined: Field(datetime.date)

    @validator('username')
    def validate_username(cls, u):
        for user in uers:
            if user.username == u:
                raise ValueError('username already taken!')
        return users.append(u)

    @validator('email')
    def validate_email_unique(cls, e):
        for user in users:
            if user.email == e:
                raise ValueError('email already taken!')
        return users.append(e)

    @validator('email')
    def validate_email(cls, v):
        return EmailStr.validate(v)

