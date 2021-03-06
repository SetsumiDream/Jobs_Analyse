# -*- coding: utf-8 -*-

import os
from multiprocessing import cpu_count


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

bind = ["127.0.0.1:9000"]  # 线上环境不会开启在公网 IP 下，一般使用内网 IP
daemon = True  # 是否开启守护进程模式
pidfile = '%s/logs/gunicorn.pid' % BASE_DIR

#workers = cpu_count() * 2
workers = 1
#worker_class = "gevent"  # 指定一个异步处理的库
forwarded_allow_ips = '*'

keepalive = 60
timeout = 30
graceful_timeout = 10
worker_connections = 65535
preload_app = True
# 日志处理
capture_output = True
loglevel = 'info'
errorlog = '%s/logs/gunicorn_error.log' % BASE_DIR
