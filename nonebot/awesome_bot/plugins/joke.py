# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/14 23:13
# Description:

from nonebot import on_command
from nonebot.matcher import Matcher
from nonebot.permission import SUPERUSER
from nonebot.rule import to_me
from nonebot.typing import T_State
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Bot, unescape, MessageEvent, Message, MessageSegment
from nonebot.log import logger
import requests
from urllib import request, parse
import time,random,json
def get_joke():
    url = "http://v.juhe.cn/joke/randJoke.php"
    data = {'key':'434d940280f6c01ede40217da78bcfa2'}
    data = parse.urlencode(data)
    data = bytes(data, encoding='utf-8')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36',
    }
    req = request.Request(url, data=data, headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    json_data = json.loads(html)
    result=json_data['result']
    return result[random.randint(0,len(result)-1)]['content']


joke = on_command('joke', aliases=set(['笑话','讲个笑话']), rule=to_me(), priority=1)


@joke.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    await joke.send(Message(get_joke()))
