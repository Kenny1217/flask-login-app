FROM python:3.13.1

# Set environment variables
ENV FLASK_APP_USER="flask_user"
ENV FLASK_APP_USER_HOME="/usr/local/$FLASK_APP_USER"

# Switch to root user
USER root

# Create a non-root user
RUN useradd --shell /bin/bash -d "$FLASK_APP_USER_HOME" -m -u 1001 "$FLASK_APP_USER"

# Update and upgrade packages on base docker image
RUN apt-get update && apt-get upgrade

# Copy requirements.txt file to docker image
COPY ./requirements.txt "$FLASK_APP_USER_HOME/requirements.txt"

# Install packages in requirements.txt to docker image
RUN pip3 install -r "$FLASK_APP_USER_HOME/requirements.txt"

# Expose port 8080 for flask application
EXPOSE 8080

# Switch to non-root user
USER "$FLASK_APP_USER"

# Set working directory
WORKDIR "$FLASK_APP_USER_HOME"