# Установка и настройка

---

## Подготовка

Данный гайд подразумевает что у вас в системе уже стоит:

- [Python](https://www.python.org/downloads/)
- Heroku CLI
  - Гайд по [установке](https://devcenter.heroku.com/articles/heroku-cli#download-and-install) и [настройке](<https://devcenter.heroku.com/articles/heroku-cli#getting-started>) (создавать новое приложение не нужно, только авторизироваться в аккаунт)
- Так же необходимо установить [PostgresSQL](https://www.postgresql.org/download/)

---

## Установка репозитория

1. Клонировать репозиторий одной из команд:
    - Если настроен SSH ключ:``` git clone git@bitbucket.org:code-and-fun/web-app.git ```
    - Через https (требуется логин): ``` git clone https://<YOUR_USER_NAME>@bitbucket.org/code-and-fun/web-app.git ```

2. В корневой папке создать виртуальное окружение:
    - Стандартный алгоритм:
        - ```python3 -m venv venv```
    - Я рекомендую поставить virtualenv и создавать с его помощью:
        - ``` pip install virtualenv ```
        - ``` virtualenv venv ```
3. Активировать виртуальное окружение
    - ```.\venv\Scripts\activate```
4. Установаить зависимости:
    - ``` pip install -r requirements.txt ```
5. Получить переменные среды с heroku:
    - Перед получением всех переменных, их можно посмотреть, использовав команду ``` heroku config -a cloud-reader ```
    - Секретный ключ django: ``` heroku config:get DJANGO_KEY -s  >> .env -a cloud-reader ```
    - Для базы данных есть несколько вариантов:
        - Подключение к удалённой базе данных специально созданной для разработки: ``` heroku config:get HEROKU_POSTGRESQL_TEAL_URL -s  >> .env -a cloud-reader ```
        - Запустить базу данных локально как-то можно и это даже рекомендует Heroku, но у меня не получилось сделать это по его рекомендациям. Но всегда можно настроить её самостоятельно.
6. Запустить приложение локально:
    - Для Linux: ``` heroku local web ```
    - Для Windows: ``` local -f .\Procfile.windows ```

## Важные заметки

При разработке локально доступ к бд для разработки можно будет получить несколькими способами:

1. Сайт администратора. Для доступа к нему необходимо создать супер пользователя (если он не был создан ранее). ``` python manage.py createsuperuser ```
2. Подключиться при помощи psql или [pgcli](https://www.pgcli.com) (pgAdmin не пробовал), использую url полученный с heroku.
