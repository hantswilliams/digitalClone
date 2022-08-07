from pydantic import BaseModel, Field
from typing import Optional

class VideoModel(BaseModel):
    audioFileLocation: str
    imageFileLocation: str
