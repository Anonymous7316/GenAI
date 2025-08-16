from pydantic import BaseModel,EmailStr,Field

class User(BaseModel):
    id: int
    name: str
    email: EmailStr

newUser: User = User(id=1, name="John Doe", email="abc@gmail.com")

print(newUser)