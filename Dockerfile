FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY requirment.txt /code/
RUN pip install -r requirment.txt

COPY . /code