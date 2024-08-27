# Use an official Python image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Install required dependencies
RUN apt-get update && apt-get install -y \
    libpq-dev gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . /app

# Collect static files
RUN python manage.py collectstatic --noinput

# Expose the port Django will run on
EXPOSE 8000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "pr_academy360.wsgi:application"]
