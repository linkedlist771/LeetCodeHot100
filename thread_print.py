import asyncio


async def print_i(i: int):
    while True:
        print(i)
        await asyncio.sleep(1)


async def main():
    task1 = asyncio.create_task(print_i(1))
    task2 = asyncio.create_task(print_i(2))
    task3 = asyncio.create_task(print_i(3))
    await asyncio.gather(task2, task1, task3)


if __name__ == "__main__":
    asyncio.run(main())
