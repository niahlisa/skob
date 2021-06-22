FROM python:slim

LABEL maintainer="niayesh abbasi <niahlisa2000@gmail.com>"

EXPOSE 8080

WORKDIR /opt/app

ENV SKOB_AUTHZ_BIND_ADDRESS=0.0.0.0
ENV SKOB_AUTHZ_NUM_WORKERS=4

COPY requiremets.txt .
RUN pip install -r requirements.txt

COPY . .

RUN adduser -M -d /opt/app authz
USER authz:authz 

CMD ./start

