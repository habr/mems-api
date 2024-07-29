from pydantic import BaseModel, HttpUrl

class MemeBase(BaseModel):
    text: str

class MemeCreate(MemeBase):
    image_url: HttpUrl

class MemeUpdate(MemeBase):
    pass

class Meme(MemeBase):
    id: int
    image_url: HttpUrl

    class Config:
        orm_mode = True
