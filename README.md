# Телеграм-бот для пицерии

**сценарий:** Необходимо разработать телеграм-бота для пиццерии. Основная задача бота - вывод в чат меню.

**функционал:** Бот работает в связке с БД. Кроме непосредственно бота, реализована также и админка с *CRUD* функционалом. 

# Как запустить на localhost:
## Приложение считывает несколько переменных окружения:
- *db_uri* - соединение с базой данных, по умолчанию - SQLite pizza_shop.sqlite
- *username* - логин к админке
- *password* - пароль к админке
- *secret_key* - секретный ключ для Flask
- *token* - ключ от телеграм-бота, получить можно у [@BotFather](https://telegram.me/botfather)

## Перед запуском необходимо установить зависимости из requirements.txt:
```#!bash
pip install -r requirements.txt
```

## Создаем модели:
```#!bash
python models.py
```

## Заносим в БД первоначальный каталог:
```#!bash
python load_catalogue.py
```

## Запуск серверного скрипта
Запустить локально
```#!bash
python server.py 
```
Затем открыть в браузере [http://127.0.0.1:5000/admin/](http://127.0.0.1:5000/admin/)

## Запуск скрипта бота
```#!bash
python bot.py 
```

# Цели проекта

Код написан в образовательных целях. Курс веб-разработки – [DEVMAN.org](https://devman.org)
