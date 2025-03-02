FROM python:3.12.3

ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY django.sh .
RUN chmod +x django.sh

EXPOSE 8000

ENTRYPOINT ["/app/django.sh"]