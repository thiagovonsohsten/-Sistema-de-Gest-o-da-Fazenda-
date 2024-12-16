FROM mysql:8.0

ENV MYSQL_ROOT_PASSWORD=romero13
ENV MYSQL_DATABASE=fazenda_db

COPY init.sql /docker-entrypoint-initdb.d/
