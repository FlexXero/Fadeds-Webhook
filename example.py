import asyncio
import websockets

uri = "ws://0.0.0.0:6969"

try:
    async def main():
        async with websockets.connect(uri) as ws:
            print("Connected!")
            await ws.send("Hello, webhook!")
            print(f"Received: {await ws.recv()}")

    asyncio.run(main())
except websockets.ConnectionClosedError as e:
    print(f"Connection closed: {e}")
