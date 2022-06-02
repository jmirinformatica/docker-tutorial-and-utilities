FROM ubuntu:20.04
ENV TZ Europe/Madrid
RUN apt-get update && apt-get install -y tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime  && dpkg-reconfigure -f noninteractive tzdata \
    && apt-get install -y python3 python3-pip \
    && pip3 install flask \
    && apt-get remove -y --purge python3-pip \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir static
WORKDIR /myapp
COPY app.py .
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
