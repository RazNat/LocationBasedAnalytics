FROM mysql/mysql-server:latest-aarch64

ENV MYSQL_DATABASE=MBTAdb \
    MYSQL_ROOT_PASSWORD=MyNewPass

ADD MBTA.sql /docker-entrypoint-initdb.d

EXPOSE 3306