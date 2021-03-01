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

file = open('/home/UPC-nCoV-submit/cqhttp/nonebot/awesome_bot/plugins/remain/config.json', 'r', encoding='utf-8-sig')
ans=json.load(file)
mysql_user=ans['mysql_user']
mysql_passwd=ans['mysql_passwd']
async def insert(user,start,thing,location,note,end,before_start) :
    timeArray = time.strptime(start, "%Y-%m-%d %H:%M")
    timeStamp = int(time.mktime(timeArray))-before_start*60
    timeArray = time.localtime(timeStamp)
    remaind = time.strftime("%Y-%m-%d %H:%M", timeArray)
    print(start)
    db = pymysql.connect(host="localhost",port=3306,user=mysql_user, password=mysql_passwd, database="my")
    if end!='无' :
        sql = "INSERT INTO thing(user,remaind,start,thing,location, notes, end) VALUES ('"+user+"','"+remaind+"','"+start+"','"+thing+"','"+location+"','"+note+"','"+end+"')"
    else :
        sql = "INSERT INTO thing(user,remaind,start,thing,location, notes, end) VALUES ('"+user+"','"+remaind+"','"+start+"','"+thing+"','"+location+"','"+note+"',NULL)"
    try :
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


add_remaind = on_command('add_remaind', aliases=set(['提醒', '增加提醒']), rule=to_me())


@add_remaind.handle()
async def handle(bot: Bot, event: Event, state: T_State):
    args = str(event.get_message()).strip()
    if args:
        state["thing"] = args


@add_remaind.got("thing", prompt="请按照格式输入开始时间（必填）、结束时间（必填）、地点、提醒名称（必填）、提前提醒时间（必填，单位：分钟）、备注，除必填选项外其余如果空缺，请填无，填写样例：\n提醒 2021-2-10 8:00 2021-2-10 9:00 学校 上交作业 20 无 \n代表于2021-2-10 8:00 开始，结束时间2021-2-10 9:00，地点为学校，事情为上交作业，提前20min提醒，无备注")
async def handle_event(bot: Bot, event: Event, state: T_State):
    try :
        thing = state["thing"]
        thing_array=thing.split(" ")
        if thing_array[0]!='提醒' :
            thing_array.insert(0,'提醒')
        user=event.get_user_id()
        msg = await insert(user,thing_array[1]+" "+thing_array[2],thing_array[6],thing_array[5],thing_array[8],thing_array[3]+" "+thing_array[4],int(thing_array[7]))
        if msg :
            await add_remaind.send(Message("增加成功"))
        else :
            await add_remaind.send(Message("增加失败"))
    except Exception as e: 
        print(e)
        await add_remaind.send(Message("发生错误，增加失败"))