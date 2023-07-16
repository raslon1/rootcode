import asyncio
import json
import logging
from datetime import datetime
from databases import Database
from app.core.config import DATABASE_URL, SOCKET_HOST, SOCKET_PORT

database = Database(DATABASE_URL)

class SocketServer():
    async def handle(self, reader, writer):
        data = await reader.read(100)
        message = json.loads(data.decode())
        logging.info(message)
        message['d'] = datetime.strptime(message['d'], '%Y-%m-%d %H:%M:%S.%f')
        await database.connect()
        query = "INSERT INTO t(x, y, d) VALUES (:x, :y, :d)"

        await database.execute(query=query, values=message)
        await database.disconnect()
        writer.close()

    async def run_socket_server(self):
        server = await asyncio.start_server(self.handle, SOCKET_HOST, SOCKET_PORT)
        async with server:
            logging.info("SERVER RUN")
            await server.serve_forever()
        logging.info("SERVER CLOSE")

    async def task_socket_server(self):
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        task = loop.create_task(self.run_socket_server())
        if not loop.is_running():
            loop.run_until_complete(task)
