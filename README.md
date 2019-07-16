# README
This code is a Hello World and a sample structure using Flask with gunicorn as a server and docker.

## Getting started
Let's clone the git repository:
```bash
git clone https://github.com/erasmosouza/flask-quickstart.git
```
```bash
cd flask-quickstart
```

In the root directory of app there is a Dockerfile, and all you need is build the image with Docker: 
```bash
docker build -t flask-quickstart .
```
Then, run it:
```bash
docker run -p 8000:8000 flask-quickstart
```

Now you can open your favorite browser and access the application through `http://localhost:8000/` 

## Cleaning up
Now, let's remove our container and clean up our mess. 

Get the container id: 
```bash
$ docker ps -a
```

Pick the container id and delete it. You can use `-f` to force removing the container even it is running: 
```
docker rm -f <container-id>
```

Let's now delete the image, get the image id:
```
docker image ls
```

Delete it: 
```
docker image rm <image-id>
```

## Sample Docker image
There is a sample image I've hosted in Docker Hub, you can get [here](https://cloud.docker.com/u/erasmopinheiro/repository/docker/erasmopinheiro/sample-flask-app).


