# STORE CLOTHES
## Этот проект сделан просто для понимания работы с django
### Проект не доделан полностью!

# Установка и запуск проекта
В корне проекта:
1. Устанавливаем необходимые пакеты
    ```
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
2. Запуск проекта
    ```
   ./manage.py migrate
   ./manage.py loaddata products/fixtures/categories.json
   ./manage.py loaddata products/fixtures/goods.json
   ./manage.py runserver
   ```