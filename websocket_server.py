# Importing the relevant libraries
import websockets
import asyncio
import json


# Server data
PORT = 11183
print("Server listening on Port " + str(PORT))

# A set of connected ws clients
connected = set()

# The main behavior function for this server
async def server(websocket, path):
    print("A client just connected")
    print(websocket)
    print(type(websocket))
    # Store a copy of the connected client
    connected.add(websocket)
    print(connected)
    # Handle incoming messages
    try:
        async for message in websocket:
            print("Received messagom client: " + message)
            if (message == str("enable")):
                await sendcmd(websocket, "enabling")




    # Handle disconnecting clients 
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")
    finally:
        connected.remove(websocket)

async def sendcmd(websocket, message):
    await websocket.send(message)
    return "OK"

# Start the server
start_server = websockets.serve(server, "localhost", PORT)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()