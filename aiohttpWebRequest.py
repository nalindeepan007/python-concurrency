import asyncio
import aiohttp
from aiohttp import ClientSession
from util.timingCoroutineDecorator import async_timed

@async_timed()
async def fetchStatus(session: ClientSession, url: str) -> int:
    async with session.get(url) as result:
        return result.status

@async_timed()
async def main():
    async with aiohttp.ClientSession() as session:
        url = "https://nalindeepan007.github.io/CVissfolio/"
        status = await fetchStatus(session, url)
        print(f'Status for {url} was {status}')

asyncio.run(main())