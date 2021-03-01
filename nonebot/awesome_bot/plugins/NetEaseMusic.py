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
import requests        #导入requests包import urllib
import urllib
from urllib import request, parse
import time,random,json
def NetEaseMusic():
    url = "http://api.tianapi.com/txapi/hotreview/index"
    data = {'key':'fd6a3820d162acbeadd8fe6684543d6e'}
    data = parse.urlencode(data)
    data = bytes(data, encoding='utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    }
    req = request.Request(url, data=data, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    json_data = json.loads(html)
    result=json_data['newslist'][0]['content']
    return result

net_ease_music = on_command('net_ease_music', aliases=set(['网易云神评', '网易神评']), rule=to_me())


@net_ease_music.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    try :
        await net_ease_music.send(Message(NetEaseMusic()))
    except Exception as e: 
        print(e)
        await net_ease_music.send(Message("获取失败"))