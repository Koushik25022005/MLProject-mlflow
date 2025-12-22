FROM python:3.11-bullseye

RUN apt-get update -y && apt-get install awscli -y
WORKDIR /app

COPY . /app
RUN pip install -r requirements.txt

CMD ["python", "app.py"]
