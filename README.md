# recipe-api

docker-compose down
docker-compose run --rm app sh -c "django-admin startproject app ."

docker-compose build
docker-compose run --rm app sh -c "flake8"
docker-compose run --rm app sh -c "python manage.py test"

docker-compose up


docker-compose run --rm app sh -c "python manage.py wait_for_db"