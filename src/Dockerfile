FROM python:3.11.9-slim

WORKDIR /app

COPY requirements/requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .

ENV PYTHONUNBUFFERED=1

CMD ["sh", "-c", "./runserver.sh"]