#alarm_config.py
#Project configuration
[project]
project_name = '九歌四'

#Message push configuration
[put]
dingtalkroboturl = 'https://oapi.dingtalk.com/robot/send?access_token=c058ed7b576a12d676e849e4eed5ad20d889057b68ed805b495c216d1198974a'




#-----WARNING：Don't change following content-----

#Eack time interval (unit seconds)
PutTackTime = 3.2

#Message queue configuration
[queue]
#The number of messages that can't be sent can be saved at most, if the queue is full, it will be empty
queuesize = 95

#Message filtering configuration
[filterconfig]
#包含列表中各字符串的消息每locktime时间内只会被发送一次，locktime时间内重复出现包含该字符串的消息会被丢弃，列表中各字符串之间互不影响。locktime单位为秒
#例如locktime=300，300秒时间内A、B两条消息都包含列表中的"TCPretr"字符串，那么可能有一条会被丢弃（消息越多丢弃越多,丢弃消息每满DiscardAlarmThreshold条会发送一条告警）。这时包含列表中字符串"aaaaaaaaaaaaa"的C消息也在这300秒内要发送，但只有一条，它不会被丢弃。
filterkeywordlist = ["TCPretr","aaaaaaaaaaaaa","bbbbbbbbbbbbbbbbb"]
locktime = 300
DiscardAlarmThreshold = 50
