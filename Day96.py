import time
import asyncio
import requests


async def function1():
    print("func 1")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("Day96.ico", "wb").write(response.content)

    return "Ishaan"


async def main():
    await function1()

    # return 3
    L = await asyncio.gather(function1())
    print(L)
    task = asyncio.create_task(function1())
    await function1()


asyncio.run(main())
