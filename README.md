### 一个python django实现 增删改查案例
本项目使用的 python3和django 2.0版本 还需要安装Psycopg2用来连接数据库，关于Psycopg2的使用请点击 [Psycopg2](http://initd.org/psycopg/docs/install.html)<br/>
同时需要搭建一个自己的本地数据库服务我用的是psql，并且把项目里的settings.py文件里的数据库配置修改成你自己的<br/>
blog module下的dbaseconf.py是连接的psql的数据库class也需要修改<br/>
在install过程中 如出现 ...not found等字样 请自行根据提示下载，因为我也忘了都需要啥了....<br/>
安装时 请使用
```
pip3 install xxx
```

### 启动服务
我开发用的vscode 把项目下载到本地后使用vscode打开 F5 启动服务 需要安装python插件<br/>
也可以使用命令行 进入到项目根目录运行 
```
python3 manage.py runserver
```

### 页面访问地址
```
http://127.0.0.1:8000/static/pages/index.html
```