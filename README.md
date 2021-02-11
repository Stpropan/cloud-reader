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
    - ``` heroku config:get DJANGO_KEY -s  >> .env -a cloud-reader ```
    - ``` heroku config:get DATABASE_URL -s  >> .env -a cloud-reader ```
6. Запустить приложение локально:
    - Для Linux: ``` heroku local web ```
    - Для Windows: ``` local -f .\Procfile.windows ```
7. Не проверено:
