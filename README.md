# Django проект, "/get-current-usd/" возвращает актуальный курс доллара к рублю и 10 последних запросов курсов в формате JSON. 

## Для получения курса использовано внешнее API https://www.exchangerate-api.com/.
## Между каждым запросом курса должна быть пауза не менее 10 секунд.


# Инструкция по развёртыванию
Скачать исходный код проекта: `git clone https://github.com/Sana451/django-get-current-usd.git`    
Перейти в папку с проектом: `cd django-get-current-usd/`
Установить зависимости: `pip install -r requirements.txt`

Произвести сборку контейнера: `docker build --progress=plain --no-cache -t weather-app .`    
Запустить контейнер: `docker run -it --rm -p 8000:8000 --name weather-app weather-app`    

## Использованиеы
После запуска контейнера перейти на URL: [http://127.0.0.1:8000/get-current-usd/](http://127.0.0.1:8000/get-current-usd/).