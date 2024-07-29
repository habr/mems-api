from sqlalchemy import Column, Integer, String, Text
from .database import Base

class Meme(Base):
    __tablename__ = "memes"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(Text, nullable=False)
    image_url = Column(String, nullable=False)