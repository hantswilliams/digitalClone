from fastapi import APIRouter
from src.endpoints import product, user, image, audio_transform

router = APIRouter()
router.include_router(product.router)
router.include_router(user.router)
router.include_router(image.router)
router.include_router(audio_transform.router)