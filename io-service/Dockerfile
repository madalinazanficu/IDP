FROM python:3.8

# Copy the requirments file and install deps
COPY io-service/requirements.txt .
RUN pip install -r requirements.txt


# Set the working directory inside the container
WORKDIR /auth-server

# Copy the source code into the container
COPY io-service/server.py .
COPY io-service/db_entities.py .

# Expose the port that the Flask app runs on
EXPOSE 5001

# Define the command to run the app
CMD ["python3", "-u", "server.py"]