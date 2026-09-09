from fastapi import FastAPI, UploadFile, File
import os
import shutil

app = FastAPI()
ALLOWED_EXTENSIONS = {
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png"
}
MAX_FILE_SIZE = 5 * 1024 * 1024

@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    extension = os.path.splitext(
        file.filename
    )[1].lower()

    if extension not in ALLOWED_EXTENSIONS:

        return {
            "error": "File type not supported"
        }
    
    contents = await file.read()
    if len(contents) > MAX_FILE_SIZE:

        return {
            "error": "File size exceeds 5 MB"
        }
    
    file_path = f"FileUpload/uploads/{file.filename}"

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }