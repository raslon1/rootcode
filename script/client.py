import asyncio
import json
import logging
from datetime import datetime
import random


async def tcp_echo_client(message):
    logging.info("CLIENT RUN")
    reader, writer = await asyncio.open_connection(
        '0.0.0.0', 8888)
    writer.write(message.encode())
    writer.close()


async def run_socket_client() -> None:
    while True:
        try:
            await asyncio.sleep(10)
            diagram_data_dict = {
                "x": random.randint(1, 20),
                "y": random.randint(1, 20),
                "d": str(datetime.now())
            }
            logging.info(diagram_data_dict)
            diagram_data_dump = json.dumps(diagram_data_dict)
            await tcp_echo_client(diagram_data_dump)
        except Exception as e:
            logging.warning("Server not found")

if __name__ == "__main__":
    asyncio.run(run_socket_client())