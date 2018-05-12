import schedule
import time
import datetime
import threading

def job():
    print("I'm running on thread %s" % threading.current_thread())
    print('time' + str(datetime.datetime.now()))

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


if __name__ == "__main__":

    schedule.every(10).seconds.do(run_threaded, job)
    schedule.every(10).seconds.do(run_threaded, job)
    schedule.every(10).seconds.do(run_threaded, job)

    while 1:
        schedule.run_pending()
        time.sleep(1)