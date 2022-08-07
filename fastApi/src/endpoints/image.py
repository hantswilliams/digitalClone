from fastapi import APIRouter, File, UploadFile
from typing import Optional, Union
from fastapi import Query
import uuid
import os
from io import BytesIO

from src.components.transform_image import img_resizer_function

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/images",
    tags=["Image"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_root():
    return ["Image Management"]

@router.post("/add")
async def create_upload_file(file: UploadFile = File(...)):
    """
    the name of the first key:value is `file`, and is followed by the image 
    """

    extension = file.filename.split(".")[-1] in ("jpg", "jpeg")

    if not extension:
        return "Image must be jpg/jpeg format!"

    randomUID = str(uuid.uuid4())
    originalFileName = randomUID + "#original#" + file.filename 
    updatedFileName = randomUID + "#moded#" + file.filename 

    # file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    #get original object size from contents
    imgSize_original = len(contents)

    #resize image
    originalImage, resizeImage = img_resizer_function(contents)
    print('Image resized successfully!')

    #save image locally 
    originalImage.save(f"files/transformed/image/original/{originalFileName}")
    resizeImage.save(f"files/transformed/image/moded/{updatedFileName}")

    return {
        "fileName_uploaded": file.filename,
        "fileName_original": originalFileName, 
        "fileName_moded": updatedFileName,
    }
