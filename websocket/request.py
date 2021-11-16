# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests
import json
import websockets
import asyncio
import websocket
import re
def getjsondata():
    roomid=5050
    #url=r"https://api.live.bilibili.com/room/v1/Room/room_init?id={}".format(roomid)
    url="https://live.bilibili.com/5050?spm_id_from=333.851.b_62696c695f7265706f72745f6c697665.16"
    print(url)
    headers={"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36 Edg/91.0.864.59"}
    getdata=requests.get(url,headers=headers)
    # jsondagta=json.loads(getdata.text.encode("utf-8"))
    data=getdata.text
    print(data)
    datalist=re.findall("< div class='chat-items'.*?</div>",data)
    print(getdata.status_code)
    #　获取到对应的房间号
    # print(jsondagta["data"]["room_id"])
    #chat-items
    print(datalist)



async def connectweb():
    url=r"ws://broadcastlv.chat.bilibili.com:2244/sub"
    authjson = {
        "uid": 0,
        "roomid": 5050,
        "protover": 1,
        "platform": "web",
        "clientver": "1.4.0"
    }
    async with websockets.connect(url) as server:
        await  server.send(json.dumps(authjson))
        # recvmessage=server.recv()
        print("message")
        # print(recvmessage)



def print_hi():
    ws = websocket.WebSocket()
    ws.connect("ws://broadcastlv.chat.bilibili.com:2244/sub")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    getjsondata()
    # asyncio.get_event_loop().run_until_complete(connectweb())
    # print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
