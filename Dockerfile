# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV APP_HOME /app

# Create the working directory
RUN mkdir %APP_HOME%
WORKDIR %APP_HOME%

# Copy the requirements file into the container at /app
COPY Requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r Requirements.txt

# Copy the entire project directory into the container at /app
COPY . .

# Set the port for Streamlits
EXPOSE 8501

# Set the entrypoint for the container
ENTRYPOINT ["streamlit", "run", "Main.py", "--server.port=8501", "--server.address=0.0.0.0"]
