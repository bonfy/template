# Flask Demo Template

本demo主要关注于 Flask + peewee + nginx 的Demo

## 准备

参照[python web 部署：nginx + gunicorn + supervisor + flask mac 平台](http://www.jianshu.com/p/6dce773cb6b8)

Notice: supervisor 暂时没有python3版本的,mac 下可以用 brew install 安装


```cmd
brew install supervisor
brew install nginx

$ pyvenv venv
$ source venv/bin/activate

$ python3 -m pip install flask
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
