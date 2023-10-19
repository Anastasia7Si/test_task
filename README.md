# test_task
Тестовое задание для Bewise.ai

## Прокет доступен по адресу: http://localhost/quizzes/
Примеры запроса POST:
{
    "count": 4
}

Ответ:

{
    "question_text": "A Hungarian inventor is famous for this puzzling cube"
}

### Запуск проекта в контейнере
Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:Anastasia7Si/test_task.git
cd test_task
```
В папке проекта /infra создать файл .env и прописать в него свои данные.
Пример:
```
POSTGRES_DB=example
POSTGRES_USER=example_user
POSTGRES_PASSWORD=example_password
DB_HOST=example_db
DB_PORT=5432
DB_ENGINE=django.db.backends.postgresql
SECRET_KEY='projectparol'
```
Запустить проект через docker-compose:
```
docker compose -f docker-compose.yml up
```
Подготовить и выполнить миграции:
```
docker compose -f docker-compose.yml exec backend python manage.py makemigrations
docker compose -f docker-compose.yml exec backend python manage.py migrate
```
Создать суперюзера:
```
sudo docker compose -f docker-compose.yml exec backend python manage.py createsuperuser
```
Собрать статику и скопировать ее:
```
docker compose -f docker-compose.yml exec backend python manage.py collectstatic
docker compose -f docker-compose.yml exec backend cp -r /app/collected_static/. /static/
```
### Автор
- Пушкарная Анастасия(https://github.com/Anastasia7Si)