FROM python:3.8

# Set the working directory inside the container
WORKDIR /auth-server

# Copy the requirments file and install deps
COPY auth-server/requirements.txt /auth-server/
RUN pip install -r requirements.txt

# Copy the source code into the container
ADD auth-server/*.py /auth-server/

# Expose the port that the Flask app runs on
EXPOSE 6001

# Define the command to run the app
CMD ["python3", "-u", "/auth-server/server.py"]