FROM python:3.8

# Copy the requirments file and install deps
COPY server/requirements.txt .
RUN pip install -r requirements.txt

# Set the working directory inside the container
WORKDIR /auth-server

# Copy the source code into the container
COPY server/app.py .
COPY server/db_entities.py .

# Expose the port that the Flask app runs on
EXPOSE 6000

# Define the command to run the app
CMD ["python3", "server.py"]