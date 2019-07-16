# our base image
FROM python:3.7-alpine

# working directory
WORKDIR /app

# copy current directory into the container
ADD . /app

# install requirements
RUN pip3 install -r requirements.txt

# make port 8000 available to the world
EXPOSE 8000

CMD ["gunicorn", "--config", "./conf/gunicorn_conf.py", "src:app"]