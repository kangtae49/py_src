import os
import time

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()

def myfunc():
	print 'myfunc'

#scheduler.add_job(myfunc, trigger='cron', minute='*/5')
#scheduler.add_job(myfunc, 'interval', seconds=5)
scheduler.add_job(myfunc, trigger='cron', second='5')
scheduler.start()
	
try:
	while True:
		time.sleep(2)
except (KeyboardInterrupt, SystemExit):
	scheduler.shutdown()  
