
import logging
from varinfo import *

p = print
logger = logging.getLogger(__name__)
filelogger = logging.getLogger()
#print(f'__name__: {__name__}')

logging.basicConfig(level=1)

p(varinfo(logging))

logging.debug("hei dette er debug")
logging.info("hei dette er info")
logging.warning("hei dette er warning")
logging.error("hei dette er error")
logging.critical("hei dette er veldig critcal!!")

print("fin")

def log_all(logobj,msg):
    logobj.debug(f'DEBUG-> {msg}')
    logobj.info(f'INFO-> {msg}')
    logobj.warning(f'WARNING-> {msg}')
    logobj.error(f'ERROR-> {msg}')
    logobj.critical(f'CRITICAL-> {msg}')


log_all(logger,'hei')
p(f'Logging level: {logger.level}')
logger.setLevel(21)
log_all(logger,'etter setlevel 100')

p(varinfo(logger))

va = varinfo(logger)






raise SystemExit()




p(varinfo(logger))
p(logger.level)
p(logger.level)