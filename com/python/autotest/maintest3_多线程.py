"""
python的多线程与锁(一)
threading(更高级别，封装了一些函数，很好的解决了锁的问题)
-原语
 -锁
 -信号量
_thread（低级别）

"""
import _thread
import threading
import logging
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)
loops=[2,4]
#继承threading类，重写里面的run()方法
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name
    #重写thredding类里的run（）方法
    def run(self):
        self.func(*self.args)#解包，把参数解析出来
def loop(nloop,nsec):
    logging.info("start loop " + str(nloop) + "at" + ctime())
    sleep(nsec)
    logging.info("end loop " + str(nloop) +  "at" + ctime())
    # lock.release()

def main():
    logging.info("start all at "+ctime())
    threads=[]
    # locks=[]
    nloops = range(len(loops))
    #加锁操作
    # for i in nloops:
    #     lock = _thread.allocate_lock()
    #     lock.acquire()
    #     locks.append(lock)
    for i  in nloops:
        t = MyThread(loop,(i, loops[i]),loop.__name__)
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()# join() 方法解决了,线程锁的问题
    logging.info("end all at " +ctime())

if __name__ == '__main__':
    main()