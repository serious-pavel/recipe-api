# recipe-api

docker-compose down
docker-compose run --rm app sh -c "django-admin startproject app ."

docker-compose build
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"

docker-compose up


docker-compose run --rm app sh -c "python manage.py wait_for_db"


docker compose down --volumes --remove-orphans
docker system prune -a --volumes
WARNING! This will remove:
  - all stopped containers
  - all networks not used by at least one container
  - all anonymous volumes not used by at least one container
  - all images without at least one container associated to them
  - all build cache

docker ps


docker volume ls
[docker-compose down]
docker volume rm recipe-api_dev-db-data

docker-compose run --rm app sh -c "python manage.py createsuperuser"

open -a Docker



cd proxy
docker build .