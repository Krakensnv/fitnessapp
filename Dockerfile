#Dockerfile
#docker build -t fitnessapp .
#docker run -d -p 5000:5000 fitnessapp

FROM python:3.10-slim-buster
ADD . /fitnessapp
WORKDIR /fitnessapp
RUN pip install --no-cache-dir -r requirements.txt
CMD [ "python", "./run.py" ]
