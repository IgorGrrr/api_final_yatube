# api_final

Yatube API позволяет взаимодействовать с социальной сетью Yatube. Функционал позволяет публиковать посты и комментарии и управлять подписками с помощью програмного интерфейса. Проект реализован с помощью Django REST Framework
***

## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/IgorGrrr/api_final_yatube.git`

`cd api_final_yatube`

Cоздать и активировать виртуальное окружение:

`python3 -m venv env`

`source env/bin/activate`

`python3 -m pip install --upgrade pip`


Установить зависимости из файла requirements.txt:

`pip install -r requirements.txt`

Выполнить миграции:

`python3 manage.py migrate`

Запустить проект:

`python3 manage.py runserver`
***

## Примеры запросов

POST запрос 