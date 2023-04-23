service_name := web
docker_file_path := -f ./infra/docker-compose.yml
bash_command := exec $(service_name) python manage.py
args = $(filter-out $@,$(MAKECMDGOALS))
container_id := $$(docker-compose $(docker_file_path) ps -q $(service_name))

isort:
	isort /Users/olga/dev/foodgram-project-react/backend/ .

flake:
	flake8 /Users/olga/dev/foodgram-project-react/backend/ --exclude=venv,migrations,tests,settings.py

run:
	python3 /Users/olga/dev/foodgram-project-react/backend/foodgram/manage.py runserver

mm:
	python3 /Users/olga/dev/foodgram-project-react/backend/foodgram/manage.py makemigrations

migrate:
	python3 /Users/olga/dev/foodgram-project-react/backend/foodgram/manage.py migrate

createsuperuser:
	python3 /Users/olga/dev/foodgram-project-react/backend/foodgram/manage.py createsuperuser

docker_run:
	docker-compose $(docker_file_path) up --build

docker_rebuild:
	docker-compose $(docker_file_path) up -d --build

docker_migrate:
	docker-compose $(docker_file_path) $(bash_command) migrate

docker_superuser:
	docker-compose $(docker_file_path) $(bash_command) createsuperuser

docker_stat:
	docker-compose $(docker_file_path) $(bash_command) collectstatic --no-input

docker_stop:
	docker-compose $(docker_file_path) down

copy_db:
	docker cp ./infra/fixtures.json "$(container_id)":/app

load_db:
	docker-compose $(docker_file_path) $(bash_command) loaddata fixtures.json

clist:
	docker container ls -a --format="table {{.ID}}\t{{.Names}}"

ilist:
	docker image ls

print:
	printf "$(args)" -$(args)
