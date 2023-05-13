# RESTful Web Service Implementation + Docker

## This project contains five endpoints:

### 1. GET /: Root of the application. This serves as a simple welcome page which displays the welcome message 
### 2. GET /Customers: Route to display all customers in the customers.json file
### 3. GET /Customers/{id}: Route to display a specific customer based on the id provided
### 4. GET /Customers/<int:id>/orders: # Route to display all orders for a given customer ID
### 5. GET /app.route('/customers/<int:customer_id>/orders/<int:order_id>':Route to display a single order by customer and order ID

## We run the application on the docker container using the dockerfile as implemented below:

FROM ubuntu:20.04

Update OS and install required packages
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y upgrade && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-pip \
    libssl-dev


#Add requirements.txt
COPY requirements.txt /webapp/

#Install uwsgi Python web server
RUN pip3 install uwsgi

#Install app requirements
RUN pip3 install -r /webapp/requirements.txt

#Create app directory
COPY . /webapp/

#Set the default directory for our environment
ENV HOME /webapp
WORKDIR /webapp

#Expose port 8000 for uwsgi
EXPOSE 8000

ENTRYPOINT ["uwsgi", "--http", "0.0.0.0:8000", "--module", "app:app", "--processes", "1", "--threads", "8"]



## How to run the application 

1. ## Build the dockerfile using the command below:
    docker build -t flask .
2. ## Run the dockerfile using the command below:
    docker run -d -p 8000:8000 flask. The -d option runs the command in the deamon mode meaning that the container runs in the background
3. ## To check if the container is running, use the command below:
    docker ps -a
4. ## To check all the images in docker use the command below:
    docker images
4. ## To stop the container, use the command below:
    docker stop <container_id>
5. ## To remove the container, use the command below:
    docker rm <container_id>
6. ## To remove the image, use the command below:
    docker rmi <image_id>
    
    
  The recordings and the powerpoint to be submitted as a part of the assignment are uploaded at: https://drive.google.com/drive/folders/1DgzFNtSqQWpOGiF1IvFG8Ywsedi7N5ix?usp=sharing
