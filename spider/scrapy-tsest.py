from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
import os
import time

def run_spider():
    print(datetime.now().strftime("%H:%M:%S")," Run the scrapy")
    os.system("scrapy crawl quotes")
    time.sleep(5)


if __name__=="__main__":
    startpath = os.path.abspath(os.path.dirname(__file__))
    relpath = startpath.rsplit("\\",2)[0]
    os.chdir(relpath)
    print("Now, switch current directory to", os.getcwd())
    scheuler = BlockingScheduler()
    scheuler.add_job(run_spider, 'interval', seconds=10, id="job1")
    scheuler.start()
    scheuler.remove_job("job1")
