from fastapi import APIRouter, Depends, File, UploadFile, HTTPException
from ..dependencies import get_minio_client
from minio import Minio
import uuid

router = APIRouter(
    prefix="/upload",
    tags=["upload"],
)

@router.post("/", response_model=str)
async def upload_file(file: UploadFile = File(...), minio_client: Minio = Depends(get_minio_client)):
    try:
        filename = f"{uuid.uuid4()}_{file.filename}"
        minio_client.put_object(
            "memes",
            filename,
            file.file,
            length=-1,
            part_size=10*1024*1024,
            content_type=file.content_type
        )
        return filename
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
