from fastapi import APIRouter
from src.endpoints import product, user, image, audio, video

router = APIRouter()
router.include_router(product.router)
router.include_router(user.router)
router.include_router(image.router)
router.include_router(audio.router)
router.include_router(video.router)