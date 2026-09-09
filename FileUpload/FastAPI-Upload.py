from pathlib import Path
from fastapi import FastAPI, UploadFile, File

app = FastAPI()

UPLOAD_DIR = Path("D:\\Python\\Python-Sample\\FileUpload\\uploads1")


@app.post("/upload")
async def upload_file(
    file: UploadFile = File(...)
):

    # Create directory if it doesn't exist
    UPLOAD_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    # Create file path
    file_path = UPLOAD_DIR / file.filename

    # Write binary file
    with open(file_path, "wb") as output:

        while chunk := await file.read(1024 * 1024):

            output.write(chunk)

    return {
        "message": "File uploaded successfully",
        "filename": file.filename
    }