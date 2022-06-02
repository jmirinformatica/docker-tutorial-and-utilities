FROM python:3.8-slim
ENV TZ Europe/Madrid
WORKDIR /myapp
RUN apt-get update && apt-get install -y tzdata gcc \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure -f noninteractive tzdata \
    && pip3 install flask \
    && pip3 install uwsgi \
    && apt-get remove --purge -y gcc \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* 

COPY *.py ./
COPY templates templates/
EXPOSE 9981/tcp
ENTRYPOINT [ "uwsgi" ]
CMD [ "--socket", "0.0.0.0:9981", "--protocol=http", "--wsgi", "wsgi:app" ]
