FROM ubuntu:latest

#set working directory
WORKDIR /app

#copy eveything from current folder to working directory
COPY . /app

#install system dependencies
RUN apt-get update && apt-get install -y python3 python3-pip

#start processing with cmd
CMD ["python3", "app.py"]
