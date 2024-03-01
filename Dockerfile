FROM python:3.11

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

VOLUME [ "/app" ]


EXPOSE 8000

# Run the app:
CMD python manage.py runserver 0.0.0.0:8000