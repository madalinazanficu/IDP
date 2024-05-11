FROM python:3.8

# Copy the requirments file and install deps
COPY business-service/requirements.txt .
RUN pip install -r requirements.txt

# Set the working directory inside the container
WORKDIR /business-service

# Copy the source code into the container
COPY business-service/server.py .
COPY auth-server/utils.py .
COPY business-service/business_utils.py .

# Expose the port that the Flask app runs on
EXPOSE 6000

# Define the command to run the app
CMD ["python3", "-u", "server.py"]