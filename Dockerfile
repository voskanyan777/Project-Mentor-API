FROM python:3.10

WORKDIR /application

COPY req.txt .

RUN pip install --no-cache-dir -r req.txt

COPY . .

WORKDIR /application/app

ENV DB_NAME postgres
ENV DB_USER postgres
ENV DB_PASS postgres
ENV DB_HOST postgres_db
ENV DB_PORT 5432
ENV SECRET_AUTH_KEY SECRETAUTHKEY
ENV EMAIL_LOGIN pro.connect.platform@gmail.com
ENV EMAIL_PASSWORD irbp rrol kroc zyts
