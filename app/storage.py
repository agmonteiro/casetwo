from pathlib import Path
from uuid import uuid4
from PIL import Image
from fastapi import UploadFile, HTTPException

# =========================
# Image Uploading/Filtering

UPLOAD_DIR = Path("app/uploads")
UPLOAD_DIR.mkdir(exist_ok=True)


ALLOWED_EXTENSIONS = {
    ".png",
    ".jpg",
    ".jpeg",
    ".jxl"
}


async def save_image(file: UploadFile) -> str:
    extension = Path(file.filename).suffix.lower()

    if extension not in ALLOWED_EXTENSIONS:
        raise HTTPException(
            status_code=400,
            detail="Unsupported image format."
        )

    content = await file.read()

    if extension != ".jxl":
        try:
            from io import BytesIO
            Image.open(BytesIO(content)).verify()
        except Exception:
            raise HTTPException(
                status_code=400,
                detail="Invalid image file."
            )

    filename = f"{uuid4().hex}{extension}"
    filepath = UPLOAD_DIR / filename

    with open(filepath, "wb") as f:
        f.write(content)

    return str(filepath)