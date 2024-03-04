import asyncio
import hashlib
import random
from datetime import datetime

async def task_process_request(event: asyncio.Event):
    print("aguardando evento")
    await event.wait()
    print("evento concluido...")

async def sensor(event: asyncio.Event):
    sleep = random.randint(3, 8)
    await asyncio.sleep(sleep)

    print(f"finalizou a coleta : {name_event:}")
    event.set()

async def request_data(results: dict):
    while True:
        event = asyncio.Event()

        seed = dateTime.utcnow().isoformat().encode()
        name_event = hashlib.md5(seed).hexdigest()

        results[name_event] = event

        asyncio.create_task(task_process_request(event))
        asyncio.create_task(sensor(event))
        await asyncio.sleep(5)

async def main():
    results = dict()
    queue = asyncio.Queue()

    asyncio.create_task(request_data(results,queue))
    asyncio.create_task(process_response(results,queue))
    await asyncio.Event.wait()

if __name__ == "_main_":
    asyncio.run(main())