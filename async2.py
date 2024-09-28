import asyncio
from datetime import datetime

async def keep_printing(name):
    while True:
        print(f"{name} {datetime.now()}")
        await asyncio.sleep(0.5)

async def async_main():
    await asyncio.gather(keep_printing("first"),
    keep_printing("second"),
    keep_printing("third")
    )


asyncio.run(async_main())