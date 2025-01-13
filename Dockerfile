#Use official Python runtime as parent image
FROM python:3.12-slim

#Set the working directory in the container
WORKDIR /app

#Install FFmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg

#install aws cli \
RUN apt-get install -y awscli

#copy current code into container at /app
COPY . /app

#install packages
RUN pip install --no-cache-dir -r requirements.txt

#Run app.py when the container launches
CMD ["uvicorn", "main:app", "--host","0.0.0.0", "--port", "80"]
