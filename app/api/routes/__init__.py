from fastapi import APIRouter
from app.api.routes.diagram_route import router as draw_diagram_router


router = APIRouter()

router.include_router(draw_diagram_router, prefix="/draw_diagram", tags=["draw_diagram"])
