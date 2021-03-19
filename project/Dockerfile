FROM python:3.8.3-alpine
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip3 install --upgrade pip
COPY ./req.txt .
RUN pip3 install -r req.txt

COPY . .
ENTRYPOINT ["/app/entrypoint.sh"]
EXPOSE 8000