# pull the base image 
FROM python:3.9-slim

# set teh working directory
WORKDIR /myapp

# copy the current directory contents into the container at /myapp
COPY . /myapp

# install dependencies
# RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Command to run on container start
CMD ["python", "app.py"]