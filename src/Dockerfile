# Use the official Python image.
# 3.12.4-slim is a lighter version of Python to reduce the image size.
FROM python:3.12.4-slim

ENV PYTHONUNBUFFERED=1

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install -r requirements.txt