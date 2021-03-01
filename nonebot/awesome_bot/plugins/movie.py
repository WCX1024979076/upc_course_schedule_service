from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Bot, unescape, MessageEvent, Message, MessageSegment
from nonebot.log import logger
import pymysql
import time
import datetime
import json
import requests        #导入requests包
add_remaind = on_command('add_remaind', aliases=set(['盗版视频', '视频解析']), rule=to_me())


@add_remaind.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["url"] = args

def get_url(movie_url) :
    url = 'https://www.eggvod.cn/jxcode.php?in=81516699&code=2'
    data = requests.get(url).text    
    return 'https://www.eggvod.cn/jxjx.php?lrspm='+data+'&zhm_jx='+movie_url


@add_remaind.got("url", prompt="请输入视频链接！例如：视频解析 www.baidu.com")
async def handle_event(bot: Bot, event: Event, state: T_State):
    try :
        url = state["url"].split(" ")[1]
        await add_remaind.send(Message("解析成功："+get_url(url)))
    except Exception as e: 
        print(e)
        await add_remaind.send(Message("解析失败"))