import asyncio
import json
import websockets

async def stream_telemetry(websocket):
    print("Dashboard UI client connected.")
    try:
        while True:
            payload = {
                "system_status": "ONLINE",
                "current_floor": 1,
                "state": "IDLE",
                "last_call_status": "VERIFIED",
                "verification_latency_ms": 1150.0
            }
            await websocket.send(json.dumps(payload))
            await asyncio.sleep(2)
    except websockets.exceptions.ConnectionClosed:
        print("Dashboard UI client disconnected.")

async def main():
    print("Starting WebSocket Server on ws://localhost:8765...")
    async with websockets.serve(stream_telemetry, "localhost", 8765):
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())