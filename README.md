# trip.cat
App for traveling

## Установка зависимостей
pip install -r requirements.txt

## Настройка переменных окружения
set FLASK_APP=main.py
set FLASK_ENV=development -- для запуска в режиме тестирования

### Запуск приложения
flask run --param=value
Параметры:
host, port, debug, ...
