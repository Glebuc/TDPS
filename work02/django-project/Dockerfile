FROM ubuntu:latest
MAINTAINER Gleb Deryugin 'gleb567892@gmail.ru'
RUN apt-get update -qy
RUN apt-get install -qy python3.10 python3-pip python3-dev
COPY . /my_project
WORKDIR /my_project
RUN pip install -r requirements.txt
CMD ["python3", "/my_project/my_project/manage.py", "runserver", "127.0.0.1:8000"]
