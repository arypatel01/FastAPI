from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pathlib import Path

app = FastAPI()

@app.get("/download/pdf")
def download_pdf():
    file_path = Path("file.pdf")

    if not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="File Not Found"
        )

    return FileResponse(
        path=file_path,
        filename="chapter3.pdf",
        media_type="application/pdf"
    )

@app.get("/download/image")
def download_image():
    file_path = Path("image.png")

    if not file_path.is_file():
        raise HTTPException(
            status_code=404,
            detail="File Not Found"
        )

    return FileResponse(
        path=file_path,
        filename="marks.png",
        media_type="image/png"
    )