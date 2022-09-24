import demo
import logging

logger=logging.getLogger(__name__)

logger.debug("Start of hello program")

def add_number():
    a=10
    b=20
    logger.info("Addition:",a+b)

if __name__=='__main__':
    add_number()