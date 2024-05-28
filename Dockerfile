# Use an official Python runtime as a parent image
FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

RUN apt update && apt install -y build-essential libpq-dev 


COPY requirements.txt /app/
# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Add the current directory contents into the container at /app
COPY . /app/

# Collect static files
RUN python manage.py collectstatic --noinput

# Make port 90 available to the world outside this container
EXPOSE 8000

# Run app.py when the container launches
CMD ["gunicorn", "socialmedia.wsgi:application", "--bind", "0.0.0.0:8000", "--reload"]


