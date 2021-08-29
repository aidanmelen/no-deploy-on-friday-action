FROM python:3.9-alpine

ENV NO_DEPLOYMENT_DAYS='Friday, Saturday, Sunday'
ENV TZ='UTC'
ENV COUNTRY='US'
ENV HOLIDAYS='true'

COPY requirements.txt /requirements.txt 

RUN pip install -r /requirements.txt

COPY src/app /app

WORKDIR /app

ENTRYPOINT ["python"]

CMD ["/app/main.py"]
