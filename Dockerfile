# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app


# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Collect static files (optional)
RUN python manage.py collectstatic --noinput

# Run migrations (optional)
RUN python manage.py migrate --noinput

# Make port 8000 available to the world outside this container
EXPOSE 8000

# Define environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Run migrations and start the application using gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pr_academy360.wsgi:application"]
