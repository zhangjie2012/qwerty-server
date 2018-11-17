FROM python:3.7

RUN apt-get update && \
    apt-get install -y supervisor

COPY requirements.txt /requirements.txt
RUN pip3 install --no-cache-dir -r /requirements.txt -i https://pypi.douban.com/simple

RUN ln -sf /usr/share/zoneinfo/Asia/Shanghai  /etc/localtime

WORKDIR /code
COPY /uwsgi.ini /code
COPY /src/ /code
COPY /supervisor-app.conf /etc/supervisor/conf.d/

EXPOSE 8080

CMD ["supervisord", "-n"]
