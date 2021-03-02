"""
python的多线程
"""
import logging
from time import sleep,ctime

logging.basicConfig(level=logging.INFO)

def loop0():
    logging.info("start loop0 at "+ ctime())
    sleep(4)
    logging.info("end loop0 at "+ ctime())
def loop1():
    logging.info("start loop1 at "+ ctime())
    sleep(2)
    logging.info("end loop1 at "+ ctime())

def main():
    logging.info("start all at "+ctime())
    loop0()
    loop1()
    logging.info("end all at " +ctime())

if __name__ == '__main__':
    main()