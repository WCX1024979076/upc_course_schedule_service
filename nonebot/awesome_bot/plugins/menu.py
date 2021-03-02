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

menu = on_command('menu', aliases=set(['菜单']), rule=to_me(), priority=1)


@menu.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    msg = """****Bot菜单****
菜单：功能介绍
今日人品：看看今天人品如何？
bullshit/狗屁不通生成器+主题：狗屁不通！
zhihu/知乎：知乎日报
ai：价值一个亿的AI核心代码
hhsh: 能不能好好说话？
remain: 提醒
movie: 盗版视频/视频解析
joke: 笑话/讲个笑话
net_ease_music：网易云神评/网易神评
开源地址：https://github.com/WCX1024979076/upc_course_schedule_service
"""
    at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await menu.send(Message(at_ + msg))
