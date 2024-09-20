import asyncio
import websockets
from websockets.exceptions import ConnectionClosedError

sexyart = """
$$$$$$$$\             $$\                 $$\                            
$$  _____|            $$ |                $$ |                           
$$ |   $$$$$$\   $$$$$$$ | $$$$$$\   $$$$$$$ | $$$$$$$\                  
$$$$$\ \____$$\ $$  __$$ |$$  __$$\ $$  __$$ |$$  _____|                 
$$  __|$$$$$$$ |$$ /  $$ |$$$$$$$$ |$$ /  $$ |\$$$$$$\                   
$$ |  $$  __$$ |$$ |  $$ |$$   ____|$$ |  $$ | \____$$\                  
$$ |  \$$$$$$$ |\$$$$$$$ |\$$$$$$$\ \$$$$$$$ |$$$$$$$  |                 
\__|   \_______| \_______| \_______| \_______|\_______/                                                 
                                                                         
$$\      $$\           $$\       $$\                           $$\       
$$ | $\  $$ |          $$ |      $$ |                          $$ |      
$$ |$$$\ $$ | $$$$$$\  $$$$$$$\  $$$$$$$\   $$$$$$\   $$$$$$\  $$ |  $$\ 
$$ $$ $$\$$ |$$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$  __$$\ $$ | $$  |
$$$$  _$$$$ |$$$$$$$$ |$$ |  $$ |$$ |  $$ |$$ /  $$ |$$ /  $$ |$$$$$$  / 
$$$  / \$$$ |$$   ____|$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$  _$$<  
$$  /   \$$ |\$$$$$$$\ $$$$$$$  |$$ |  $$ |\$$$$$$  |\$$$$$$  |$$ | \$$\ 
\__/     \__| \_______|\_______/ \__|  \__| \______/  \______/ \__|  \__|
"""

print(sexyart)
print("\n\nCreating websocket, please wait!")
asyncio.sleep(2.5)

connected_clients = set()

async def handle_client(websocket, path):
    print(f"A client connected: {websocket.remote_address}")
    connected_clients.add(websocket)

    try:
        async for message in websocket:
            print(f"Message received: {message}")
            for client in connected_clients:
                if client != websocket:
                    await client.send(message)
    except ConnectionClosedError:
        print(f"Client disconnected: {websocket.remote_address}")
    finally:
        connected_clients.remove(websocket)

async def main():
    print(sexyart + "\n\n")
    print("Faded's Websocket - Running")

    async with websockets.serve(handle_client, "0.0.0.0", 6969):
        await asyncio.Future()  

asyncio.run(main())
