# This is dir 'work02'

## For start django-project

cd /django-project

docker build -t django_app .

docker run -it -p 8000:8000 django_app
