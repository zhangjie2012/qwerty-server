# 部署

## 开发环境

容器网络：

    docker network create -d bridge qwerty

MySQL：

    docker pull mysql:5.7
    docker run -it -d --name qwerty-mysql --restart=always --network qwerty -e MYSQL_ROOT_PASSWORD=qwerty-pwd -p 3306:3306 mysql:5.7
    docker exec -it dae2c9b181a5 mysql -uroot -pqwerty-pwd -e "create database qwerty charset=utf8mb4"

安装依赖：

    pip3 install -r requirements.txt

配置文件，默认读取位置为 `/etc/qwerty.yml`。可通过环境变量 `CONFIG_FILE` 指定目录。

启动 server：

    ./manage.py runserver


## 生产环境

TODO
