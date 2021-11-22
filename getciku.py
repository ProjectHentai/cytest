import asyncio

import aiohttp
import aiofiles

headers = {"Referer": "http://114.67.246.176:17565/",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.41",
           "X-Requested-With": "XMLHttpRequest"}


async def fetch(session, file, msg):
    async with session.post("http://114.67.246.176:17565/index/chat", data={"msg": msg},
                            headers=headers) as resp:
        data = await resp.json()
        msg = data["msg"]
        print(msg)
        await file.write(msg + "\n")
        return msg


async def main():
    file = await aiofiles.open("ciku.txt", "a+", encoding="utf-8")
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, file, "老婆") for i in range(10000)]
        await asyncio.gather(*tasks)
    await file.close()


asyncio.run(main())
