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

    model_path = './checkpoints/audio2head.pth.tar'
    save_path = './results/'

    audio2head(postItems.audioFileLocation, postItems.imageFileLocation, model_path, save_path)

    return {
        "modelInputs": {
            "audio": postItems.audioFileLocation,
            "image": postItems.imageFileLocation,
        }
    }
