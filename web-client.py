import asyncio
import websockets
import time

async def hello(uri):
    async with websockets.connect(uri) as websocket:
        await websocket.send("hello world")
        print("< HELLO WORLD")
        while True:
            recv_text = await websocket.recv()
            if recv_text:
                print("> {}".format(recv_text))
                time.sleep(1)
                await websocket.send("hello world")

asyncio.get_event_loop().run_until_complete(hello('ws://localhost:8765'))