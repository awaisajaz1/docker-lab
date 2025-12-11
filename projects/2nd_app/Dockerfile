# pull the base image 
FROM python:3.9-slim

# set teh working directory
WORKDIR /myapp

# copy the current directory contents into the container at /myapp
COPY . /myapp

# install dependencies
RUN pip install --no-cache-dir -r requirement.txt

# expose port, port mapping
# EXPOSE 5000

# Command to run on container start
CMD ["python", "app.py"]