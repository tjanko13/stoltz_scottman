FROM ubuntu:20.04
RUN apt-get update -y
RUN apt-get install -y python3.7
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential
COPY . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
ENTRYPOINT ["python3"]
CMD ["app.py"]