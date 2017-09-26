#coding=utf-8
from flask import Flask,flash,request,render_template,jsonify,session,redirect,url_for,send_from_directory
import json,urllib2,urllib
import os
import commands
import logging
from urlparse import unquote
import types
import time
import threading
import Queue
import ConfigParser

def init():
    #Define profile
    global config
    config = ConfigParser.SafeConfigParser()
    config.read('alarm_config.py')
    global queuesize
    queuesize = int(config.get('queue','queuesize'))
    global PutTackTime
    PutTackTime = float(config.get('put','PutTackTime'))
    global locktime
    locktime = int(config.get('filterconfig','locktime'))
    global dingtalkroboturl
    dingtalkroboturl = config.get('put','dingtalkroboturl')
    global project_name
    project_name = config.get('project','project_name')
    global DiscardAlarmThreshold
    DiscardAlarmThreshold = int(config.get('filterconfig','DiscardAlarmThreshold'))
    global MessagesQueue
    MessagesQueue = Queue.Queue(queuesize)
    global keywordlist
    keywordlist = eval(config.get('filterconfig','filterkeywordlist'))
    global keylocktimelist
    keylocktimelist = {}
    global NumOfDropList
    NumOfDropList = {}
    global DiscardAlarmThresholdlist
    DiscardAlarmThresholdlist = {}
init()

def putlog():
    while 1:
        message=MessagesQueue.get()
        MessagesQueue.task_done()
        os.system("curl '"+dingtalkroboturl+"' -H 'Content-Type: application/json' -k -d '{\"msgtype\": \"markdown\",\"markdown\": {\"title\":\""+message+"\"}}'")
        time.sleep(PutTackTime)

def messagefilter(message,keywordlist):
    for keyword in keywordlist:
        if keyword in message:
            if not keylocktimelist.has_key(keyword):
                keylocktimelist[keyword] = 0
            if not NumOfDropList.has_key(keyword):
                NumOfDropList[keyword] = 0
            if not DiscardAlarmThresholdlist.has_key(keyword):
                DiscardAlarmThresholdlist[keyword] = DiscardAlarmThreshold
            if time.time() > keylocktimelist[keyword]:
                keylocktimelist[keyword]=time.time() + locktime
                MessagesQueue.put(message)
                return True
            else:
                NumOfDropList[keyword] = NumOfDropList[keyword] + 1
                if NumOfDropList[keyword] == DiscardAlarmThresholdlist[keyword]:
                    DiscardAlarmThresholdlist[keyword] = DiscardAlarmThresholdlist[keyword] + DiscardAlarmThreshold
                    MessagesQueue.put(""" WARNING","text": "# **WARNING**\\nThere are already **"""+str(NumOfDropList[keyword])+""" """+keyword+"""** messages thrown away"""+('!'*200))
                return keyword
    MessagesQueue.put(message)
    return True

app = Flask(__name__)
@app.route('/',methods=["POST"])
def rdirect():

    #Gets the value of each parameter of the API
    message=request.form.get('message','None').encode("utf-8").replace('"','\\"')
#    handle=request.form.get('handle','None').encode("utf-8")
#    status=request.form.get('status','None').encode("utf-8")
#    event_time=request.form.get('event_time','None').encode("utf-8")
#    if event_time.isdigit() == True and len(event_time)  == 13:
#        event_time=time.ctime(float(event_time)/1000)
#    else:
#        event_time="Time format error1"
#    event_id=request.form.get('event_id','None').encode("utf-8")

    alarm_object=request.form.get('alarm_object','None').encode("utf-8")
#    type_desc=request.form.get('type_desc','None').encode("utf-8")
    alarm_type=request.form.get('alarm_type','None').encode("utf-8")
    if alarm_type.find("@@"):
        alarm_type = alarm_type.split('@')[0]
    alarm_level=request.form.get('alarm_level','None').encode("utf-8")
#    event_id=status=event_time=type_desc=""
#    print(message)

    sendmsg=alarm_type+"\",\"text\": \"# **"+alarm_type+"**\\n## ***project***： "+project_name
    if alarm_level != 'None':
        sendmsg = sendmsg + "\\n## ***alarm_level***： "+alarm_level 
    if alarm_object != 'None':
        sendmsg = sendmsg + "\\n## ***alarm_object***： "+alarm_object
    sendmsg = sendmsg + "\\n## ***message***： "+message
    if MessagesQueue.full():
        MessagesQueue.queue.clear()
        MessagesQueue.put(""" WARNING","text": "# **WARNING**\\nMessage queue overflow, message has been dropped"""+('!'*200))
    Ret = messagefilter(sendmsg,keywordlist)
    if Ret == True:
        return redirect("OK")
    else:
        return redirect("""WARNING:Message is filtered by the keyword '"""+Ret+"""'!""")

if __name__ == '__main__':
    putt = threading.Thread(target=putlog)
    putt.setDaemon(True)
    putt.start()
    app.run(host='0.0.0.0', port=1234,debug=True,threaded=True)

