# Pull a base image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Install Curl & Firefox
RUN echo "deb http://deb.debian.org/debian/ unstable main contrib non-free" >> /etc/apt/sources.list.d/debian.list
RUN apt update
RUN apt install -y curl firefox

# Create a working directory for the crawlers project
WORKDIR /app

# Copy requirements to the container
COPY ./Pipfile ./Pipfile.lock /app/

# Install the requirements to the container
RUN pip install pipenv
RUN pipenv install --system --deploy

# Copy the crawlers project files into the working directory
COPY ./ /app

# Open ports on the container
EXPOSE 6800 8000
