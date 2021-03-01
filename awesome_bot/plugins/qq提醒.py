# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/14 20:56
# Description:
import datetime

import nonebot
from nonebot.adapters import Bot, Event
import pytz
import datetime
import aiohttp
import asyncio

from nonebot.adapters.cqhttp import Message
from nonebot.log import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from awesome_bot.config.config import *

from nonebot import require

scheduler = require("nonebot_plugin_apscheduler").scheduler


def getBot() -> Bot:
    print(nonebot.get_bots())
    print(nonebot.get_bots().values())
    print(list(nonebot.get_bots().values()))
    print(len(list(nonebot.get_bots().values())))

    return list(nonebot.get_bots().values())[0]


@scheduler.scheduled_job('cron', hour='*', minute='10')
async def _():
    tz = pytz.timezone('Asia/Shanghai')
    nowtime = datetime.datetime.now(tz).strftime("%H:%M")
    print(list(nonebot.get_bots().values())[0])
    bot = list(nonebot.get_bots().values())[0]
    msg = f"现在时间是: {nowtime}" + "\n" + "你好"
    await bot.send_private_msg(user_id=1024979076, message=Message(msg))

