FROM python:3.9-slim

WORKDIR /code

# Copy requirements.txt to the working directory
COPY ./requirements.txt /code/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy the application code to the working directory
COPY ./app /code/app

# Set the PYTHONPATH
ENV PYTHONPATH=/code

# Set the working directory to /code/app
WORKDIR /code/app

# Make port 5050 available to the world outside this container
# EXPOSE 5050
EXPOSE 8888

# Run the application
CMD ["chainlit", "run", "main.py", "-h", "--port", "5050"]
