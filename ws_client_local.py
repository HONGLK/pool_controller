# Importing the relevant libraries
import websockets
import asyncio
import json

# The main function that will handle connection and communication 
# with the server
async def listen():
    url = "ws://127.0.0.1:11183"
    # Connect to the server
    async with websockets.connect(url) as ws:
        # Send a greeting message
        payload = {"username": "local"}
        await ws.send(payload)
        # Stay alive forever, listening to incoming msgs
        while True:
            await ws.recv()
def trig(msg):
    print(msg)
# Start the connection
asyncio.get_event_loop().run_until_complete(listen())