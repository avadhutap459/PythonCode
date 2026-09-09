from typing import List
from fastapi import FastAPI,UploadFile, File

app = FastAPI()

@app.post("/upload-multiple")
async def upload_multiple_files(
    files: List[UploadFile] = File(...)
):

    uploaded_files = []

    for file in files:

        uploaded_files.append(
            file.filename
        )

    return {
        "files": uploaded_files
    }