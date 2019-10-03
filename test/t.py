import sys
import asyncio

sys.path.append('../')

from bot import Bot  # noqa: E420


async def run():
    async with Bot('') as b:
        user = await b.get_me()

        print(user)

asyncio.get_event_loop().run_until_complete(run())
