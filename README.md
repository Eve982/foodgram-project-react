## **Описание проекта:**

[![.github/workflows/foodgram_workflow.yml](https://github.com/Eve982/foodgram-project-react/actions/workflows/foodgram_workflow.yml/badge.svg)](https://github.com/Eve982/foodgram-project-react/actions/workflows/foodgram_workflow.yml)

Проект представляет собой ресурс, где посетители без авторизации могут читать рецепты. Фронтенд написан на React, бекенд на DRF.
Авторизованые пользователи могут:
- публиковать/удалять рецепты, добавлять теги своим рецептам;
- подписаться/отписаться от автора рецептов;
- отдельная страница с рецептами только избранных авторов;
- добавить/удалить рецепт из списка покупок;
- скачать список покупок, который автоматически формируется на основе рецептов из списка покупок;

Проект находится тут:
```
http://ola.sytes.net/
```
Здесь лежит Redoc:
```
http://ola.sytes.net/api/docs/
```
Админзона проекта (доступна только администратору):
```
http://ola.sytes.net/admin/
```
Логин для доступа к админ зоне:
```
test@test@test
```
Пароль для доступа к админ зоне:
```
test1234
```

## **Как запустить проект:**
Все команды необходимо выполнять в командной строке Вашего ПК. Первую команду следует выполнять в той локальной папке своего ПК, в которую Вы хотите склонировать проект из стороннего репозитория.
Клонировать репозиторий выполнением следующей команды в командной строке:
#
```
git clone <сссылка на проект>
```
если Вы используете SSH-подключение, то, вместо <сссылка на проект>, укажите:
```
git@github.com:Eve982/foodgram-project-react.git
```
для HTTPS-подключений укажите следующую ссылку:
```
https://github.com/Eve982/foodgram-project-react.git
```
Перейти в клонированый проект командой:
```
cd foodgram_project_react
```
## Запуск приложения в Docker-контейнерах на локальной машине:

Убедитесь, что на Вашем компьютере установлен и запущен Docker.
Находясь в папке проекта зайдите в папку infra выполнив следующую команду в терминале
```
cd infra
```
Откройте файл docker-compose.yml и замените следующую строку в разделе backend:
```
image: eve982/foodgram_backend:latest
```
на эту:
```
build: ../backend/
```
а строку в разеделе frontend:
```
eve982/foodgram_frontend:latest
```
на эту:
```
build: ../frontend/
```
В папке backend создайте и наполните файл '.env' по этому [шаблону](#шаблон-наполнения-env-файла).

Запустите контейнер
```
docker-compose up
```
Для пересборки контейнеров, в случае, если Вы вносили изменения в проект выполните команду:
```
docker-compose up -d --build
```
Создайте суперпользователя для доступа к админ зоне:
```
docker-compose exec web python manage.py createsuperuser
```
Соберите статику:
```
docker-compose exec web python manage.py collectstatic --no-input
```
Проект запущен и доступен по адресу: [http://localhost/](http://localhost/)

<!-- ### **Загрузка тестовых данных в БД**
Узнать CONTAINER ID запущенных контейнеров можно выполнив команду:
```
docker container ls
```
Получить список всех контейнеров можно выполнив команду:
```
docker container ls -a
```
Список только названий и ID контейнеров:
```
 docker container ls --format="table {{.ID}}\t{{.Names}}"
```
Остановить все запущеные контейнеры:
```
docker container stop $(docker container ls -q)
```
Чтобы загрузить тестовые данные в БД, перейдите в каталог проекта и скопируйте файл базы данных в контейнер приложения (Вам нужен контейнер с приставкой -web в названии):
```
docker cp fixtures.json <CONTAINER ID>:/app
```
СПОСОБ 1:
Выполните команду:
```
docker-compose exec web python manage.py loaddata fixtures.json
```
СПОСОБ 2:
Перейдите в контейнер приложения:
```
docker container exec -it <CONTAINER ID> bash
```
Выполните команду для загрузки данных в БД:
```
python manage.py loaddata
```
Для того чтоб сохранить внесенные изменения в БД:
```
docker-compose exec web python manage.py dumpdata > fixtures.json
``` -->
## **Шаблон наполнения env-файла:**

```
ALLOWED_HOSTS=['*', 'localhost']
```
Cекретный ключ, необходимый фреймворку Django для хэширования данных. Можно воспользоваться любым онлайн сервисом для генерации этого ключа:
```
SECRET_KEY=secret-key
```
Настройка режима разработки в продакшене должна быть в режиме False:
```
DEBUG=False
```
Используемая база данных, как правило это postgresql:
```
DB_ENGINE=django.db.backends.postgresql
```
Указываем название сервиса (контейнера):
```
DB_HOST=db
```
Указываем порт для подключения к БД:
```
DB_PORT=5432
```
Имя БД:
```
POSTGRES_DB=foodgram
```
Логин для подключения к БД:
```
POSTGRES_USER=login
```
Пароль для подключения к БД:
```
POSTGRES_PASSWORD=password
```
<!-- Далее, перейдите на Вашу страницу GitHub(GitLab) в раздел 'Actions secrets and variables' и добавьте все указанные выше переменные. Кроме того, Вам нужно добавить еще несколько переменные:
Здесь нужно указать IP-адрес Вашего сервера и его доменное имя(при наличии):
```
ALLOWED_HOSTS=['публичный_IP_адрес_сервера', 'example.syte.net', 'localhost', '*']
```
```
HOST=<публичный_IP_Вашего_сервера>
```
```
USER=логин_созданный_при_создании_сервера
```
```
SSH_KEY=[приватный_ключ_с_локальной_машины](#чтобы-вывести-список-всех-ключей-в-терминал-локальной-машины)
```
```
DOCKER_PASSWORD=Docker_пароль
```
```
DOCKER_USERNAME=Docker_логин
```
```
TELEGRAM_TO=имя_телеграм_бота
```
```
TELEGRAM_TOKEN=телеграм_токен
```

Зайти на свой сервер выполнив в терминале локальной машины команду:
```
ssh <логин_созданный_при_создании_сервера>@<публичный_IP_адрес_сервера>
```
Скачать проект на сервер командой 'git clone' [по аналогии с тем, как описано выше](#) для локальной машины.

На локальной машине из корня проекта выполнить команды для отправки всех изменений в Ваш репозиторий на GitHub или GitLab, если Вы используете его:
```
git add .
git commit -m 'change setiings for new server'
git push
```
Зайдите на страницу своего удаленного репозитория в раздел Actions и дождитесь пока весь workflow успешно завершится.

После успешного деплоя на Ваш сервер, Вам останется лишь выполнить пару команд на сервере.

Войти в командную строку контейнера на сервере:
```
sudo docker exec -it infra-backend-1 bash
```
Выполнить команду для сбороа статики:
```
python manage.py collectstatic --no-input
```
Проект успешно запущен на Вашем сервере!


# Где взять приватный SSH-ключ:
Выполните в терминале локальной машины команду для получения списка всех SSH-ключей:
```
ls -al ~/.ssh
```
Приватный ключ может называться id_rsa или id_ed25519 без расширения .pub. Чтобы скопировать его в буфер обмена выполните команду:
```
pbcopy < ~/.ssh/<название_ключа>
``` -->
<!-- 
docker-compose exec backend python manage.py collectstatic --no-input
sudo docker exec -it infra-backend-1 bash
 -->