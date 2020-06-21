FROM python:latest
WORKDIR /app/src
COPY ./requirements.txt ./
RUN ["apt-get", "update", "-y"]
RUN ["apt-get", "install", "cmake", "-y"]
RUN ["pip3", "install", "-r", "requirements.txt"]
RUN ["pip3", "install", "requests"]
COPY . .
ENV FLASK_APP index.py
ENV IMAGE_URL "http://localhost:8080/"
CMD ["flask", "run", "--host=0.0.0.0"]
