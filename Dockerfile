FROM python:3.9.7-slim-buster as builder
RUN apt-get update && apt-get clean
COPY requirements.txt /build/
WORKDIR /build/
RUN pip install -U pip && pip install -r requirements.txt

FROM python:3.9.7-slim-buster as app
COPY --from=builder /build/ /app/
COPY --from=builder /usr/local/lib/ /usr/local/lib/

RUN apt-get update && apt-get install -y sqlite3 libsqlite3-dev
RUN mkdir /db
RUN /usr/bin/sqlite3 /db/putzplan.db
WORKDIR /app/
COPY . /app/

VOLUME [ "/db" ]
EXPOSE 3000
ENTRYPOINT python main.py

#
# docker run -e SLACK_SIGNING_SECRET=$SLACK_SIGNING_SECRET -e SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN -e PORT=3000 -p 3000:3000 -it your-repo/hello-bolt
#