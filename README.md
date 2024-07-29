# YACut
Проект YaCut — это сервис укорачивания ссылок. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.

## Содержание
- [Технологии](#технологии)
- [Запуск проекта](#запуск-проекта)
- [Использование](#использование)
- [Команда проекта](#команда-проекта)

## Технологии
- [**Python 3.12+**](https://www.python.org/downloads/release/python-3120/)
- [**Flask**](https://pypi.org/project/Flask/3.0.2/)
- [**Flask-SQLAlchemy**](https://pypi.org/project/SQLAlchemy/2.0.21/)
- [**WTForms**](https://pypi.org/project/WTForms/3.0.1/)


## Запуск проекта

Клонируйте репозиторий и перейдите в него:
```shell
$ git clone https://github.com/4its/yacut.git && cd yacut
```

Создайте и активируйте виртуальное окружение(пример команды на Linux):
```shell
$ python3.12 -m venv venv && source venv/bin/activate
```

Обновите PIP и установите необходимые зависимости:
```shell
$ pip install upgrade pip && pip install -r requirements.txt
```

Создайте файл переменных окружения `.env` со следующими обязательными параметрами:
```text
FLASK_APP=yacut
FLASK_DEBUG=1
DATABASE_URI=sqlite:///db.sqlite3
SECRET_KEY=YOUR_SUPER_SECRET_KEY
```
Описание параметров можно найти в файле `env_example`.

Примените миграции(и создание базы данных):
```shell
$ flask db upgrade    
```

Запуск проекта:
```shell
$ Flask run
```

## Использование

После запуска проекта, Вам будут доступны как Web версия, так и API:

#### Адрес по умолчанию: [**http://127.0.0.1:5000**](http://127.0.0.1:5000)
#### Документацию можно посмотреть тут: https://app.swaggerhub.com/apis/EGIAZARYAN/ya_cut_project/0.1.0

## Команда проекта
- [**Georgii Egiazarian**](https://github.com/4its)
