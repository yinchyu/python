import requests
import pickle
import asyncio
import aiohttp


async def requ():
    print("get  https://cn.bing.com/")
    resp = await aiohttp.request('GET', 'https://cn.bing.com/')
    print(" 请求到了数据")

    # await asyncio.sleep(0.001)
    # async with aiohttp.ClientSession() as session:
    #     async with session.get('https://cn.bing.com/') as resp:
    #         # print(resp.status)
    #         print(await resp.status)
    # rep=requests.get("https://cn.bing.com/")
    # print(rep.status_code)
    # a=pickle.dumps(rep.text)
    # print(type(a))
    # with open("html",'wb') as f:
        # pickle.dump(rep,f)

def prase():
    a=open("html",'rb')
    d=pickle.load(a)
    # print(d.text)

async def main():
    tasks=[asyncio.create_task(requ()) for i in range(10)]
    await asyncio.gather(*tasks)
   # asyncio.run(asyncio.wait(tasks))


if __name__ == '__main__':
    # prase()
    # requ()
    asyncio.run(main())
