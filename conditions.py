import asyncio

async def worker(condition: asyncio.Condition, i):
    async with condition:
        print(f"worker {i} esperando o condition")
        await condition.wait()
        print(f"worker {i} executado")

async def controller(condition: asyncio.Condition):
    print("controller iniciando")
    await asyncio.sleep(2)
    async with condition:
        print("Controller notificando workers")
        condition.notify_all()

async def main():
    condition = asyncio.Condition()
    workers = [worker(condition, i) for i in range(3)]
    controller_task = controller(condition)

    asyncio.gather(*workers, controller_task)

if __name__ == "_main_":
    asyncio.run(main())