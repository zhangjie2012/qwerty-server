# qwerty: A full personal website by django

## 开发环境部署

容器网络：

    docker network create -d bridge qwerty

MySQL：

    docker pull mysql:5.7
    docker run -it -d --name qwerty-mysql --restart=always --network qwerty -e MYSQL_ROOT_PASSWORD=qwerty-pwd -p 3306:3306 mysql:5.7
    docker exec -it dae2c9b181a5 mysql -uroot -pqwerty-pwd -e "create database qwerty charset=utf8mb4"

启动 server：

    DB_NAME=qwerty DB_USER=root DB_PASSWD=qwerty-pwd DB_HOST=0.0.0.0 DB_PORT=3306 ./manage.py runserver
