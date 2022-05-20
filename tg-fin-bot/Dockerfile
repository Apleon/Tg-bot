FROM python:3.8

WORKDIR /home

ENV TELEGRAM_API_TOKEN="5391985305:AAFDP_BgiMPcrZfW7kqw-c-V_Ly3GYhzwc8"
ENV TELEGRAM_ACCESS_ID="598219952"

ENV TZ=Europe/Minsk
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN pip install -U pip aiogram pytz && apt-get update && apt-get install sqlite3
COPY *.py ./
COPY createdb.sql ./

ENTRYPOINT ["python", "server.py"]

