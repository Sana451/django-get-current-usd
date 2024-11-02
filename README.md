# Django проект Get-current-usd возвращает актуальный курс доллара к рублю и 10 последних запросов курса в формате JSON.

## Для получения курса использовано внешнее API https://www.exchangerate-api.com/.
## Между каждым запросом курса должна быть пауза не менее 10 секунд.

# Инструкция по развёртыванию
* Скачать исходный код проекта: `git clone https://github.com/Sana451/django-get-current-usd.git`
* Перейти в папку с проектом: `cd django-get-current-usd/`
* Установить виртуальное окружение: `python -m pip install --upgrade pip && pip install virtualenv`
* Создать виртуальное окружение `python -m virtualenv django_virtualenv`
* Активировать виртуальное окружение:
1. Для OS Windows  `django_virtualenv\Scripts\activate`
2. Для OS Linux `source django_virtualenv/bin/activate`
* Установить зависимости: `pip install -r requirements.txt`
* Запустить сервер `python manage.py runserver`

## Использование

После запуска контейнера перейти на
URL: [http://127.0.0.1:8000/get-current-usd/](http://127.0.0.1:8000/get-current-usd/).