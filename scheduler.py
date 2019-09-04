from apscheduler.schedulers.blocking import BlockingScheduler
import news
import os

sched = BlockingScheduler()


@sched.scheduled_job('interval', mintues=120)
def timed_job():
    os.system('python news.py')


sched.start()
