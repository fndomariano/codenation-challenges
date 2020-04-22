FROM python:3
MAINTAINER Fernando Mariano <fernando.mar16@gmail.com>
RUN mkdir /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r /app/requirements.txt
	
WORKDIR /app