FROM python:alpine

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY ./script.py /app

CMD ["kopf", "run", "script.py"]