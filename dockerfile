FROM harbor.in.fii-icloud.com/public-pl/python:3.6.8-centos7-sp

COPY mic22/requirements.txt /app

RUN ls \
 && yum install -y mysql-devel gcc python3-devel \
 && pip3 install --no-cache-dir -U pip \ 
 && pip3 install --no-cache-dir \
         gunicorn \
         gevent \ 
 && pip3 install --no-cache-dir -r requirements.txt \ 
 && yum remove -y \
        gcc \
        python3-devel \
        mysql-devel \
 && yum clean all \
 && rm -rf /var/cache/yum

#COPY microfoudry.ini  /etc/supervisor/conf.d
COPY asyntask.ini  /etc/supervisor/conf.d

COPY ./mic22 /app
