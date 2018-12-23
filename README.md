# qwerty: a full website solution for programmer

Qwerty demo site: <https://www.zhangjiee.com>. Checkout [TODO list](https://www.zhangjiee.com/topic/20).

## Features

+ [x] Blog
+ [x] Topic: a lightweight github issue manager, like notes, wiki.
+ [x] MicroBlog: a micro blog
+ [x] Resume
+ [x] About: personal info

## Web Client

Qwerty is a back-end server, you need a web client, qwerty support a official [qwerty-client](https://github.com/zhangjie2012/qwerty-client) (based on ant design pro). If you don't like it, you can coding by yourself.

## Deploy

Qwerty support Dockerfile, I also recommend use [docker](https://www.docker.com/) deploy service.

1. back-end need MySQL-5.7, you need prepare one
1. `cp ./config_example.yml /etc/qwerty.yml`, then modify it according your site information
1. create log directory: `mkdir -p /data/log`
1. build image: `docker build -t ${image_name} .`
1. run docker: `docker run --name qwerty-server -it -d -p 8080:8080 -v /etc/qwerty.yml:/etc/qwerty.yml -v /data/log/:/data/log/ ${image_name}`

Test service run success, `curl 0.0.0.0:8080/health_check`, you will get `{"status": "ok"}`.

### jekyll to qwerty

1. put jekyll `_posts` to qwerty server has permission to read location
1. `POST` API `/datamgr/import_jekyll_content?token=${token}`, request body(json) `{"dst_dir": "_posts path"}`

## Develop

I recommand use docker.

Create docker network:

    docker network create -d bridge qwerty

Install MySQL-5.7:

    docker pull mysql:5.7
    docker run -it -d --name qwerty-mysql --restart=always --network qwerty -e MYSQL_ROOT_PASSWORD=qwerty-pwd  -p 3306:3306 mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    docker exec -it qwerty-mysql mysql -uroot -pqwerty-pwd -e "create database qwerty charset=utf8mb4"

Install dependent library:

    pip3 install -r requirements.txt

Run:

    CONFIG_FILE=./config_example.yml ./manage.py migrate
    CONFIG_FILE=./config_example.yml ./manage.py runserver
