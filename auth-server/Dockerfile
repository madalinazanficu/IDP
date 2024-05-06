FROM python:3.8

# Copy the requirments file and install deps
COPY auth-server/requirements.txt .
RUN pip install -r requirements.txt

# Set the working directory inside the container
WORKDIR /auth-server

# Copy the source code into the container
COPY auth-server/server.py .
COPY auth-server/db_entities.py .
COPY auth-server/utils.py .

# Expose the port that the Flask app runs on
EXPOSE 6000

# Define the command to run the app
CMD ["python3", "-u", "server.py"]