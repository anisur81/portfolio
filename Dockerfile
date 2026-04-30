# Use the official Python image
FROM python:3.12.3

# Set the working directory in the container
WORKDIR /app

# Copy the entire project into the container
COPY . .

RUN pip install gunicorn

# Expose port 8000 for the Django development server
EXPOSE 8000

# Default command to run the Django server
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["gunicorn", "devsecops-portfolio.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]