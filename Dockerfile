FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
RUN apk add --no-cache jpeg-dev zlib-dev
RUN apk add --no-cache --virtual .build-deps build-base linux-headers \
    && pip install Pillow
COPY requirements.txt /
RUN pip install -r /requirements.txt
RUN mkdir -p ~/app
COPY . ~/app
WORKDIR ~/app
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
