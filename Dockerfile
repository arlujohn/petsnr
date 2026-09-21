# Use an official lightweight Python image
FROM python:3.14-slim

# Set environment variables to optimize Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container
WORKDIR /app

# Additional Command lines
RUN apt-get update && apt-get install -y --no-install-recommends \
    procps \
    gcc \
    libpq-dev \
    curl \
    telnet \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file first for better caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn
# Copy the rest of the application code
COPY . /app/

# Expose the default Django port
EXPOSE 8000

# Run the Django development server
CMD ["gunicorn", "--bind","0.0.0.0:8000","petsnr.wsgi:application"]
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]   