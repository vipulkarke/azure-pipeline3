# Use the official Python image as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install the required dependencies
RUN pip install flask

# Expose the Flask port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
