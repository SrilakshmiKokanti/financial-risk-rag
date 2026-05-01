from fastapi import APIRouter, UploadFile, File
from rag.indexer import build_index
import shutil

router = APIRouter()

@router.post('/ingest')
async def ingest(file: UploadFile = File(...)):
    with open(f'./docs/{file.filename}', 'wb') as out:
        shutil.copyfileobj(file.file, out)
    build_index()
    return {'message': f'Indexed {file.filename} successfully.'}