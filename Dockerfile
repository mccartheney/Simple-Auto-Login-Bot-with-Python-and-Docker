FROM python:3.9-slim

WORKDIR /app

COPY src/ /app

RUN pip install selenium
RUN pip install python-dotenv

RUN apt-get update && apt-get install -y chromium-driver

CMD python main.py
