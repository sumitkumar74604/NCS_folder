# Use an official Python runtime as a parent image
FROM python:3.9-slim

# # Set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install dependencies
RUN pip install --upgrade pip
RUN pip install virtualenv

# Create a virtual environment
RUN python -m virtualenv env1

# Activate the virtual environment
SHELL ["/bin/bash", "-c"]
RUN source env1/bin/activate && \
    pip install django==4.2.11
RUN  pip install -r requirements.txt

# Expose the port the app runs on
EXPOSE 8000

# Run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

