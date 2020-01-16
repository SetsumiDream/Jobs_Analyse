收集静态文件
python manage.py collectstatic

收集依赖包
pip freeze > requirments.txt
安装依赖包
pip install -r requirments.txt

启动uWSGI
uwsgi --ini uwsgi.ini
ps -ef|grep uwsgi
关闭
uwsgi --stop uwsgi.pid
kill -9 n

启动gunicorn
pip install gunicorn
pip install gevent
gunicorn -c Jobs_web_django/gunicorn_config.py Jobs_web_django.wsgi
ps aux|grep gunicorn

kill `cat logs/gunicorn.pid`


开启nginx
nginx -c /var/www/Jobs_web_django/nginx.conf
关闭
nginx -s stop

上线服务器访问
http://49.234.125.109/

celery 配置
pip install supervisor
mkdir /etc/supervisor
echo_supervisord_conf > /etc/supervisor/supervisord.conf
mkdir supervisord.conf.d
cd supervisord.conf.d
touch celeryd_worker.conf

unlink /var/run/supervisor.sock
unlink /tmp/supervisor.sock

/root/.virtualenvs/jobenv/bin/supervisord -c supervisord.conf
supervisorctl status
supervisorctl update
supervisorctl reload
supervisorctl start all

https://www.jianshu.com/p/9869cd1cbefe 配置
https://blog.csdn.net/qq_18863573/article/details/52437689
https://blog.csdn.net/sdafhkjas/article/details/102780983 解决错误

linux 不能安装的包
matplotlib==3.1.2
mysqlclient==1.4.6
pandas==0.25.3





