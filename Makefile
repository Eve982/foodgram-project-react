service_name := web
docker_file_path := -f ./infra/docker-compose.yaml
bash_command := exec $(service_name) python manage.py
args = $(filter-out $@,$(MAKECMDGOALS))
container_id := $$(docker-compose $(docker_file_path) ps -q $(service_name))

run:
	docker-compose $(docker_file_path) up -d --build

rebuild:
	docker-compose $(docker_file_path) up -d --build

migrate:
	docker-compose $(docker_file_path) $(bash_command) migrate

user:
	docker-compose $(docker_file_path) $(bash_command) createsuperuser

stat:
	docker-compose $(docker_file_path) $(bash_command) collectstatic --no-input

stop:
	docker-compose $(docker_file_path) down -v

bd:
	docker cp ./infra/fixtures.json "$(container_id)":/app

load:
	docker-compose $(docker_file_path) $(bash_command) loaddata fixtures.json

clist:
	docker container ls -a --format="table {{.ID}}\t{{.Names}}"

ilist:
	docker image ls

print:
	printf "$(args)" -$(args)