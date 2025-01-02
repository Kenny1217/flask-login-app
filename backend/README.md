# Flask Application Backend:
This directory contains all the required backend components for the flask application to run.
- [Dockerfile](./docker/Dockerfile)
- [Requirements.txt](./docker/requirements.txt)

## Dockerfile Setup:

### Step 1: Define the base image
```
FROM python:3.13.1
```

### Step 2: Define environment variables
```
ENV FLASK_APP_USER="flask_user"
ENV FLASK_APP_USER_HOME="/usr/local/$FLASK_APP_USER"
```

### Step 3: Switch to root user 
```
USER root
```

### Step 4: Create a non-root user
```
RUN useradd --shell /bin/bash -d "$FLASK_APP_USER_HOME" -m -u 1001 "$FLASK_APP_USER"
```

### Step 5: Update base docker image
```
RUN apt-get update && apt-get upgrade
```

### Step 6: Move requirements.txt file to docker image
```
COPY ./requirements.txt "$FLASK_APP_USER_HOME/requirements.txt"
```

### Step 7: Install packages in requirements.txt to docker image
```
RUN pip3 install -r "$FLASK_APP_USER_HOME/requirements.txt"
```

### Step 8: Expose port 8080 for application
```
EXPOSE 8080
```

### Step 9: Switch to non-root user 
```
USER "$FLASK_APP_USER"
```

### Step 10: Set the docker image working directory
```
WORKDIR "$FLASK_APP_USER_HOME"
```
