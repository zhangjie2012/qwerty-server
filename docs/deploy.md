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

1. 生成 docker 镜像：`docker build -t ${your_image_name} .`
2. 宿主机创建配置文件和日志目录：
    + `cp ./config_example.yml /data/qwerty.yml`：修改站点配置
    + `mkdir /data/log`
3. 启动容器：`docker run --name qwerty-server -it -d -p 8080:8080 -v /data/qwerty.yml:/etc/qwerty.yml -v /data/log/:/data/log/ -v /data/backup/:/data/backup/ --network qwerty ${your_image_name}`

注意：如果 MySQL57 也是通过 docker 启动的话，注意设置 `network`。
