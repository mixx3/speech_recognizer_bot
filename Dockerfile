FROM python:3.10
WORKDIR /app

COPY ./requirements.txt /app/

RUN pip install --no-cache-dir -r /app/requirements.txt
RUN apt-get -y update
RUN apt-get install -y ffmpeg

ADD alembic.ini /app/
ADD .env /app/.env
ADD migrations /app/migrations
ADD bot /app/bot


CMD ["python3", "-m", "bot"]