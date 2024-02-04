# Use the official Python image as the base image
FROM python:3.9

# Set environment variables for Python to run in unbuffered mode
ENV PYTHONUNBUFFERED 1

# Create and set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY . /app/

# Install dependencies using pip
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
 

# Expose the port that the Django development server will run on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
