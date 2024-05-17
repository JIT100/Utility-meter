FROM python:3.11-alpine

ENV PYTHONUNBUFFERED 1

WORKDIR /app
COPY ./requirements.txt  /app/requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["sh", "/app/entrypoint.sh"]