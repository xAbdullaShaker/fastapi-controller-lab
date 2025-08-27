# serializers/user.py

from pydantic import BaseModel

class UserSchema(BaseModel):
    username: str  # User's unique name
    email: str  # User's email address
    password: str  # Plain text password for user registration (will be hashed before saving)

    class Config:
        orm_mode = True  # Enables compatibility with ORM models

# Schema for returning user data (without exposing the password)
class UserResponseSchema(BaseModel):
    username: str
    email: str

    class Config:
        orm_mode = True

class UserLoginSchema(BaseModel):
    username: str  # Username provided by the user during login
    password: str  # Plain text password provided by the user during login

# New schema for the response (containing the JWT token and a success message)
class UserTokenSchema(BaseModel):
    token: str  # JWT token generated upon successful login
    message: str  # Success message

    class Config:
        orm_mode = True