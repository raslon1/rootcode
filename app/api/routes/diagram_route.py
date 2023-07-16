from fastapi import APIRouter, Depends
from starlette.responses import StreamingResponse

from app.db.repositories.diagram import DiagramRepository
from app.api.dependencies.database import get_repository
from app.diagram_service.diagrams.stat_diagram import DiagramService

router = APIRouter()


@router.get("/")
async def draw_diagram(
        diagram_repo: DiagramRepository = Depends(get_repository(DiagramRepository)),
        diagram_service: DiagramService = Depends(DiagramService)
):
    data = await diagram_repo.get_diagram_data()
    diagram = await diagram_service.draw(data)
    return StreamingResponse(diagram, media_type="image/png")
