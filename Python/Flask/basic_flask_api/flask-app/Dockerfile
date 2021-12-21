# syntax=docker/dockerfile:1
FROM python:3.7-alpine

# Define the working directory 
WORKDIR /basic_flask_api
# Copy the current directories contents into the contianers files
COPY . . 

## Set flask environment variables 
ENV FLASK_APP=app.py

# copy contents of directory into the docker working directory 
ADD . /basic_flask_api

# Install dependancies from requirements folder
RUN pip3 install -r requirements.txt

# Define command to start container
## The "--host=0.0.0.0" is so that the application can be viewed externally
## (i.e outside the container)
CMD ["flask", "run", "--host=0.0.0.0"]

# To create the image from this docker file run: 
# docker image build -t <name of image> . 
