# Allergen

## Requirements 
* [Docker](https://www.docker.com/get-started)

## Set up with docker
```
docker-compose build
docker-compose up
```

## Populate the database 
```docker-compose run django python manage.py loaddata db.json```

## Run the project
```docker-compose up```

## Front-end endpoint
* Go to 0.0.0.0:8080

## Back-end endpoint 
* Go to 0.0.0.0:8000

## Read swagger endpoint
* Go to 0.0.0.0:8000/docs/