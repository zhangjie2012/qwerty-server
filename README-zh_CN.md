# qwerty：技术人网站完整解决方案

[English document](./README.md).

qwerty demo 网站：<https://www.zhangjiee.com>，查看 [TODO](https://www.zhangjiee.com/topic/20)。

## 核心功能

+ [x] 博客（Blog）
+ [x] 话题（Topic）：一个轻量级的 Github issue 管理，用于类似笔记和 Wiki 形式的记录
+ [x] 微博（MicroBlog）：世界纷乱，不如一个人狂欢
+ [x] 简历（Resume）：无需华丽，但有条理
+ [x] 关于（About）：个人介绍

## Web Client

qwerty 只是一个服务端，目前有的客户端有：

+ [qwerty-client](https://github.com/zhangjie2012/qwerty-client)：基于 ant design pro 网页客户端，【官方版本】

## 部署

qwerty 提供了 Dockerfile，推荐使用 [Docker](https://www.docker.com/) 部署。

1. 后端存储使用 MySQL 5.7，需要准备 MySQL 服务
1. `cp ./config_example.yml /etc/qwerty.yml`，根据你的站点信息修改配置：
   + `server`：服务配置，`token` 用于高危 API 的鉴权
   + `site`：站点信息，名称，版权信息和 ICP 备案号
   + `user`：个人信息
   + `db`：填写 MySQL 库名、账号密码等信息
   + `log`：日志配置
1. 创建宿主机日志目录：`mkdir -p /data/log`
1. 构建镜像：`docker build -t ${image_name} .`
1. 启动容器：`docker run --name qwerty-server -it -d -p 8080:8080 -v /etc/qwerty.yml:/etc/qwerty.yml -v /data/log/:/data/log/ ${image_name}`
1. 测试服务：`curl 0.0.0.0:8080/health_check` -> `{"status": "ok"}` 表示成功

### 从 Jekyll 迁移到 qwerty

1. 将 Jekyll 的 `_posts` 置于 qwerty server 可被访问的目录下
1. `POST` 调用 API `/datamgr/import_jekyll_content?token=${token}` 执行导入操作，request body 为 `{"dst_dir": "_posts path"}`

注意：qwerty 不支持静态资源，如果原博客使用了图片资源，请将图片提交到云存储上，然后手动修改文章内容使之生效。

## 本地开发

推荐使用 Docker 开发与调试。

容器网络：

    docker network create -d bridge qwerty

MySQL：

    docker pull mysql:5.7
    docker run -it -d --name qwerty-mysql --restart=always --network qwerty -e MYSQL_ROOT_PASSWORD=qwerty-pwd  -p 3306:3306 mysql:5.7 --character-set-server=utf8mb4 --collation-server=utf8mb4_unicode_ci
    docker exec -it qwerty-mysql mysql -uroot -pqwerty-pwd -e "create database qwerty charset=utf8mb4"

安装依赖：

    pip3 install -r requirements.txt

启动：

    CONFIG_FILE=./config_example.yml ./manage.py migrate
    CONFIG_FILE=./config_example.yml ./manage.py runserver
