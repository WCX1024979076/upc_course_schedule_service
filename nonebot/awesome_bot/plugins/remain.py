# Author: BeiYu
# Github: https://github.com/beiyuouo
# Date  : 2021/1/14 20:56
# Description:
import datetime

import pymysql
import time
import datetime
import pytz
import datetime
import aiohttp
import asyncio
import nonebot
from nonebot.adapters import Bot, Event
from nonebot.adapters.cqhttp import Message
from nonebot.log import logger
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from awesome_bot.config.config import *
from nonebot import require

async def insert(user,start,thing,location,note,end,before_start) :
    timeArray = time.strptime(start, "%Y-%m-%d %H:%M:%S")
    timeStamp = int(time.mktime(timeArray))-before_start*60
    timeArray = time.localtime(timeStamp)
    remaind = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
    print(start)
    db = pymysql.connect(host="localhost",port=3306,user="root", password="upc1953root?", database="my")
    if end!='无' :
        sql = "INSERT INTO thing(user,remaind,start,thing,location, notes, end) VALUES ('"+user+"','"+remaind+"','"+start+"','"+thing+"','"+location+"','"+note+"','"+end+"')"
    else :
        sql = "INSERT INTO thing(user,remaind,start,thing,location, notes, end) VALUES ('"+user+"','"+remaind+"','"+start+"','"+thing+"','"+location+"','"+note+"',NULL)"
    try :
        print(sql)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit() 
        cursor.close()
        return True
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # print(e[0])
        # traceback.print_exc()
        # 如果发生错误则回滚
        return False

async def search(remaind) :
    db = pymysql.connect(host="localhost",port=3306,user="root", password="upc1953root?", database="my")
    sql = "SELECT user,remaind,start,thing,location,notes,end FROM thing WHERE remaind='"+remaind+"'"
    try :
        cursor = db.cursor()
        cursor.execute(sql)
        line = cursor.fetchall()
        db.commit() 
        cursor.close()
        return line
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # print(e[0])
        # traceback.print_exc()
        # 如果发生错误则回滚
        return False




scheduler1 = require("nonebot_plugin_apscheduler").scheduler


def getBot() -> Bot:
    print(nonebot.get_bots())
    print(nonebot.get_bots().values())
    print(list(nonebot.get_bots().values()))
    print(len(list(nonebot.get_bots().values())))

    return list(nonebot.get_bots().values())[0]


@scheduler1.scheduled_job('cron', hour='*', minute='*')
async def _():
    tz = pytz.timezone('Asia/Shanghai')
    nowtime = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M")
    ans_array=await search(nowtime)
    bot = list(nonebot.get_bots().values())[0]
    for i in ans_array :
        msg="定时提醒\nqq号："+i[0]+"\n开始时间："+i[2].strftime("%Y-%m-%d %H:%M:%S")+"\n结束时间："+i[6].strftime("%Y-%m-%d %H:%M:%S")+"\n事件："+i[3]+"\n地点："+i[4]+"\n备注："+i[5]
        await bot.send_private_msg(user_id=i[0], message=Message(msg))

