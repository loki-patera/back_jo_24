FROM python:3.12.6-alpine

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUBUFFERED=1

WORKDIR /app/back

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .