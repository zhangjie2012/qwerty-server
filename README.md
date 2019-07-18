# qwerty-server

[qwerty](http://getqwerty.org/) 的 API server。

## 部署

默认提供了 Dockerfile 文件，支持 [Docker](https://www.docker.com/) 部署，也推荐使用 Docker。

1. 安装 MySQL@5.7，创建存储库和数据库账户密码
1. `cp ./config_example.yml /etc/qwerty.yml`，根据你的网站信息修改配置文件
1. 创建日志目录，`mkdir -p /data/log`
1. 构建镜像: `docker build -t ${image_name} .`
1. 启动服务: `docker run --name qwerty-server -it -d -p 8080:8080 -v /etc/qwerty.yml:/etc/qwerty.yml -v /data/log/:/data/log/ ${image_name}`

测试服务是否正常运行：`curl 0.0.0.0:8080/health_check`，得到 `{"status": "ok"}` 表示运行正常。

## 开发

安装开发环境：

1. 安装 MySQL@5.7
   - macOS：`brew install mysql@5.7`
1. 创建数据库并授权：
   - `create database qwerty charset=utf8mb4`
   - `grant all privileges on qwerty.* to qwerty_user@'localhost' identified by 'qwerty_password'`
1. 安装依赖库: `pip3 install -r requirements.txt`
1. 复制一份配置文件，修改配置: `cp config_example.yml config.yml`

迁移数据库，运行服务：

``` shell
CONFIG_FILE=./config.yml ./manage.py migrate
CONFIG_FILE=./config.yml ./manage.py runserver
```
