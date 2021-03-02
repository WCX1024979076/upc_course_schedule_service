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
phrase = on_command('phrase', aliases=set(['成语接龙']), rule=to_me())


@phrase.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    try :
        args = str(event.get_message().split(" ")[1]).strip()
    except Exception as e: 
        args = str(event.get_message()).strip()
    if args:
        state["phrase"] = args

def get_phrase(phrase_text) :
    url = 'http://i.itpk.cn/api.php?question=@cy'+phrase_text
    print(url)
    data = requests.get(url).text
    return data


@phrase.got("phrase", prompt="请输入成语")
async def handle_event(bot: Bot, event: Event, state: T_State):
    try :
        await phrase.send(Message("答案："+get_phrase(state["phrase"])))
    except Exception as e: 
        print(e)
        await phrase.send(Message("解析失败"))