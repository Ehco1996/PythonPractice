import asyncio

import aiohttp


async def fetch(session, url):
    async with session.get(url) as resp:
        return await resp.text()


async def main():
    async with aiohttp.ClientSession() as s:
        html = await fetch(s, 'http://g.cn')
        print(html)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
