"""
作者:萌新源
时间:2022/3/30
操作系统:debian for raspberry pi
修改请保留本插件的版权
本插件版权属于萌新源
要发布请注明出处

"""
from nonebot import on_keyword
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import GroupMessageEvent,Bot,Message,MessageSegment,Event
import requests
import json

xingzuo = on_keyword({'#星座'})

@xingzuo.handle()
async def xz(bot: Bot, event: Event, state: T_State):
    anses = str(event.get_message()).strip()
    ansek = anses.strip('#星座')
    url = f'http://hm.suol.cc/API/xzys.php?msg={ansek}'
    x = requests.get(url)
    ansx = x.text
    b = '{br}'
    n = '\n'
# print(hua)
    if b in ansx:
        ansu = ansx.replace(b,n)
        await xingzuo.finish(Message(f'{ansu}'))
    else:
        await xingzuo.finish(Message(f'{ansx}'))
    
    

