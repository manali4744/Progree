FROM python:3.7.9-slim

# copy project
COPY . /app3

# set work directory
WORKDIR /app3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
Run apt-get update
RUN apt-get -y install gcc  
RUN pip install --upgrade pip setuptools
RUN pip install chatterbot==1.0.2
RUN pip install pytz
 

RUN pip install chatterbot_corpus


CMD [ "python", "./bot.py"]