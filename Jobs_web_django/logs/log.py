import logging
from logging import handlers


fmt = '%(asctime)s %(levelname)7.7s %(funcName)s: %(message)s'
formatter = logging.Formatter(fmt, datefmt="%Y-%m-%d %H:%M:%S")

# 设置 handler
handler = logging.handlers.TimedRotatingFileHandler('myapp.log', when='D', backupCount=30)
handler.setFormatter(formatter)

# 定义 logger 对象
logger = logging.getLogger("MyApp")
logger.addHandler(handler)
logger.setLevel(logging.ERROR)