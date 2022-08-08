from fastapi import APIRouter, File, UploadFile
from typing import Optional, Union
from fastapi import Query
import uuid
import os
from io import BytesIO

from src.components.video.create_video import audio2head
from src.models.video import VideoModel


# from src.components.transform_audio import audio_converter_function

#APIRouter creates path operations for item module
router = APIRouter(
    prefix="/video",
    tags=["Video"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
def read_root():
    return ["Video Clone Management"]

@router.post("/add")
async def create_upload_file(postItems: VideoModel):
    """
    the name of the first key:value is `file`, and is followed by the image 
    """

    # print current working directory
    machineCwd = os.getcwd()

    responseAudioFile = postItems.audioFileLocation 
    responseImageFile = postItems.imageFileLocation

    model_path = machineCwd + '/src/components/video/checkpoints/audio2head.pth.tar'
    save_path = machineCwd + '/src/components/video/results'

    responseAudioFile = machineCwd + '/files/transformed/audio/moded/' + responseAudioFile
    responseImageFile = machineCwd + '/files/transformed/image/moded/' + responseImageFile

    audio2head(responseAudioFile, responseImageFile, model_path, save_path)

    return {
        "modelInputs": {
            "audio": responseAudioFile,
            "image": responseImageFile,
        }
    }
