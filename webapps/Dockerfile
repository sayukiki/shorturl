FROM python:3.8.6

ENV PYTHONUNBUFFERED 1

RUN pip install Django==3.1.2 \
                django-redis==4.12.1 \
                redis==3.5.3 \
                daphne==2.5.0 \
                aioredis==1.3.1

RUN mkdir /code
WORKDIR /code

COPY ./webapps/docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["bash", "docker-entrypoint.sh"]

EXPOSE 8000
CMD ["start"]