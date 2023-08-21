FROM python:3.9

WORKDIR /app/backend

COPY requirements.txt /app/backend
RUN pip install -r requirements.txt
RUN pip install mysqlclient

# Copy the entrypoint script into the container
COPY entrypoint.sh /app/entrypoint.sh



COPY . /app/backend

EXPOSE 8000

 CMD python /app/backend/manage.py makemigrations
 CMD python /app/backend/manage.py migrate

CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 web_application.wsgi
# CMD python /app/backend/manage.py runserver 0.0.0.0:8080

# docker file for staging encv

#docker file of django

#docker file for django djnah=o api github api

#DOCKER FILES T-21 AUG2023

#DOCKER FILES PHASE 2

#Docker files phase 3

#Docker file in phase 4

#Docker file in phase 5

