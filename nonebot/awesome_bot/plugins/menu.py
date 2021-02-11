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
ssr/v2ray：来条订阅链接
twqd/签到/体温签到+学号：体温签到
twqh/土味情话/爱我吗：爱你！
bullshit/狗屁不通生成器+主题：狗屁不通！
zhihu/知乎：知乎日报
帮我骂人+@小可爱：不要轻易骂小可爱嗷~
ai：价值一个亿的AI核心代码
hhsh: 能不能好好说话？
搜题：（开发中...）
疫情：（开发中...）
开源地址：https://github.com/beiyuouo/plugins-for-nonebot2
"""
    at_ = f"[CQ:at,qq={event.get_user_id()}]"
    await menu.send(Message(at_ + msg))
