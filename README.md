# qwerty: a full website solution for programmer


qwerty demo site: <https://www.zhangjiee.com>. Checkout [TODO list](https://www.zhangjiee.com/topic/20).

## Features

+ [x] Blog
+ [x] Topic: a lightweight github issue manager, like notes, wiki
+ [x] MicroBlog: a micro blog
+ [x] Resume
+ [x] About: personal info

## qwerty stack

- this qwerty is just an __api server__, you need a __web client__.

    qwerty support a official [qwerty-client](https://github.com/zhangjie2012/qwerty-client) (based on ant design pro). If you don't like it, you can coding by yourself.

## Deploy

qwerty support Dockerfile, I also recommend use [docker](https://www.docker.com/) deploy service.

1. back-end need MySQL-5.7, you need prepare install
1. `cp ./config_example.yml /etc/qwerty.yml`, then modify it according your site information
1. create log directory: `mkdir -p /data/log`
1. build image: `docker build -t ${image_name} .`
1. run docker: `docker run --name qwerty-server -it -d -p 8080:8080 -v /etc/qwerty.yml:/etc/qwerty.yml -v /data/log/:/data/log/ ${image_name}`

Test service run success, `curl 0.0.0.0:8080/health_check`, you will get `{"status": "ok"}`.

### jekyll to qwerty

1. put jekyll `_posts` to qwerty server has permission to read location
1. `POST` API `/datamgr/import_jekyll_content?token=${token}`, request body(json) `{"dst_dir": "_posts path"}`

## Develop

Install ENV:

1. install MySQL-5.7: `apt install mysql-server`
1. create database ant grant:
   - `create database qwerty charset=utf8mb4`
   - `grant all privileges on qwerty.* to qwerty_user@'localhost' identified by 'qwerty_password'`
1. install server dependent python3 libraries: `pip3 install -r requirements.txt`
1. set configure, copy config and replece config by you need: `cp config_example.yml config_server.yml`

Run:

    CONFIG_FILE=./config_example.yml ./manage.py migrate
    CONFIG_FILE=./config_example.yml ./manage.py runserver
