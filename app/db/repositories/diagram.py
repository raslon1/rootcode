from fastapi import HTTPException
from fastapi import status

from app.db.repositories.base import BaseRepository

ALL_DATA = f"""
    SELECT
        date_trunc('minute', d) - (CAST(EXTRACT(MINUTE FROM d) AS integer) % 1) * interval '1 minute' AS trunc_1_minute,
        sum(x) as x,
        sum(y) as y
    FROM t
    GROUP BY trunc_1_minute
    ORDER BY trunc_1_minute;
"""


class DiagramRepository(BaseRepository):
    async def get_diagram_data(self):
        try:
            all_diagram_data = await self.db.fetch_all(query=ALL_DATA)
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Ошиибка",
            )
        return [
            {
                "x": diagram_data.x,
                "y": diagram_data.y,
                "trunc_1_minute": diagram_data.trunc_1_minute} for diagram_data in all_diagram_data
        ]