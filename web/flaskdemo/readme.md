# Flask Demo Template

本demo主要关注于 Flask + peewee + nginx 的Demo

## 配置篇

参照[python web 部署：nginx + gunicorn + supervisor + flask mac 平台](http://www.jianshu.com/p/6dce773cb6b8)

Notice: supervisor 暂时没有python3版本的,mac 下可以用 brew install 安装


```cmd
brew install supervisor
brew install nginx

$ pyvenv venv
$ source venv/bin/activate

$ python3 -m pip install -r req.txt
```

### supervisor配置

```cmd
$ echo_supervisord_conf > supervisor.conf           # 生成 supervisor 默认配置文件
$ vim supervisor.conf                               # 修改 supervisor 配置文件，添加 gunicorn 进程管理
```
在最后加入：
```
[program:app]
command=/Users/bonfy/Desktop/Github/template/web/flaskdemo/venv/bin/gunicorn -w4 -b0.0.0.0:5000 app:app      ; supervisor启动命令
directory=/Users/bonfy/Desktop/Github/template/web/flaskdemo                            ; 项目的文件夹路径
startsecs=0                                                                             ; 启动时间
stopwaitsecs=0                                                                          ; 终止等待时间
autostart=false                                                                         ; 是否自动启动
autorestart=false                                                                       ; 是否自动重启
stdout_logfile=/Users/bonfy/Desktop/Github/template/web/flaskdemo/log/gunicorn.log      ; log 日志
stderr_logfile=/Users/bonfy/Desktop/Github/template/web/flaskdemo/log/gunicorn.err
```

如果要一起加入nginx

```
[program:nginx]
;command=/usr/sbin/nginx                          ; Linux
command=/usr/local/Cellar/nginx/1.10.2_1/bin/nginx
startsecs=0
stopwaitsecs=0
autostart=false
autorestart=false
stdout_logfile=/Users/bonfy/Desktop/Github/template/web/flaskdemo/log/nginx.log
stderr_logfile=/Users/bonfy/Desktop/Github/template/web/flaskdemo/log/nginx.err
```

如果要激活管理界面

```
supervisor 还有一个web的管理界面，可以激活。更改下配置

[inet_http_server]         ; inet (TCP) server disabled by default
port=127.0.0.1:9001        ; (ip_address:port specifier, *:port for all iface)
username=user              ; (default is no username (open server))
password=123               ; (default is no password (open server))

[supervisorctl]
serverurl=unix:///tmp/supervisor.sock ; use a unix:// URL  for a unix socket
serverurl=http://127.0.0.1:9001       ; use an http:// url to specify an inet socket
username=user                         ; should be same as http_username if set
password=123                          ; should be same as http_password if set
;prompt=mysupervisor                  ; cmd line prompt (default "supervisor")
;history_file=~/.sc_history           ; use readline history if available
```

### nginx 配置

brew 安装的nginx
位置：

```cmd             
/usr/local/Cellar/nginx/1.10.1/bin/nginx     #启动nginx的路径
/usr/local/etc/nginx/nginx.conf              #nginx 的配置文件    
```

nginx.conf 最后有一句

```
    include servers/*;
```

所以我们配置flask只要

```cmd
$ cd /usr/local/etc/nginx/
$ mkdir servers

$ cp location/flask.conf servers/        # copy flask.conf 到servers
```

```config
server {
    listen 80;                           # 表示访问nginx服务器的地址是127.0.01:1024
    # server_name example.org;           # 这是HOST机器的外部域名，用地址也行

    location / {
        proxy_pass http://127.0.0.1:5000; # 这里是指向 gunicorn host 的服务地址
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

  }

```

### nginx 命令

```cmd
nginx           # 启动nginx
nginx -t        # 检查配置文件ngnix.conf的正确性命令
nginx -s reload # 重新载入配置文件
nginx -s reopen # 重启 Nginx
nginx -s stop   # 停止 Nginx
```

### supervisor命令

```cmd
supervisord -c supervisor.conf                             # 通过配置文件启动supervisor
supervisorctl -c supervisor.conf status                    # 察看supervisor的状态
supervisorctl -c supervisor.conf reload                    # 重新载入 配置文件
supervisorctl -c supervisor.conf start [all]|[appname]     # 启动指定/所有 supervisor管理的程序进程
supervisorctl -c supervisor.conf stop [all]|[appname]      # 关闭指定/所有 supervisor管理的程序进程
```

nginx 在supervisor monitor 中永远都是 status: exited; 原因见 [Running (and monitoring) nginx with supervisord](http://serverfault.com/questions/647357/running-and-monitoring-nginx-with-supervisord)

> To ensure that your nginx is running with supervisord you have to set 'daemon off' in your nginx.conf (see also nginx docu at [http://nginx.org/en/docs/ngx_core_module.html#daemon](http://nginx.org/en/docs/ngx_core_module.html#daemon)).
