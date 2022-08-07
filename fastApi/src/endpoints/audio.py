from fastapi import APIRouter, File, UploadFile
from typing import Optional, Union
from fastapi import Query
import uuid
import os
from io import BytesIO

from src.components.audio.transform_audio import audio_converter_function

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/audio",
    tags=["Audio"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_root():
    return ["Audio Management"]

@router.post("/add")
async def create_upload_file(file: UploadFile = File(...)):
    """
    the name of the first key:value is `file`, and is followed by the image 
    """

    extensionType = file.filename.split(".")[-1]

    extension = file.filename.split(".")[-1] in ("m4a", "wav")
    print('Extension: ', extension)

    if not extension:
        return "Audio must be m4a or wav format!"

    randomUID = str(uuid.uuid4())
    originalFileName = randomUID + "#original#" + file.filename 

    # if exntesion is not wave, do conversion
    if extensionType != "wav":
        updatedFileNameSave = (randomUID + "#moded#" + file.filename).replace(".m4a", ".wav")
    else:
        updatedFileNameSave = originalFileName

    # file.filename = f"{uuid.uuid4()}.jpg"
    contents = await file.read()  # <-- Important!

    # save file to disk as m4a
    if extensionType != "wav":
        with open(f"files/transformed/audio/original/{originalFileName}", "wb") as f:
            f.write(contents)
    elif extensionType == "wav":
        with open(f"files/transformed/audio/moded/{originalFileName}", "wb") as f:
            f.write(contents)

    if extensionType != "wav":
        conversionResult = audio_converter_function(f"files/transformed/audio/original/{originalFileName}", f"files/transformed/audio/moded/{updatedFileNameSave}")
    else:
        conversionResult = 'uploaded .wav file no need for conversion'

    return {
        "extensionUploaded": extensionType,
        "fileName_uploaded": file.filename,
        "fileName_original": originalFileName, 
        "fileName_moded": updatedFileNameSave,
        "location_moded": f"files/transformed/audio/moded/{updatedFileNameSave}",
        "conversionResult": conversionResult
    }
