# Filename: PortListner.py
# @author: RobinTang
# Created on 2012-9-5 1:42:05
 
import threading
import socket
import time
import pymysql
import time
import datetime
encoding = 'utf8'
BUFSIZE = 20480

def insert(user,start,thing,location,note,end,before_start) :
    timeArray = time.strptime(start, "%Y-%m-%d %H:%M")
    timeStamp = int(time.mktime(timeArray))-before_start*60
    timeArray = time.localtime(timeStamp)
    remaind = time.strftime("%Y-%m-%d %H:%M", timeArray)
    print(start)
    db = pymysql.connect(host="localhost",port=3306,user="root", password="upc1953root?", database="my")
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

def insert_data(data) :
    print(data+"1233")
    list=eval('(' + data + ')')
    for i in list :
        out=insert(i['user'],i['start'],i['thing'],i['location'],i['note'],i['end'],i['before'])

# a read thread, read data from remote
class Reader(threading.Thread):
    def __init__(self, client):
        threading.Thread.__init__(self)
        self.client = client
        
    def run(self):
        while True:
            data = self.client.recv(BUFSIZE)
            if(data):
                string = bytes.decode(data, encoding)
                print(string)
                msg=insert_data(string)
                print(type(string))
            else:
                break
        print("close:", self.client.getpeername())
        
    def readline(self):
        rec = self.inputs.readline()
        if rec:
            string = bytes.decode(rec, encoding)
            if len(string)>2:
                string = string[0:-2]
            else:
                string = ' '
        else:
            string = False
        return string
 
# a listen thread, listen remote connect
# when a remote machine request to connect, it will create a read thread to handle
class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", port))
        self.sock.listen(0)
    def run(self):
        print("listener started")
        while True:
            client, cltadd = self.sock.accept()
            Reader(client).start()
            cltadd = cltadd
            print("accept a connect")
 
lst  = Listener(5050)   # create a listen thread
lst.start() # then start
 