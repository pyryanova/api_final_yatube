# API Yatube

REST API для социальной сети **Yatube**.

Пользователи могут:
- публиковать посты с изображениями (в формате base64);
- просматривать и комментировать чужие посты;
- подписываться на авторов;
- просматривать список сообществ.

Реализована:
- аутентификация по JWT-токену (`JWTAuthentication` через Djoser);
- разграничение прав доступа;
- вложенные ресурсы;
- сериализация и валидация данных через Django REST Framework.

---

## Технологии

- Python 3.10+
- Django 4.x
- Django REST Framework
- Djoser + SimpleJWT
- SQLite (по умолчанию)

---

## Установка и запуск

1. Клонировать репозиторий:

   ```bash
   git clone https://github.com/pyryanova/api_final_yatube.git
   cd api_final_yatube
   ```

2. Создать и активировать виртуальное окружение:

   ```bash
   python -m venv venv
   source venv/bin/activate  # для Windows: venv\Scripts\activate
   ```

3. Установить зависимости:

   ```bash
   pip install -r requirements.txt
   ```

4. Выполнить миграции:

   ```bash
   python manage.py migrate
   ```

5. Запустить сервер разработки:

   ```bash
   python manage.py runserver
   ```

6. Открыть документацию API:

   ```
   http://127.0.0.1:8000/redoc/
   ```

---

## Аутентификация

Используется JWT-аутентификация через Djoser.

- Получение токена:
  ```http
  POST /api/v1/jwt/create/
  ```

- Обновление токена:
  ```http
  POST /api/v1/jwt/refresh/
  ```

- Проверка токена:
  ```http
  POST /api/v1/jwt/verify/
  ```

- Передача токена:
  ```http
  Authorization: Bearer <ваш_токен>
  ```

> ⚠️ **Важно:** Анонимные пользователи могут только просматривать ресурсы. Для создания и редактирования требуется авторизация.

---

## Тестирование

Для запуска автотестов:

```bash
pytest
```

---

## Postman

1. В папке `postman_collection/` находится коллекция для ручной проверки API.
2. Импортируйте файл `CRUD_for_yatube.postman_collection.json` в Postman.
3. Используйте коллекцию для тестирования всех эндпоинтов.

---

## Лицензия

Проект создан в учебных целях в рамках обучения на Яндекс.Практикуме.  
Исходный код: [https://github.com/pyryanova/api_final_yatube](https://github.com/pyryanova/api_final_yatube)
