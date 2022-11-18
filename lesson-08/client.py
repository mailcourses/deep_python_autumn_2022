import asyncio
import aiohttp


async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            text = await resp.text()
            print("text", len(text), text[:200])

            return len(text)


if __name__ == "__main__":
    URL = "https://docs.python.org/3/library/unittest.html"

    asyncio.run(fetch_url(URL))
