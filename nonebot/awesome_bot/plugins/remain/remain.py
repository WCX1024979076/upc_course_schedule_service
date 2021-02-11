import pymysql
import time
import datetime
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
        print(line)
        db.commit() 
        cursor.close()
        return line
    except pymysql.Error as e:
        print(e.args[0], e.args[1])
        # print(e[0])
        # traceback.print_exc()
        # 如果发生错误则回滚
        return False
