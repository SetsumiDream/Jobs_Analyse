
Jobs_Analyse 开发日志

----------------------------------------------------------

开始时间
2019/12/26

----------------------------------------------------------

项目需求：
	1. 爬虫框架获取招聘网站
	   网站: 拉钩、智联、前程无忧、BOSS直聘
	   需求: 岗位信息，存入数据库，再从数据库导出，形成DF文件
	2. 数据分析
	   需求: 数据分析，机器学习
	3. web页面显示数据情况
	   需求: 页面输入信息爬取，生成分析

----------------------------------------------------------

项目概要设计和详细设计:
	1.待写

----------------------------------------------------------

编码(进度):
	2019/12/26
	 1.创建Git版本管理，创建基本环境 .jobenv
	   创建master、develop、jobs_spider分支
	 2.jobs_spider分支的编写

	2019/12/27
	 1.jobs_spider分支的编写

	2020/01/02
	 1.完成51job、boss直聘、拉钩爬取

	2020/01/04
	 1.完成登录页面

----------------------------------------------------------

测试报告:
	1.

----------------------------------------------------------

验收/发布上线/维护
	占位

----------------------------------------------------------
项目起始记录
----------------------------------------------------------

2019/12/26 详细记录

----------------------------------------------------------

Git项目版本管理

1. 创建虚拟环境
	virtualenv .webenv
	pip install django==1.11.18 mysqlclient redis

2. 创建django项目
	django-admin startproject 

3. git上创建仓库，项目进行git init
	git bash here
	git init

	vi .gitignore
	.git/
	.idea/
	.gitignore

	git add .
	git commit -m '创建了项目'
	git remote add origin git@github.com:SetsumiDream/Jobs_Analyse.git
	git push -u origin master

	git checkout -b develop  # 创建分支
	git push -u origin develop  # 上传分支

	# 设置权限
	Branches 
	add rule

	git checkout -b jobs_spider
	git push -u origin jobs_spider

	修改默认上传
	jobs_spider

jobs_spider分支的编写

scrapy在windows上安装有时会报错
解决办法:
  1.pip install pywin32
  2.https://www.lfd.uci.edu/~gohlke/pythonlibs/#twisted
    下载对应版本Twisted
    pip install 路径文件

1. 安装 pip install scrapy

----------------------------------------------------------

2019/12/27 详细记录

----------------------------------------------------------

今天进行了scrapy框架的学习
主要进行了xpath、规则爬虫、selenium、下载中间件、写入数据库
明天周六，班级组织聚会

下一步计划 开始着手网站的爬取，并存入数据库，再导出成DF文件
第二步计划 django项目 写爬虫前端
第三步计划 爬取数据的显示
第四步计划 机器学习处理数据

----------------------------------------------------------

2019/12/29 详细记录

----------------------------------------------------------

今天规划了下要爬取的字段

1.岗位名称 workname
2.公司名称 company
3.公司类型 cptype
4.公司行业 business
5.工作地点 place
6.工作经验 exp
7.教育水平 edu
8.需要人数 needNum
9.发布时间 time
10.岗位详细 work_msg
11.工资 salary

安装pandas 方便存储
pip install pandas

----------------------------------------------------------

2019/12/30 详细记录

----------------------------------------------------------

今天开始整理爬虫
创建第一个爬虫项目

----------------------------------------------------------

2020/01/02 详细记录

----------------------------------------------------------

https://blog.csdn.net/weixin_39726347/article/details/88061687

BOSS直聘反爬 破解 使用中间件拦截，注入JS代码
pip install mitmproxy==4.0.1

完成51job、BOSS直聘、拉钩网爬虫功能

git add.
git commit -m ""
git push

git上合并版本 New pull request
git checkout develop  切回develp
git pull              拉回版本
git  checkout -b jobs_web    切换分支
git push -u origin jobs_web  上传分支

明日计划编写 django项目
因为时间不多，所以爬虫数据使用51job爬取的数据

----------------------------------------------------------

2020/01/03 详细记录

----------------------------------------------------------

今天开始写django项目
pip install django==1.11.18 mysqlclient redis
django-admin startproject Jobs_web_django

首先我们要配置一下项目
	在项目下，创建templates和static文件夹，用来放置模板和静态文件
	在settings里设置templates和static的路径 
	'DIRS':[os.path.join(BASE_DIR, 'templates')]
	STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]

	顺便把mysql数据库配置也修改了
	DATABASES = {
	    'default': {
	        'ENGINE': 'django.db.backends.mysql',
	        'NAME': 'axf_test',
	        'HOST': '127.0.0.1',
	        'POST': 3306,
	        'USER': '用户名',
	        'PASSWORD': '密码',
	    }
	}
	再顺便用cmd 进入mysql创建我们的数据库
	mysql -u root -p
	密码
	create database axf_test charset=utf8;

我们的视图模块
创建子应用job_view
	python manage.py startapp job_view

	在主应用settings中 INSTALLED_APPS 注册子应用 'job_view',
	主应用路由中，添加url(r'^', include('job_view.urls', namespace='job_view')),

	子应用中
	urls.py 中配置路由
	from django.conf.urls import url
	from . import views
	urlpatterns = [
	    url(r'^login/$', views.login, name='login')
	]

	views.py 中配置视图函数
	from django.shortcuts import render
	def index(request):
	    return render(request, 'login.html')

这个是参考的登录模板
https://blog.csdn.net/weixin_44196651/article/details/89737022

写了一个打字机效果，参考
https://www.cnblogs.com/wangtaobiu/


开始写用户接口模块
startapp user
注册user
然后开始写模型
连接mysql
?serverTimezone=UTC

把views改为api
开始写接口
因为发送短信是常用功能，写成lib包
发送短信第三方接口写到应用的config里面方便修改
这个短信接口需要post请求，安装requests
验证码信息先放在django.core.cache里
键放在common的keys里
错误码放在common的errors里
在lib里写响应格式http.py
def render_json(code=0, data=None):
    dic = {
        'code': code,
        'data': data
    }
    if settings.DEBUG:
        dic_dumps = json.dumps(dic, ensure_ascii=False, indent=4, sort_keys=True)
    else:
        dic_dumps = json.dumps(dic, ensure_ascii=False, separators=[',', ':'])
    return HttpResponse(dic_dumps)

流程
前端
js通过ajax发送post请求
后端
获取post的手机号，生成验证码，通过第三方接口发送短信，返回成功响应并把验证码和手机号以键值对的形式保存到redis
获取post的手机号和验证码，与redis的验证码对比，返回响应

登录功能完成

----------------------------------------------------------

2020/01/04 详细记录

----------------------------------------------------------


----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------