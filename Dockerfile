# From https://hub.docker.com/r/nikolaik/python-nodejs/
FROM nikolaik/python-nodejs:latest

# Create and change to the app directory.
WORKDIR /usr/src/app

# Copy local code to the container image.
COPY . ./

RUN pip install -r requirements

# Run the web service on container startup.
CMD [ "./deploy.sh" ]
