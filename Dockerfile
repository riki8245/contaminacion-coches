# Use the official Python image as a base
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the contents of the local app directory into the container at /app
COPY . .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Define environment variable
# ENV NAME World

# Run app.py when the container launches
CMD ["python", "app/app.py"]