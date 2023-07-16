import base64
import io

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from fastapi import HTTPException, status


class DiagramService:
    async def draw(self, data):
        if not data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Нет данных",
            )

        df = pd.DataFrame(data)
        df.plot(x="trunc_1_minute", y=["x", "y"], kind="bar")
        plt.title("Статистика")
        plt.xlabel("Время")
        plt.rcParams["figure.figsize"] = [15, 15]
        plt.rcParams["figure.autolayout"] = True
        plt.gcf().autofmt_xdate()
        L = plt.legend()
        # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%d/%Y %H:%M'))
        plt.gca().xaxis.set_major_locator(mdates.DayLocator())
        L.get_texts()[0].set_text('План')
        L.get_texts()[1].set_text('Факт')
        filtered_image = io.BytesIO()
        plt.savefig(filtered_image, dpi=50, format="png")
        filtered_image.seek(0)
        plt.close()
        # encoded_image = base64.b64encode(filtered_image.getvalue())
        # img = "data:image/png;base64, " + encoded_image.decode("utf8")
        # filtered_image.close()
        return filtered_image
