# Recipe API

This project is my implementation of course project for [Backend REST API with Python & Django - Advanced](http://londonapp.dev/django-python-advanced). This is
a **Django REST Framework** application for managing recipes, users, and authentication. It includes an **NGINX reverse proxy**, a **PostgreSQL database**, and **Docker-based deployment**.

## How to Set Up and Run the Project Locally

Follow these steps to copy and run the **Recipe API** project on your local development machine.

### Clone the Repository

```sh
git clone https://github.com/serious-pavel/recipe-api.git
cd recipe-api
```
### Set Up Environment Variables
Edit the .env file and update database credentials and SECRET_KEY.
```sh
cat .env.sample > .env
```
### Build and Start the Containers
```sh
docker-compose build
docker-compose up -d
```
### Run Migrations and Create a Superuser
```sh
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
```
### Access the Application
API Base URL: http://127.0.0.1:8000/api/
Admin Panel: http://127.0.0.1:8000/admin/
### Running Tests & Code Checks
```sh
docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "flake8"
```
### Stopping and Cleaning Up
```sh
docker-compose down
docker-compose down --volumes --remove-orphans
```

## Useful commands

### Running the project with Docker
```sh
docker-compose build
docker-compose up -d
#up only db service
docker-compose up db
docker-compose down
docker-compose -f docker-compose-deploy.yml build
docker-compose -f docker-compose-deploy.yml up -d
docker-compose -f docker-compose-deploy.yml down
#restart service without its dependent services
docker-compose -f docker-compose-deploy.yml up --no-deps -a app
```

### Managing Django Application
```sh
docker-compose run --rm app sh -c "django-admin startproject app ."
docker-compose run --rm app sh -c "python manage.py migrate"
docker-compose run --rm app sh -c "python manage.py createsuperuser"
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"
docker-compose run --rm app sh -c "python manage.py wait_for_db"
```
### Deployment with docker-compose-deploy.yml
```sh
docker-compose -f docker-compose-deploy.yml build
docker-compose -f docker-compose-deploy.yml up -d
docker-compose -f docker-compose-deploy.yml down
```
### Docker Maintenance Commands
```sh
docker ps
docker volume ls
docker volume rm recipe-api_dev-db-data
open -a Docker
```
### Cleaning
```sh
docker system prune -a --volumes
```
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all anonymous volumes not used by at least one container
  - all images without at least one container associated to them
  - all build cache


```sh
docker compose down --volumes --remove-orphans
```
 - **_docker compose down_**: Stops and removes all containers defined in the docker-compose.yml file.
 - **_--volumes_**: Removes all named and anonymous volumes associated with the stopped containers. This will delete database data, uploaded files, and other persistent data stored in Docker volumes.
 - **_--remove-orphans_**: Removes any containers that are not defined in the current docker-compose.yml file but are part of the same Docker Compose project. This helps clean up unused services that might have been left running from previous configurations.
 
### NGINX Proxy & Static Files
```sh
cd proxy
docker build .
cd ..
docker volume ls
docker-compose run --rm app sh -c "python manage.py collectstatic --noinput"
```
### Additional Resources
[Advanced Deployment Guide](https://github.com/LondonAppDeveloper/build-a-backend-rest-api-with-python-django-advanced-resources/blob/main/deployment.md)
