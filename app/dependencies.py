from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .crud import get_meme

def get_meme_or_404(meme_id: int, db: Session = Depends(get_db)):
    db_meme = get_meme(db, meme_id)
    if db_meme is None:
        raise HTTPException(status_code=404, detail="Meme not found")
    return db_meme
