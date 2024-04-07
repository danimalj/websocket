import asyncio
import websockets

file_path = 'responses.txt'  # File to store the responses

async def post_to_websocket(uri, message, count):
    async with websockets.connect(uri) as websocket:
        with open(file_path, 'a') as file:
            for _ in range(count):
                await websocket.send(message + str(_))
                response = await websocket.recv()
                file.write(response + '\n')
                print(f"Received response: {response}")

# Example usage
uri = "ws://localhost:8765"  # Replace with the actual WebSocket URI
message = "Hello, WebSocket!"  # Replace with the actual message to send
count = 1000  # Number of times to post to the WebSocket

# Run the asynchronous function
asyncio.run(post_to_websocket(uri, message, count))
