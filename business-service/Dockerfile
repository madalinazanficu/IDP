FROM python:3.8

# Set the working directory inside the container
WORKDIR /business-service

# Copy the requirments file and install deps
COPY business-service/requirements.txt /business-service/
RUN pip install -r requirements.txt

# Copy the source code into the container
ADD business-service/*.py /business-service/

# Expose the port that the Flask app runs on
EXPOSE 4001

# Define the command to run the app
CMD ["python3", "-u", "/business-service/server.py"]