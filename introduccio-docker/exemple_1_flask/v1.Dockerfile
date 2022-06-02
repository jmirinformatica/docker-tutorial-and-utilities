FROM ubuntu:20.04
ENV TZ Europe/Madrid
RUN apt-get update
RUN apt-get install -y tzdata
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && dpkg-reconfigure -f noninteractive tzdata
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN pip3 install flask
WORKDIR /myapp
RUN mkdir static
COPY app.py .
ENTRYPOINT [ "python3" ]
CMD [ "app.py" ]
