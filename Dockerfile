FROM ubuntu:20.04

# Update OS and install required packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    libssl-dev


# Add requirements.txt
COPY requirements.txt /webapp/

# Install uwsgi Python web server
RUN pip3 install uwsgi

# Install app requirements
RUN pip3 install -r /webapp/requirements.txt

# Create app directory
COPY . /webapp/

# Set the default directory for our environment
ENV HOME /webapp
WORKDIR /webapp

# Expose port 8000 for uwsgi
EXPOSE 8000

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8000", "--module", "app:app", "--processes", "1", "--threads", "8"]
