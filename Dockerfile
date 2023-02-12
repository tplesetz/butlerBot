FROM python:3.10-alpine

WORKDIR /butlerBot

COPY requirements.txt .env ./

RUN apk add --no-cache --virtual .build-deps build-base && \
    pip install -r requirements.txt && \
    apk del .build-deps

COPY butlerbot.py .

CMD ["python", "butlerbot.py"]
