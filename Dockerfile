# Use the official Python image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /portfolio

# Copy the entire project into the container
COPY . /portfolio

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=/portfolio

RUN apt-get update && apt-get install -y build-essential
RUN pip install --upgrade pip
RUN pip install gunicorn django

# Expose port 8000 for the Django development server final
EXPOSE 8000

# Default command to run the Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "portfolio.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "5"]