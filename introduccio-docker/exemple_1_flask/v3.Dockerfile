FROM python:3.8-slim
ENV TZ Europe/Madrid
WORKDIR /myapp
RUN apt-get update && apt-get install -y tzdata \
    && ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure -f noninteractive tzdata \
    && pip3 install flask \
    && rm -rf /var/lib/apt/lists/* \
    && mkdir static
COPY app.py .
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
