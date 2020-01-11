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




