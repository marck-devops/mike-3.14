# Use the official Python image from Docker Hub as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . /app

# Install the required dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose port 5000 so the app is accessible externally
EXPOSE 5000

# Set the default command to run the Flask app
CMD ["python", "app.py"]
