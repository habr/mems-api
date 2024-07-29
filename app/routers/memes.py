from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import schemas, crud, dependencies

router = APIRouter(
    prefix="/memes",
    tags=["memes"],
    dependencies=[Depends(dependencies.get_db)],
)

@router.get("/", response_model=List[schemas.Meme])
def read_memes(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    memes = crud.get_memes(db, skip=skip, limit=limit)
    return memes

@router.get("/{meme_id}", response_model=schemas.Meme)
def read_meme(meme_id: int, meme: schemas.Meme = Depends(dependencies.get_meme_or_404)):
    return meme

@router.post("/", response_model=schemas.Meme)
def create_meme(meme: schemas.MemeCreate, db: Session = Depends(dependencies.get_db)):
    return crud.create_meme(db, meme)

@router.put("/{meme_id}", response_model=schemas.Meme)
def update_meme(meme_id: int, meme: schemas.MemeUpdate, db: Session = Depends(dependencies.get_db)):
    return crud.update_meme(db, meme_id, meme)

@router.delete("/{meme_id}", response_model=schemas.Meme)
def delete_meme(meme_id: int, db: Session = Depends(dependencies.get_db)):
    return crud.delete_meme(db, meme_id)
