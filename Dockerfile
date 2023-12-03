from python:3.11-slim

RUN mkdir app
RUN cd app

WORKDIR /app

ADD . /app

RUN pip install --upgrade pip

RUN pip3 install -r requirements.txt

CMD python main.py
