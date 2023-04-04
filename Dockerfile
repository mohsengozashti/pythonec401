FROM python:alpine3.17
WORKDIR /app
RUN pip install --no-cache-dir sqlalchemy requests flask

COPY . .

ENV FLASK_APP=main.py
ENV FLASK_ENV=development

CMD ["flask","run","==host=0.0.0.0"]

EXPOSE 5000
