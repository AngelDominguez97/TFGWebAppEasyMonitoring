FROM python:3.10.4

RUN apt-get update && apt-get install -y openssh-client

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./api /code/api

COPY ./main.py /code/main.py

COPY ./.env /code/.env

COPY ./SSL /code/SSL

CMD ["uvicorn", "main:app", "--port ", "8432", "-ssl-keyfile", "./SSL/server.key", "--ssl-certificate", "./SSL/server.crt"]