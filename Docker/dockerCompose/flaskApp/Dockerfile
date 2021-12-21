# syntax=docker/dockerfile:1

# This defines an existing image that will be used as a foundation for our own image
FROM python:3.7-alpine 

# WORKDIR defines the directory that will be used as the containers "root" folder
# any further commands such as COPY, ADD or RUN will be run with this as the "/" (project root) location
WORKDIR /docker-flask-test

# COPY adds files to the working directory 
# Copy the current directories contents into the contianers files
# The below commands is copying all of the ./ into the container project root (which at the moment is "/docker-flask-test")
COPY . .

# EXPOSE does *not* publish the port, it only gets everything ready 
# to set ports for a container it has to be done in the docker run command
# docker run -p 5000:5000 <image> 
EXPOSE 5000

## ENV allows us to set environment variables, this can be useful if further commands such as shell scripts requires existing paramters
## Set flask environment variables 
ENV FLASK_APP=app.py

# ADD is the same as COPY but with the ability to grab remote files, and also extract/unzip compressed files such as .tar and .zip
# copy contents of directory into the docker working directory 
ADD . /docker-flask-test

# Install dependancies from requirements folder
# RUN allows us to execute commands before our container starts up
# These commands run when we build the docker image
RUN pip3 install -r requirements.txt


# Define command to start container
## The "--host=0.0.0.0" is so that the application can be viewed externally
## (i.e outside the container)
# CMD allows us to define a default command that is used when someone types in "docker run <image>"
# if they add on any extra commands when running a image, this command will be ignored
CMD ["flask", "run", "--host=0.0.0.0"]

# To create the image from this docker file run: 
# docker image build -t <name of image> . 
