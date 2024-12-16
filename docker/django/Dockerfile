FROM python:3.10-slim
WORKDIR /
COPY ../tauth/requirements.txt requirements.txt

RUN pip3 install -r requirements.txt
RUN mkdir tauth
WORKDIR /tauth
ENTRYPOINT python
