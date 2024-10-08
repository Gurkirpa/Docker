###########################################
# BASE IMAGE
###########################################

FROM ubuntu AS build

Workdir /app

RUN apt-get update && apt-get install -y python3 

COPY . /app

CMD ["python3", "app.py"]
