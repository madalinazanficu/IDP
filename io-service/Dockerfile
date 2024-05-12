FROM python:3.8

# Set the working directory inside the container
WORKDIR /io-service

# Copy the requirments file and install deps
COPY io-service/requirements.txt /io-service/
RUN pip install -r requirements.txt

# Copy the source code into the container
ADD io-service/*.py /io-service/

# Expose the port that the Flask app runs on
EXPOSE 5001

# Define the command to run the app
CMD ["python3", "-u", "/io-service/server.py"]