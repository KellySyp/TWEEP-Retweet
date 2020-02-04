import datetime

date = datetime.datetime.now()

def writeLog(msg):
	f = open("log.txt", "a")
	f.write(date.strftime("%Y-%m-%d %H:%M:%S")+" Message: "+msg+"\n")
	f.close()