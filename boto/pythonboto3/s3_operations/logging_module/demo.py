import logging

logger=logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

f=logging.Formatter('%(levelname)s-%(message)s')

fh=logging.FileHandler('demo.log')
fh.setFormatter(f)

logger.addHandler(fh)

logger.debug("Start of demo Program")


def employee():
    print("Employee name:")

if __name__=='__main__':
    employee()